
x = [l.strip() for l in open("input.txt")]

count = 0
i = 0
while i < len(x):
    elf1, elf2 = x[i].split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')

    elf1 = list(map(int, elf1))
    elf2 = list(map(int, elf2))

    # couting all overlapping ranges
    if not (elf1[-1] < elf2[0] or elf2[-1] < elf1[0]):
        count += 1

    i += 1

print("Part 2:", count)
