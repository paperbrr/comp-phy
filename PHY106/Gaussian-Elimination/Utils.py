def printMatrix(matrix:list)->None:
    '''prints a provided matrix (nested lists) in a formatted manner'''
    for i in matrix:
        print(i)
    print("----------------")

def changeSolCol(matrix:list, newSolCol:list, dim:int)->list:
    '''replaces the solution column of the provided augmented matrix with the new solution coloumn'''
    for i in range(dim):
        matrix[i][dim] = newSolCol[i]
    return matrix