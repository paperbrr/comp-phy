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