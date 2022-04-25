name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are riding a bicycle on your way to school, you see a shoetcut on the left. You can take the long way that you are used to or take the new shortcut pick left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a spooky forest and there is a sign that says crocodiles, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You're almost out of time there is a stange man who offers you a ride, he looks high, do you want to get a ride or head back (ride/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "ride":
        answer = input(
            "You get in the car and the strangers you a weird substance. Do you want to take it (yes/no)? ")

        if answer == "yes":
            print("You take the substance and ingest it, it gives you super powers and you fly to school. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and  routhlessly stab you. you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)