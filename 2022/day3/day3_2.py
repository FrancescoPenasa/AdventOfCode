def calibration(x):
    """
    This is better
    """
    if (x.islower()):
        return 1 + ord(x) - ord('a')
    elif (x.isupper()):
        return 27 + ord(x) - ord('A')

f = open("input.txt", "r")

total = 0;
row = 0;
d = dict({})
e = dict({})
for line in f.readlines():
    if row > 2: 
        row = 0
        d = dict({})
        e = dict({})
        
    if row == 0: 
        for c in line:
            d[c] = True
    
    if row == 1: 
        for c in line:
            e[c] = True

    if row == 2: 
        for c in line:
            if c in d and c in e: 
                total += calibration(c)
                break  
    row += 1

print(total)