# reservoir amount
n = int(input())

# all reservoirs volumes
volumes = list(map(int, input().split()))

# minimal operations amount
operations = 0

# checking if the sequence is descending
previous_volume = 0
for volume in volumes:
    if volume < previous_volume:
        operations = -1
        break; # if the next volume is less than previous then it's impossible to fill reservoirs equal
    previous_volume = volume

# if the sequence is ascending or consists of equal volumes(not descending)
if operations >= 0:
    operations = volumes[len(volumes) - 1] - volumes[0]

print(operations)