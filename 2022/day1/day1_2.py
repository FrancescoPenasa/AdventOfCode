f = open("input.txt", "r")

elf = 0
max = [0, 0, 0]

for line in f.readlines():
    if line == "\n": # elf finished
        if elf > max[0]:
            max[2] = max[1]
            max[1] = max[0]
            max[0] = elf
        elif elf > max[1]:
            max[2] = max[1]
            max[1] = elf
        elif elf > max[2]:
            max[2] = elf
        elf = 0
    else: # new food in elf
        elf = elf + int(line)


for i in range(0, len(max)):
    print(f"{i} elf:{max[i]}")

print(f"Sum: {max[0] + max[1] + max[2]}")