import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissor"]


while True:
    user_guess = input("Type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_guess == "q":
        print("Quit")
        break

    if user_guess not in options:
        print("Enter valid option !!")
        continue

    random_number = random.randint(0, 2)
    # 0 rock 1 paper 2 scissor
    computer_guess = options[random_number]
    print("computer picked", computer_guess + ".")
    

    if user_guess == computer_guess:
        print("Its a tie")

    elif user_guess == "rock" and computer_guess == "scissor":
        print("You won !!")
        user_win += 1  

    elif user_guess == "paper" and computer_guess == "rock":
        print("You won!!")
        user_win += 1

    elif user_guess == "scissor" and computer_guess == "paper":
        print("You won !!")
        user_win += 1

    else:
        print("You lost this round computer wins!!")
        computer_win += 1


print("Game Over!")
print(f"You won {user_win} times")
print(f"Computer won {computer_win} times")


if user_win == computer_win:
    print("Its an tie")

elif user_win < computer_win:
    print(" In a game Computer wins!!")

else:
    print(" In a game User Wins!!")








