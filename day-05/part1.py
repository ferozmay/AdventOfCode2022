
x = [l.strip('\n') for l in open("input.txt")]

stacks = [[] for i in range(9)]

for i in range(8):
    line = x[i]
    k = 0
    for j in range(1, len(x[0]), 4):
        if (line[j] != " "):
            stacks[k].append(line[j])
        k += 1

print(stacks)
