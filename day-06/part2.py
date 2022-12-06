
x = [l.strip() for l in open("input.txt")]
x = list(x[0])

for i in range(len(x)):

    letters = set()

    j = 0
    while j < 14 and i+j < len(x):
        letters.add(x[i+j])
        j += 1

    if len(letters) == 14:
        print(i+14)
