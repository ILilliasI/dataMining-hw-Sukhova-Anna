def replaceSubstring(string):
    notIndex = string.find("not")
    badIndex = string[notIndex + 3:].find("bad") + notIndex + 3
    
    if (notIndex != -1 and notIndex < badIndex):
        return string[:notIndex] + "good" + string[badIndex + 3:]
    else:
        return string

def sumOfDigits(string):
    res = 0
    currentNumber = ""
    
    for ch in string:
        if ch.isdigit():
            currentNumber += ch
        elif (currentNumber != ""):
            res += int(currentNumber)
            currentNumber = ""
    if (currentNumber != ""):
        res += int(currentNumber)
    return res

def areStringsEqual(firstString, secondString):
    length = len(firstString)
    if (length != len(secondString)):
        return False
    if (firstString == secondString):
        return True
    
    for _ in range(0, length):
        firstString = firstString[1:] + firstString[0]
        if (firstString == secondString):
            return True
    return False

def reverseWordsInString(string):
    wordsArray = string.split()
    res = ""
    
    for i in range(len(wordsArray) - 1, -1, -1):
        res += wordsArray[i]
        if (i != 0):
            res += " "
    return res

print(replaceSubstring("not not bad"))
print(sumOfDigits("aa2 22 s2d30"))
print(areStringsEqual("fooBar", "oBarfo"))
print(reverseWordsInString("The dinner was not bad"))
