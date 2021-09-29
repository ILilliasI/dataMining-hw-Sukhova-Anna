def morecommon(a, b, n):
    aNumbersCount = 0
    bNumbersCount = 0
    
    for number in a:
        if (number % n == 0):
            aNumbersCount += 1
    for number in b:
        if (number % n == 0):
            bNumbersCount += 1
    
    return aNumbersCount > bNumbersCount

print(morecommon((1, 2, 3, 4), (9, 7), 2))
print(morecommon((10, 15, 4, 6), (10, 15, 20), 5))
