firstWord = input()
secondWord = input()
letterDict = {}
ans = ''
if len(firstWord) != len(secondWord):
    ans = 'NO'
else:
    for letter in firstWord:
        if letter not in letterDict:
            letterDict[letter] = 1
        else:
            letterDict[letter] += 1
    for letter in secondWord:
        if letter not in letterDict:
            ans = 'NO'
            break
        elif letterDict[letter] > 0:
            letterDict[letter] -= 1
        else:
            ans = 'NO'
            break
    if ans != 'NO': ans = 'YES'
print(ans)