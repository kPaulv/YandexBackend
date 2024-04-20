# input n and k
n, k = map(int, input().split())
# input array
a = list(map(int, input().split()))
initial_array = a
# sorted array
sorted_array = sorted(a)
# first distance for first number is min bc array is sorted
dist = sum(sorted_array[1:k+1]) - k * sorted_array[0]
# write distances with the number as the key
minDistancesDict = {sorted_array[0] : dist}
# numbers before current
previousNumbersAmount = 0
# numbers after current
nextNumbersAmount = k
# iterate through sorted array to find min distances for every number
for i in range(1, n):
    previousNumbersAmount += 1
    nextNumbersAmount -= 1
    # difference between current number and previous
    diff = sorted_array[i] - sorted_array[i - 1]
    # -1 тк разница между a_sorted[i] и a_sorted[i-1] осталось та же
    dist = dist - diff*nextNumbersAmount + diff*(previousNumbersAmount - 1)
    while nextNumbersAmount + i + 1 < n:
        # leftDistance - distance(simple difference between two numbers) 
        # between current number and
        # number on the left bound of sub-sequence S_i with length of k
        leftDistance = sorted_array[i] - sorted_array[i - previousNumbersAmount]
        # rightDistance - distance between current number and 
        # number next to the right border
        rightDistance = sorted_array[i + nextNumbersAmount + 1] - sorted_array[i]
        # if the left distance is greater than right distance it means that dist(i, S_i) 
        # is not minimal, so we move interval + 1
        if leftDistance > rightDistance:
            # moving interval on 1 step ahead
            nextNumbersAmount += 1
            previousNumbersAmount -= 1
            # dist now has not the minimal distance. we moved interval so 
            # we must subtract distance to the leftest number(it's now out of interval) 
            # and add the distance to the next number(we included it in interval)
            dist = dist - (leftDistance - rightDistance)
        else:
            break
        
    # current number is key, min distance is value
    minDistancesDict[sorted_array[i]] = dist
 
for item in initial_array:
    print(minDistancesDict[item], end=' ')
