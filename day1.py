data = open("day1.txt", "r").read()
elves = data.split("\n\n")

def calories(elf):
    return sum(map(int, elf.split("\n")))

results = list(map(calories, elves))

results.sort()

print(results[-1])
print(sum(results[-3:]))
