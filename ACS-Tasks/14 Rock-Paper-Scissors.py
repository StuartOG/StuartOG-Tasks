import random, os

Number = random.randint(0,3)

Player_Choice = input("Choose rock, paper or scissors: ")

if Number == 1:
    print("The computer chose rock")
elif Number == 2:
    print("The computer chose scissors")
elif Number == 3:
    print("The computer chose paper")
#end if

if Player_Choice == "rock" and Number == 1:
    print("It was a draw")
elif Player_Choice == "rock" and Number == 2:
    print("You won!")
elif Player_Choice == "rock" and Number == 3:
    print("You lost")

if Player_Choice == "paper" and Number == 1:
    print("You won!")
elif Player_Choice == "paper" and Number == 2:
    print("You lost")
elif Player_Choice == "paper" and Number == 3:
    print("It was a draw")

if Player_Choice == "scissors" and Number == 1:
    print("You lost!")
elif Player_Choice == "scissors" and Number == 2:
    print("It was a draw")
elif Player_Choice == "scissors" and Number == 3:
    print("You won!")
    




