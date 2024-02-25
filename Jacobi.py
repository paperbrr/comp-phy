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

    newSols = []

    for i in range(dims):
        currentAns = ans[i]
        for j in range(dims):
            if (i!=j):
                currentAns -= matrix[i][j]*sols[solsCount-1][j]
        currentAns /= matrix[i][i]
        newSols.append(currentAns)

    sols.append(newSols)
    solsCount += 1

    check = 0

    for i in range(len(ans)):
        if abs(sols[solsCount-1][i] - sols[solsCount-2][i]) < 1e-20:
            check += 1

    if check == 3:
        break

print(sols)
print(solsCount)