def rotateMatrix90Degrees(matrix):
    newMat = makeMatrix(len(matrix))
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            newMat[y][len(matrix) - x - 1] = matrix[x][y]
    return newMat

def makeMatrix(n):
    mat = []
    for x in range(n):
        mat.append([])
        for y in range(n):
            mat[x].append(0)
    return mat

print(rotateMatrix90Degrees([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))
