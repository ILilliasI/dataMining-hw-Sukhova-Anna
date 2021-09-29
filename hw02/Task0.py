firstLanguage = set()
secondLanguage = set()
wordsCount = 0

word = input()

while (word != ""):
    for letter in word:
        if (wordsCount % 2 == 0):
            firstLanguage.add(letter)
        else:
            secondLanguage.add(letter)
    word = input()      
    wordsCount += 1

if (len(firstLanguage) > len(secondLanguage)):
    print("Mumbo")
else:
    print("Jumbo")
