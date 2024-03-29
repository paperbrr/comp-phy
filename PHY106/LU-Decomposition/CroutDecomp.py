from Utils import *

def CroutDecomposition(matrix:list, dim:int)->tuple:
    '''returns a tuple containing the decomposed forms of the provided matrix, by Crout\'s method'''
    upper = createTriangularMatrix(dim, 'upper')
    lower = copyMatrix(matrix, dim)

    for i in range(-2, -dim-1, -1):
        for j in range(-1, i, -1):
            subFactor = lower[i][j]/lower[j][j]
            upper[i][j] = subFactor
            for k in range(-1, -dim-1, -1):
                lower[i][k] -= lower[j][k]*subFactor

    return lower, upper

def findSolsCrout(matrix, ans, dims):
    '''find the solutions for the given matrix using crout\'s decomposition'''
    lower, upper = CroutDecomposition(matrix, dims)
    LY = createAugmentedMatrix(lower, dims, ans)
    Y = forwardSubstitute(LY, dims)
    UX = createAugmentedMatrix(upper, dims, Y)
    X = backSubstitute(UX, dims)

    return X