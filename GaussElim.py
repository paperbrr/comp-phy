matrix = [[2,4,3, 4],
          [1,-2,-2,0],
          [-3,3,2,-7]]

dim = 3

def printMatrix(matrix):
    for i in matrix:
        print(i)
    print("----------------")

def changeSolCol(matrix, newSolCol, dim):
    for i in range(dim):
        matrix[i][dim] = newSolCol[i]
    return matrix

def convertToEchelon(matrix, dim):
    for i in range(dim):
        for j in range(i+1, dim):
            subFactor = matrix[j][i]/matrix[i][i]
            for k in range(dim+1):
                matrix[j][k] -= matrix[i][k] * subFactor
    return matrix

def backSubstitute(matrix, dim):
    sols = []
    sols.append(matrix[dim-1][dim]/matrix[dim-1][dim-1])

    for i in range(dim-2, -1, -1):
        currentAns = matrix[i][dim]
        currentSol = 0
        for j in range(dim-1, i, -1):
            currentSol += matrix[i][j]*sols[dim-(j+1)]

        sols.append((currentAns-currentSol)/matrix[i][i])

    sols.reverse()
    return sols