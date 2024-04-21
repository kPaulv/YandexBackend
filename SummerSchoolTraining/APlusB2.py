def sum(a, b):
    len_a = len(a)
    len_b = len(b)
    limit = len_a if len_a > len_b else len_b
    diff = len_a - len_b if len_a > len_b else len_b - len_a
    
    for i in range(limit - 1, diff - 1, -1):
        b[i] += a[i]
        b[i - 1] += (b[i] // 10)
        b[i] %= 10
    
    return ''.join(map(str, b))


file = open('input.txt', 'r')
a, b = file.readline().split()
file.close()

# file = open('./data/input.txt', 'r')
a, b = file.read().split()

writer = open('output.txt', 'w')

if len(a) < 4 and len(b) < 4:
    writer.write(int(a) + int(b))
else:
    a, b = list(map(int, list(a))), list(map(int, list(b)))
    writer.write(sum(a, b))

writer.close()
