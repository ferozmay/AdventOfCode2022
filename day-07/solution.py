from collections import defaultdict

x = [l.strip() for l in open("input.txt")]

dirs = defaultdict(int)
current_path = []

for cmd in x:
    cmd = cmd.strip().split()

    if cmd[1] == 'cd':
        if cmd[2] == '..':
            current_path.pop()
        else:
            current_path.append(cmd[2])

    elif cmd[1] == 'ls' or cmd[0] == 'dir':
        continue

    else:
        for i in range(len(current_path)):
            dirs[tuple(current_path[:i + 1])] += int(cmd[0])


sum = 0
for size in dirs.values():
    if size <= 100000:
        sum += size

print("Part 1:", sum)


unused = 70000000 - max(dirs.values())

remaining = 30000000 - unused

l = []
for size in dirs.values():
    if size > remaining:
        l.append(size)

print("Part 2:", min(l))
