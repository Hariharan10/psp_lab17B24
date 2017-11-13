def selectsort(L): 
    for slot in range(len(L)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, slot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location

        temp             = L[slot]
        L[slot]          = L[positionOfMax]
        L[positionOfMax] = temp
    return L

L = [1, 31, 421, 2123, 1, 31, 421]
print(selectsort(L))
