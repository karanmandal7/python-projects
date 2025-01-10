name = input("Hey type your name: ")
print("Hello " + name + " welcome to the game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play!")

    direction = input("Do ypu want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, game over, try again.")
    elif direction == "right":
        choice = input("Okay you now see a bridge, do you want to swim under it or cross it? (swim/bridge) ")

        if choice == "swim":
            print("you got killed by an sea monster, you die, the end!")
        else:
            print("you found the prize and won!")
    else:
        print("Sorry not a valid response, you die!")

else:
    print("We are not playing....")