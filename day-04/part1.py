
x = [l.strip() for l in open("input.txt")]

count = 0
i = 0
while i < len(x):
    elf1, elf2 = x[i].split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')

    elf1 = list(map(int, elf1))
    elf2 = list(map(int, elf2))

    if elf1[0] <= elf2[0] and elf1[-1] >= elf2[-1]:
        count += 1

    elif elf2[0] <= elf1[0] and elf2[-1] >= elf1[-1]:
        count += 1

    i += 1

print("Part 1:", count)
