def mod(num: int) -> int :
    return -1*num if num<0 else num

def heronFunc(sqrtOf: int, err: float, maxItCount: int) -> float :
    rootNum = sqrtOf/2
    currentItCount = 1
    while currentItCount<maxItCount:
        if mod(sqrtOf - rootNum**2) <= err:
            return rootNum
        else: 
            rootNum = 1/2*(rootNum+(sqrtOf/rootNum))
        currentItCount+=1