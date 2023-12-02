# f = open("input.txt", "r")

# # PART 1 
# total = 0
# for line in f.readlines():
#     first = True
#     last = True
#     first_n = ""
#     last_n = ""
#     for i in range(len(line)):
#         if first and line[i].isnumeric():
#             first_n = line[i]
#             first = False
#         if last and line[-i-1].isnumeric():
#             last_n = line[-i-1]
#             last = False
#     total += int(first_n + last_n)
#     print(f"{line} - {int(first_n + last_n)} = {first_n} {last_n}")
# print(f"part1 = {total}")


# PART 2
f = open("input.txt", "r")
numbers = {"one": "one1one", "two" : "two2two", "three" : "three3three", "four": "four4four", "five": "five5five", "six" : "six6six", "seven" : "seven7seven", "eight" : "eight8eight", "nine": "nine9nine"}

total = 0
for line in f.readlines():
    print(f"before: {line}")
    line = line.lower()
    for key in numbers.keys():
        if key in line:
            line = line.replace(key, numbers[key])
    print(f"after: {line}")

    first = True
    last = True
    first_n = ""
    last_n = ""
    for i in range(len(line)):
        if first and line[i].isnumeric():
            first_n = line[i]
            first = False
        if last and line[-i-1].isnumeric():
            last_n = line[-i-1]
            last = False

    total += int(first_n + last_n)
    print(f"{line} - {int(first_n + last_n)} = {first_n} {last_n}")
print(f"part2 = {total}")