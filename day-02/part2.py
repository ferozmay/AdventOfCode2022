game = [l.strip() for l in open("input.txt")]

score = 0
for round in game:
    p1, p2 = round.split()

    match p2:
        case 'X':  # lose
            match p1:
                case 'A':
                    score += 3 + 0
                case 'B':
                    score += 1 + 0
                case 'C':
                    score += 2 + 0
        case 'Y':  # draw
            match p1:
                case 'A':
                    score += 1 + 3
                case 'B':
                    score += 2 + 3
                case 'C':
                    score += 3 + 3
        case 'Z':  # win
            match p1:
                case 'A':
                    score += 2 + 6
                case 'B':
                    score += 3 + 6
                case 'C':
                    score += 1 + 6

print("Part 2:", score)
