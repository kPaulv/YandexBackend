# nickname
nickname = input()
# check if nickname is at least 8 symbols length
if len(nickname) < 8:
    print("NO")
else:
    digitCount = 0
    lowerCount = 0
    upperCount = 0
    result = "NO"
    for symbol in nickname:
        # flag if digit found
        if symbol.isdigit():
            digitCount += 1
        # if not digit check is letter UPPER or lower
        if symbol.isupper():
            upperCount += 1
        if symbol.islower():
            lowerCount += 1
        # check if we already found all required symbols
        if digitCount > 0 and upperCount > 0 and lowerCount > 0:
            result = "YES"
            break
    
    # print result
    print(result)