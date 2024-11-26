import random


def rps():
    user_input = input("rock, paper, scissors. Pick one! ")

    # Computer action
    choices = ['rock', 'paper', 'scissors']
    choice = random.choice(choices)

    print(f"You chose {user_input} and computer chose {choice}")

    match user_input:
        case "rock":
            if choice == "rock":
                print("That's a draw")
            elif choice == "paper":
                print("You lose")
            elif choice == "scissors":
                print("You win")
        case "paper":
            if choice == "rock":
                print("You win")
            elif choice == "paper":
                print("That's a draw")
            elif choice == "scissors":
                print("You lose")
        case "scissors":
            if choice == "rock":
                print("You lose")
            elif choice == "paper":
                print("You win")
            elif choice == "scissors":
                print("That's a draw")

rps()

