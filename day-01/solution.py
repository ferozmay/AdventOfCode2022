
elfs = []

data = [l.strip() for l in open("input.txt")]

total = 0
for calorie in data:
    if calorie == "":
        elfs.append(total)
        total = 0
    else:
        total += int(calorie)

print("Part 1:", max(elfs))

elfs.sort()
top3 = elfs[-3:]

print("Part 2:", sum(top3))
