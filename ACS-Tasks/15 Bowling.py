
counter = 1
while counter <= 10:
    score = int(input("Inpiut your first score"))
    if score == 10:
        print("You scored a strike")
        counter += 1
    else:
        score_2 = int(input("Inpiut your second score"))
        score_3 = score_2 + score
        if score_3 == 10:
            print("You scored a spare")
            counter += 1
        else:
            print("You scored", score_3)