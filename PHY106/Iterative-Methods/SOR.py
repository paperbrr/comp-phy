def IterateSOR(matrix:list, dims:int, ansMatrix:list, maxIters:int, maxErr:float, initialVals:list, omega)->tuple:
    '''returns the required iteration count and solution column after solving matrix in accordance with ansMatrix
    and ensuring that error is less than maxErr. More accurate initial values will lead to a lesser number of
    iterations needed. uses SOR method, so omega input is needed'''
    sols = [[i for i in initialVals]]
    ans = ansMatrix
    solsCount = 1

    while solsCount < maxIters:

        newSols = []
        for i in range(dims):
            currentAns = ans[i]
            for j in range(dims):
                if (i!=j):
                    if j<i:
                        currentAns -= matrix[i][j]*newSols[j]
                    else:
                        currentAns -= matrix[i][j]*sols[solsCount-1][j]
            currentAns *= omega/matrix[i][i]
            currentAns += (1-omega)*sols[solsCount-1][i]
            newSols.append(currentAns)
        sols.append(newSols)
        solsCount += 1

        check = 0

        for i in range(len(ans)):
            if abs(sols[solsCount-1][i] - sols[solsCount-2][i]) < maxErr:
                check += 1
        if check == dims:
            break
    
    return solsCount, sols[solsCount-1]