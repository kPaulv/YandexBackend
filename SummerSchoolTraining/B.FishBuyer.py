n, k = map(int, input().split())
costs = list(map(int, input().split()))

minCosts = [10**6 + 1] * (n + 1)

purchases = []

minCosts[0] = 0
for i in range(1, n + 1):
    limit = k + 1 if k <= i else i + 1
    for j in range(1, limit):# max(i - k, 0), i + 1, 1): # range(1, min(i, k) + 1):
        minCosts[i] = min(minCosts[i], minCosts[i - 1] + costs[i - j])

fishes = []
day = n
while day > 0:
    for j in range(1, min(day, k) + 1):
        if minCosts[day] == minCosts[day - 1] + costs[day - j]:
            fishes.append(j)
            day -= j
            break
        else:
            fishes.append(0)
        
print(minCosts[n])
print(*fishes[::-1])        
