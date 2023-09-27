bowling_score = []

def bowling():
    while turns < 10:
        score = int(input("Input your first score"))
        if score == 10:
            print("You scored a strike")
            turns += 1
            strike()
        else:
            score_2 = int(input("Input your second score"))
            score_3 = score_2 + score
            if score_3 == 10:
                print("You scored a spare")
                bowling_score.append[10]
                bowling()
            else:
                print("You scored", score_3)
                turns += 1
                bowling_score.append[score_3]
                bowling()

def last_turn():
    if turns == 10:
        score = int(input("Input your first score"))
        if score == 10:
            print("You scored a strike")
            turns += 1
            strike()
        else:
            score_2 = int(input("Input your second score"))
            score_3 = score_2 + score
            if score_3 == 10:
                print("You scored a spare")
                bowling_score.append[10]
                bowling()
            else:
                print("You scored", score_3)
                turns += 1
                bowling_score.append[score_3]
                bowling()


    
def strike():
    int(input("Input your next score"))

print(bowling_score)
    

