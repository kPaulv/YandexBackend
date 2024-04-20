n = int(input())
numbers1 = map(int, input().split())
n2 = int(input())
numbers2 = map(int, input().split())
n3 = int(input())
numbers3 = map(int, input().split())
numbersDict = {}

for number in numbers1:
    if number not in numbersDict:
        numbersDict[number] = 1

numSet = set()
for number in numbers2:
    if number not in numbersDict:
        numbersDict[number] = 1
        numSet.add(number)
    else:
        if numbersDict[number] == 1 and number not in numSet:
            numbersDict[number] += 1

numSet.clear()

for number in numbers3:
    if number in numbersDict and number not in numSet:
        numbersDict[number] += 1
        numSet.add(number)

ans = []
for key, value in numbersDict.items():
    if value >= 2:
        ans.append(key)
ans.sort()
print(*ans)
