f = open("input.txt", "r")

# rock a x
# paper b y
# scissor c z

# if i play x gain 1
# if i play y gain 2
# if i play z gain 3
points = 0

for line in f.readlines():
    if line[2] == "X":
        points += 1
    elif line[2] == "Y":
        points += 2
    elif line[2] == "Z":
        points += 3
    
    if line[0] == "A":
        if line[2] == "X":
            points += 3
        if line[2] == "Y":
            points += 6
    
    if line[0] == "B":
        if line[2] == "Y":
            points += 3
        if line[2] == "Z":
            points += 6
    
    if line[0] == "C":
        if line[2] == "Z":
            points += 3
        if line[2] == "X":
            points += 6
            
print(points)