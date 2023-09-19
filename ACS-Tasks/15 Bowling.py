#program to calculate the score of a bowling game
def calculate_score(rolls):
    score = 0
    counter = 1
    roll_index = 0

    while counter <= 10:
        if rolls[roll_index] == 10:  # Strike
            score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2
        counter += 1
    return score

def bowling():
    rolls = []
    counter = 1

    while counter <= 10:
        print(f"Go {counter}")
        roll1 = int(input("How many pins were knocked down in the first bowl: "))

        if roll1 == 10:  # Strike
            rolls.append(roll1)
            counter += 1
            continue

        roll2 = int(input("How many pins were knocked down in the second bowl: "))

        if roll1 + roll2 > 10:
            print("Invalid input")
            continue

        rolls.append(roll1)
        rolls.append(roll2)
        counter += 1

    score = calculate_score(rolls)
    print(f"\nYour final score is: {score}")


bowling()