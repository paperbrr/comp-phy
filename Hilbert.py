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

def createAugHilbert(n):
    matrix = []
    for i in range(1,n+1):
        currentRow = []
        for j in range(1,n+1):
            currentRow.append(1/(i+j-1))
        currentRow.append(0)
        matrix.append(currentRow)

    return matrix

#hilbert
hInverse = findInverse(createAugHilbert(4), 4)
print(hInverse)