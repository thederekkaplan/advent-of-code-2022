data = open("day2.txt", "r").read()
lines = data.split("\n")

score = 0
for line in lines:
    [a, b] = line.split(" ")
    if b == "X":
        score += 1
    if b == "Y":
        score += 2
    if b == "Z":
        score += 3
    if (a == "A" and b == "Y") or (a == "B" and b == "Z") or (a == "C" and b == "X"):
        score += 6
    if (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
        score += 3

print(score)

score = 0
for line in lines:
    [a, b] = line.split(" ")
    if b == "Y":
        score += 3
    if b == "Z":
        score += 6
    if (a == "A" and b == "Y") or (a == "B" and b == "X") or (a == "C" and b == "Z"):
        score += 1
    if (a == "A" and b == "Z") or (a == "B" and b == "Y") or (a == "C" and b == "X"):
        score += 2
    if (a == "A" and b == "X") or (a == "B" and b == "Z") or (a == "C" and b == "Y"):
        score += 3

print(score)
