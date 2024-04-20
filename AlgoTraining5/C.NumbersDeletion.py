n = int(input())
numbers = map(int, input().split())
ans = 0

numberDict = {}
for number in numbers:
    if number in numberDict:
        numberDict[number] += 1
    else:
        numberDict[number] = 1
if len(numberDict) > 1:
    # sort numbers(keys in dict) to find pairs
    sortedNumberList = sorted(numberDict.keys())
    prevSum = numberDict[sortedNumberList[0]]
    # curSum = numberDict[sortedNumberList[0]]
    key1 = 0
    key2 = 0
    for i in range(len(sortedNumberList) - 1):
        # its a pair
        if (sortedNumberList[i + 1] - sortedNumberList[i]) <= 1:
            curSum = numberDict[sortedNumberList[i + 1]] + numberDict[sortedNumberList[i]]
            if curSum > prevSum:
                key1 = numberDict[sortedNumberList[i]]
                key2 = numberDict[sortedNumberList[i + 1]]
                prevSum = curSum
        elif numberDict[sortedNumberList[i+1]] > prevSum:
            prevSum = numberDict[sortedNumberList[i+1]]
        if prevSum == 0: # 0 keys diff in 1
            prevSum = 1
    ans = n - prevSum

print(ans)