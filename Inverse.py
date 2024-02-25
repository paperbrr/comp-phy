from GaussElim import *

matrix = [[1,2,-1, 0],
          [2,1,2, 0],
          [-1,2,1, 0]]

dim = 3

def copyAugMatrix(matrix,dim):
    copy = []
    for i in range(dim):
        currentRow = []
        for j in range(dim+1):
            currentRow.append(matrix[i][j])
        copy.append(currentRow)
    return copy

def createIdentity(dim):
    identity = []
    for i in range(dim):
        currentRow = []
        for j in range(dim):
            if i == j:
                currentRow.append(1)
            else:
                currentRow.append(0)
        identity.append(currentRow)
    return identity

def findInverse(matrix, dim):
    ansMatrix = []
    for i in range(dim):
        currentRow = []
        for j in range(dim):
            currentRow.append(0)
        ansMatrix.append(currentRow)

    identityMatrix = createIdentity(dim)

    printMatrix(matrix)

    for i in range(dim):
        copy = copyAugMatrix(matrix, dim)
        changedSol = changeSolCol(copy, identityMatrix[i], dim)
        converted = convertToEchelon(changedSol, dim)
        sols = backSubstitute(converted, dim)
        for j in range(dim):
            ansMatrix[j][i] = sols[j]

    return ansMatrix