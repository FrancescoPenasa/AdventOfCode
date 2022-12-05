def calibration(x):
    """
    This might have problem, it is just funny to watch at, so I keep it
    """
    result = ord(x) - ord('a') + 1;
    if (result < 0):
        result = result + ord('A') - (ord('a') - ord('Z'))
    return result

def calibration2(x):
    """
    This is better
    """
    if (x.islower()):
        return 1 + ord(x) - ord('a')
    elif (x.isupper()):
        return 27 + ord(x) - ord('A')

print(f"a: {calibration2('a')}") # 1
print(f"z: {calibration2('z')}") # 26
print(f"A: {calibration2('A')}") # 27
print(f"Z: {calibration2('Z')}") # 52

f = open("input.txt", "r")

total = 0;
for line in f.readlines():
    d = dict({})
    
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

    for c in firstpart:
        d[c] = True
    for c in secondpart:
        if c in d:
            total += calibration2(c)
            break
        
           

print(total)