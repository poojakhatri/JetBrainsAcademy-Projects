incorrect = 0
correct = 0
count = 0
total = 0
scores = input()
for score in scores.split():
    if score == 'I':
        count += 1
        incorrect += 1
    else:
        correct += 1
        if count < 3:
            total += 1

if incorrect >= 3:
    print("Game over")
    print(total)
else:
    print("You won")
    print(correct)
