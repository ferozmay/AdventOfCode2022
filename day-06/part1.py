
x = [l.strip() for l in open("input.txt")]
x = list(x[0])

for i in range(len(x)):

    letters = set([x[i], x[i+1], x[i+2], x[i+3]])

    if len(letters) == 4:
        print(i+4)
        break
