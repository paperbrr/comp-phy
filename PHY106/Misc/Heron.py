def HeronRoot(sqrtOf: int, err: float, maxItCount: int) -> float :
    "finds root of given integer withint maxItCount iterations and/or below given error. 0 return value indicates no root found within iteration count"
    rootNum = sqrtOf/2
    currentItCount = 1
    while currentItCount<maxItCount:
        if abs(sqrtOf - rootNum**2) <= err:
            return rootNum
        else: 
            rootNum = 1/2*(rootNum+(sqrtOf/rootNum))
        currentItCount+=1
    return 0