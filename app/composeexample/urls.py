from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from game.models import Grid
from game.algo import increment
import json
import re

class GridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grid
        fields = ('id', 'x', 'y', 'data')

class GridViewSet(viewsets.ModelViewSet):
    queryset = Grid.objects.all()
    serializer_class = GridSerializer

    def retrieve(self, request, pk=None):
        steps = [1]
        allNewData = []
        mod = False
        if 'after' in request.query_params:
            mod = True
            steps = re.findall(r"[0-9]+", request.query_params['after'])
            steps = list(map(lambda x: int(x), steps))
        grid = Grid.objects.get(id=pk)
        newData = json.loads(grid.data)
        for i in range(max(steps)):
            newData = increment(grid.x, grid.y, newData)
            if i+1 in steps:
                allNewData.append({"age": "<age_" + str(i+1) + ">", "grid": newData})
        grid.data = json.dumps(newData)
        grid.save()
        r = super(GridViewSet, self).retrieve(request)
        if mod:
            r.data['data'] = allNewData
        else:
            r.data['data'] = json.loads(r.data['data'])
        return r

router = routers.DefaultRouter()
router.register(r'grids', GridViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
