from Utils import *

def DolittleDecomposition(matrix:list, dim:int)->tuple:
    '''returns a tuple containing the decomposed forms of the provided matrix, by Dolittle\'s method'''
    upper = copyMatrix(matrix, dim)
    lower = createTriangularMatrix(dim, 'lower')

    for i in range(1, dim):
        for j in range(i):
            subFactor = upper[i][j]/upper[j][j]
            lower[i][j] = subFactor
            for k in range(dim):
                upper[i][k] -= subFactor*upper[j][k]

    return lower, upper

def findSolsDolittle(matrix, ans, dims):
    '''find the solutions for the given matrix using dolittle\'s decomposition'''
    lower, upper = DolittleDecomposition(matrix, dims)
    LY = createAugmentedMatrix(lower, dims, ans)
    Y = forwardSubstitute(LY, dims)
    UX = createAugmentedMatrix(upper, dims, Y)
    X = backSubstitute(UX, dims)

    return X