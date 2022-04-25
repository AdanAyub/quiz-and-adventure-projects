def end():
    print("Welcome to my celebrity quiz!")

    playing = input("Do you want to play? ")

    if playing.lower() != "yes":
        quit()

    print("Okay! Let's play :)")
    score = 0

    answer = input("Who plays thor in marvel movies? ")
    if answer.lower() == "Chris Hemsworth":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("who plays batman in the dark knight movies? ")
    if answer.lower() == "Christian Bale":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("Who made the song rap god? ")
    if answer.lower() == "Eminem":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("what is the name of the person who played Jack Sparrow? ")
    if answer.lower() == "Johnny Depp":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("who slapped Chris Rock at the oscars? ")
    if answer.lower() == "Will Smith":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the name of the girl from beauty and the beast? ")
    if answer.lower() == "Belle":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is Robert Downey Jr.'s most famous role? ")
    if answer.lower() == "Iron Man":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("Who directed the original spidermen movies? ")
    if answer.lower() == "Sam Raimi":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("Who is Wonder Woman played by in justice league ")
    if answer.lower() == "Gal Gadot":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does who is the current Prime Minister of Canada? ")
    if answer.lower() == "Justin Trudeau":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 10) * 100) + "%.")

    play_again = input("do you want to play again")

    if play_again == "yes":
        end()
    else:
        print("bye")

end()