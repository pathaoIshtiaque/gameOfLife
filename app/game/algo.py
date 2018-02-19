def getAliveNeighborCount(i, j, len_i, len_j, data):
    count = 0
    if i > 0:
        if data[i-1][j] == 1:
            count += 1
        if j > 0 and data[i-1][j-1] == 1:
            count += 1
        if j < len_j-1 and data[i-1][j+1] == 1:
            count += 1
    if i < len_i-1:
        if data[i+1][j] == 1:
            count += 1
        if j > 0 and data[i+1][j-1] == 1:
            count += 1
        if j < len_j-1 and data[i+1][j+1] == 1:
            count += 1
    if j > 0:
        if data[i][j-1] == 1:
            count += 1
    if j < len_j-1:
        if data[i][j+1] == 1:
            count += 1
    return count

def increment(x, y, data):
    newData = []
    for i in range(y):
        newRow = []
        for j in range(x):
            count = getAliveNeighborCount(i, j, y, x, data)
            if count < 2:
                newRow.append(0)
            elif count == 2:
                if data[i][j] == 1:
                    newRow.append(1)
                else:
                    newRow.append(0)
            elif count == 3:
                newRow.append(1)
            else:
                newRow.append(0)
        newData.append(newRow)
    return newData

