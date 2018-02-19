from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from game.models import Grid
from game.algo import increment
import json

class GridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grid
        fields = ('id', 'x', 'y', 'data')

class GridViewSet(viewsets.ModelViewSet):
    queryset = Grid.objects.all()
    serializer_class = GridSerializer

    def retrieve(self, request, pk=None):
        grid = Grid.objects.get(id=pk)
        print(grid.data)
        newData = increment(grid.x, grid.y, json.loads(grid.data))
        grid.data = newData
        grid.save()
        return super(GridViewSet, self).retrieve(request)

router = routers.DefaultRouter()
router.register(r'grids', GridViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
