name = input("Enter your name : ")
print("Welcome", name, "to this adventure!!")

answer = input("Your dirt road come to the end and you can go left or right which way you would like to go ? ").lower()

if answer == "left":
    answer = input("You come to a river , ypu can walk around to swim accross ? Type walk or swim around and swin to swim accross: ")

    if answer == "swim":
        print("You swim accross and were eaten by an alligator")

    elif answer == "walk":
        print("You walked for many miles , ran out of the water and you lost the game.")

    else:
        print("Not a valid !!. You lost")

elif answer == "right":
    answer = input("You come to a bridge , it looks wobbly , do you want to cross it or head back(cross/ back) ")

    if answer == "cross":
        print("You can cross accross and decide to drive in road.")

    elif answer == "back":
        answer = input("you cross the bridge and meet the stranger you will talk to them? .")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold , you win!!")
        elif answer == "no":
            print("You randomly ingnore the stranger and you lost. ")
        else:
            print("in valid option!!")
    else:
        print("you lost!!")

else:
    print("not an valid option!! you lost")


print("Thank you for Trying 😊😊😊")