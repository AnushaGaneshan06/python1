print("Welcome to my computer quiz!!!")

count = 0

playing = input("Do you want to play this game (YES / NO): ").lower()

if playing != "yes":
    quit()
    print(" Quit ....")

elif playing == "yes":
    print(" Quizs Starts..")

answer = input("Which function is used to display output in Python?  ").lower()

if answer == "print()":
    print("Correct answer!!✌️")
    count += 1
else:
    print("Incorrect answer!!😒")


answer = input("Which keyword is used to define a function in Python? ").lower()

if answer == "def":
    print("Correct answer ✌️")
    count += 1
else:
    print("Incorrect Answer😒")


answer = input("What function is used to get the total number of items in a list? ").lower()

if answer == "len":
    print("Correct answer ✌️")
    count += 1
else:
    print("Incorrect Answer😒")


answer = input("What function is used to get user input in Python? ").lower()

if answer == "input":
    print("Correct answer ✌️")
    count += 1
else:
    print("Incorrect Answer😒")



answer = input("What keyword is used to import a library in Python? ").lower()

if answer == "import":
     print("Correct answer ✌️")
     count += 1
else:
    print("Incorrect Answer😒")


print("Quiz ends...👋")


if count == 0 :
    print("Oh no you failed it .. ")
    print("Better luck next time !! ")

elif 0 < count < 4:
    print(f"Scored you got in Quiz : {(count)} , Try again get full score ..")

elif count == 5:
    print("You got full score in the quizs🥳")

else:
    pass
    
    
