from math import sin, cos, pi

def fixedfloat(accuracy):
    def decorator(func):        
        def wrapper(*args, **kwargs):
            args = list(args)

            for i in range(0, len(args)):
                if (type(args[i]) == float):
                    args[i] = round(args[i], accuracy)
            args = tuple(args)

            for key, value in kwargs.items():
                if (type(value) == float):
                    kwargs[key] = round(value, accuracy)

            result = func(*args, **kwargs)
            if (type(result) == float):
                result = round(result, accuracy)

            return result

        return wrapper
    return decorator

@fixedfloat(4)
def aver(*args, sign=1):
    return sum(args) * sign

@fixedfloat(3)
def sincos(a, b):
    return sin(a) ** 2 + cos(b) ** 2

print(sincos(pi / 2, pi / 2), sincos(pi / 4, 3 * pi / 4))
print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))