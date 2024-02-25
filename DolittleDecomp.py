matrix = [[2,4,3],
          [1,-2,-2],
          [-3,3,2]]

dim = 3

upper = [[0,0,0]*3]

lower = [[1,0,0],
         [1,1,0],
         [1,1,1]]

def printMatrix(matrix):
    for i in matrix:
        print(i)
    print("----------------")

for i in range(1, dim):
    for j in range(i):
        subFactor = matrix[i][j]/matrix[j][j]
        lower[i][j] = subFactor
        for k in range(dim):
            matrix[i][k] -= subFactor*matrix[j][k]

printMatrix(matrix)
printMatrix(lower)