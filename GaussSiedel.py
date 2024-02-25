matrix = [[10, -1, 2, 0],
          [-1, 11, -1, 3],
          [2, -1, 10, -1],
          [0, 3, -1, 8]]

ans = [6, 25, -11, 15]

dims = 4
xIni = 10
yIni = 10
zIni = 10
qIni = 10

sols = [[xIni, yIni, zIni, qIni]]
solsCount = 1

while solsCount < 200:

    currentSols = []

    for i in range(dims):
        currentAns = ans[i]
        for j in range(dims):
            if (i!=j):
                currentAns -= matrix[i][j]*sols[solsCount-1][j]
        currentAns /= matrix[i][i]
        currentSols.append(currentAns)

    sols.append(currentSols)
            
    solsCount += 1

print(sols[solsCount-1])