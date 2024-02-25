from Utils import *

def DolittleDecomposition(matrix:list, dim:int)->tuple:
    '''returns a tuple containing the decomposed forms of the provided matrix, by Dolittle\'s method'''
    upper = copyMatrix(matrix, dim)
    lower = createTriangularMatrix(dim, 'lower')
    printMatrix(lower)
    printMatrix(matrix)
    printMatrix(upper)
    for i in range(1, dim):
        for j in range(i):
            subFactor = upper[i][j]/upper[j][j]
            lower[i][j] = subFactor
            for k in range(dim):
                upper[i][k] -= subFactor*upper[j][k]

    return lower, upper