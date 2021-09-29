from functools import reduce

def maxFunctionSum(S, *args):
    if (len(args) < 1):
        return
    maxSum = reduce(lambda x, y: x + y, map(args[0], S))
    
    for f in args:
        res = reduce(lambda x, y: x + y, map(f, S))
        if (res >= maxSum):
            maxSum = res
    return maxSum
        
print(maxFunctionSum([1, 2, 3], lambda x: x, lambda x: x ** 2, lambda x: 2 * x))
