n, k = map(int, input().split())
numbers = map(int, input().split())
ans = 'NO'
counter = 0
numberDict = {}
for number in numbers:
    if number in numberDict:
        if counter - numberDict[number] <= k:
            ans = 'YES'
            break
        else:
            numberDict[number] = counter
    else:
        numberDict[number] = counter
    counter += 1

print(ans)