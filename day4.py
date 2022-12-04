data = open("day4.txt", "r").read()
lines = data.split("\n")

count = 0
count2 = 0
for line in lines:
    [elf1, elf2] = line.split(",")
    [elf1start, elf1end] = list(map(int, elf1.split("-")))
    [elf2start, elf2end] = list(map(int, elf2.split("-")))
    if ((elf1start >= elf2start and elf1end <= elf2end) or
            (elf2start >= elf1start and elf2end <= elf1end)):
        count += 1
    if ((elf1end >= elf2start >= elf1start) or
            (elf2end >= elf1start >= elf2start)):
        count2 += 1


print(count)
print(count2)

