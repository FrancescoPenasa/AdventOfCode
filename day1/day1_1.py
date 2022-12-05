f = open("input.txt", "r")

total = 0;
max = 0;
for line in f.readlines():
    if line == "\n":
        if total > max: 
            max = total
        total = 0
    else: 
        total = total + int(line)
print(f"MAX: {max} test")
