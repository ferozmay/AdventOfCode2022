
x = [l.strip() for l in open("input.txt")]

p = 0
for s in x:
    c1 = s[:len(s)//2]
    c2 = s[len(s)//2:]

    for item in c1:
        if item in c2:
            if item.islower():
                p += ord(item) - 96
            else:
                p += ord(item) - 38
            break

print("Part 1:", p)
