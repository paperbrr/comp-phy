from Utils import *

def convertToEchelon(matrix: list, dim: int) -> list:
    '''returns an upper echelon matrix (non reduced) converted from a given augmented matrix with dimensions dim'''
    for i in range(dim):
        for j in range(i+1, dim):
            subFactor = matrix[j][i]/matrix[i][i]
            for k in range(dim+1):
                matrix[j][k] -= matrix[i][k] * subFactor
    return matrix

def backSubstitute(matrix: list, dim: int) -> list:
    '''returns a dim x 1 matrix with solutions to the augmented matrix of dimensions dim given as arguments'''
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