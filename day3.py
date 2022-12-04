data = open("day3.txt", "r").read()
lines = data.split("\n")

sum = 0
for line in lines:
    first = line[0:len(line)//2]
    second = line[len(line)//2:len(line)]
    for char in first:
        if char in second:
            if char.islower():
                sum += ord(char) - 96
            else:
                sum += ord(char) - 64 + 26
            break

print(sum)

sum = 0
for i in range(0, len(lines), 3):
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            if char.islower():
                sum += ord(char) - 96
            else:
                sum += ord(char) - 64 + 26
            break

print(sum)