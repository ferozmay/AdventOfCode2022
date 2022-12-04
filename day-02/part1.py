game = [l.strip() for l in open("input.txt")]

d = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for round in game:
    p1, p2 = round.split()

    score += d[p2]

    if (p1, p2) == ('A', 'X'):
        score += 3
    if (p1, p2) == ('A', 'Y'):
        score += 6
    if (p1, p2) == ('A', 'Z'):
        score += 0
    if (p1, p2) == ('B', 'X'):
        score += 0
    if (p1, p2) == ('B', 'Y'):
        score += 3
    if (p1, p2) == ('B', 'Z'):
        score += 6
    if (p1, p2) == ('C', 'X'):
        score += 6
    if (p1, p2) == ('C', 'Y'):
        score += 0
    if (p1, p2) == ('C', 'Z'):
        score += 3


print("Part 1:", score)
