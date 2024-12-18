import random # module 

print("NUMBER GUESSING GAME !!")

top_of_range = input("Enter to guess the number : " )
# r = random.randrange(-1, 10) # not include 10

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Enter greater than 0 next time")
        quit()


random_number =random.randint(0, top_of_range) # include 11
guess_count = 0


while True:

    number_guess = input("Make a guess : ")
    if number_guess.isdigit():
        number_guess = int(number_guess)
    else:
        print("Enter the number next time !!")
        continue

    if number_guess == random_number:
        print("Correct")
        guess_count += 1
        break
    elif number_guess < random_number:
        print("Too low !!")
        guess_count += 1
    elif number_guess > random_number:
        print("Too high!!")
        guess_count += 1
    else:
        print("you got it wrong!!")

print("The number guesses took to find the correct number is : ", guess_count)










    


