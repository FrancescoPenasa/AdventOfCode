f = open("input.txt", "r")
total = 0
for line in f.readlines():
    elf1, elf2 = line.split(',')
    
    srt1, stp1 = elf1.split('-')
    srt2, stp2 = elf2.split('-')

    srt1 = int(srt1)
    srt2 = int(srt2)
    stp1 = int(stp1)
    stp2 = int(stp2)


    if srt1 >= srt2 and stp1 <= stp2:
        # print (line)
        total += 1
    elif  srt2 >= srt1 and stp2 <= stp1:
        # print (line)
        total += 1

print(total)
