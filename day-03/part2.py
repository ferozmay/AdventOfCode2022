
x = [l.strip() for l in open("input.txt")]

p = 0
i = 0
while i < len(x):

    for item in x[i]:
        if item in x[i+1] and item in x[i+2]:

            if item.islower():
                p += ord(item) - 96
            else:
                p += ord(item) - 38

            break
    i += 3


print("Part 2:", p)
