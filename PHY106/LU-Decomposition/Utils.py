def copyMatrix(matrix:list,dim:int)->list:
    '''returns a copy of the provided matrix to ensure the original doesn\'t get modified'''
    copy = []
    for i in range(dim):
        currentRow = []
        for j in range(dim):
            currentRow.append(matrix[i][j])
        copy.append(currentRow)
    return copy

def printMatrix(matrix:list)->None:
    '''prints a provided matrix (nested lists) in a formatted manner'''
    for i in matrix:
        print(i)
    print("----------------")

def createTriangularMatrix(dim:int, type:str)->list:
    '''returns a dim x dim upper or lower triangular matrix, depending on the given type. populates upper/lower with 1s'''
    matrix = []
    if type == 'upper':
        for i in range(dim):
            currentRow = []
            for j in range(dim):
                if j>=i:
                    currentRow.append(1)
                else:
                    currentRow.append(0)
            matrix.append(currentRow)
    elif type == 'lower':
        for i in range(dim):
            currentRow = []
            for j in range(dim):
                if j<=i:
                    currentRow.append(1)
                else:
                    currentRow.append(0)
            matrix.append(currentRow)
    return matrix        

def backSubstitute(matrix: list, dim: int) -> list:
    '''returns a dim x 1 matrix with solutions to the augmented matrix of dimensions dim given as arguments by using back substitution'''
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

def forwardSubstitute(matrix: list, dim: int) -> list:
    '''returns a dim x 1 matrix with solutions to the augmented matrix of dimensions dim given as arguments by using forward substitution'''
    sols = []
    sols.append(matrix[0][dim]/matrix[0][0])

    for i in range(1, dim):
        currentAns = matrix[i][dim]
        currentSol = 0
        for j in range(0, i):
            currentSol += matrix[i][j]*sols[j]

        sols.append((currentAns-currentSol)/matrix[i][i])

    return sols

def createAugmentedMatrix(matrix, dim, augCol):
    augMatrix = copyMatrix(matrix, dim)
    for i in range(dim):
        augMatrix[i].append(augCol[i])
    return augMatrix