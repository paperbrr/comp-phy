matrix = [[2,4,3],
          [1,-2,-2],
          [-3,3,2]]

dim = 3

lower = [[0,0,0]*3]

upper = [[1,1,1],
         [0,1,1],
         [0,0,1]]

def printMatrix(matrix):
    for i in matrix:
        print(i)
    print("----------------")

for i in range(-2, -dim-1, -1):
    for j in range(-1, i, -1):
        subFactor = matrix[i][j]/matrix[j][j]
        upper[i][j] = subFactor
        for k in range(-1, -dim-1, -1):
            matrix[i][k] -= matrix[j][k]*subFactor

printMatrix(matrix)
printMatrix(upper)