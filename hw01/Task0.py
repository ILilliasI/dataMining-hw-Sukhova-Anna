from math import log10

def reverseNumber(number):
    reversedNumber = 0
    
    while (number != 0):
        reversedNumber *= 10
        reversedNumber += number % 10
        number //= 10
    return reversedNumber

number = int(input())

if (number >= 0 and reverseNumber(number) == number):
    print("palindrome")
else:
    print("not palindrome")
