import random #module used to bring random functions like random.choice(), etc,. into the program for use

#scoreboard
user_score = 0
computer_score = 0

while True:
    pactions = ["rock", "paper", "scissors"]
    uctions = input("\nEnter a choice (rock, paper, scissors) or 'quit' to end: ").lower()

    if uctions == "quit":
        print("\nFinal Score:")
        print(f" You: {user_score} | Computer: {computer_score}")
        break

    if uctions not in pactions:
        print("Invalid choice. Please select rock, paper, or scissors.")
        continue

    computer_action = random.choice(pactions)
    print(f"\nYou chose {uctions}, computer chose {computer_action}.\n")

    if uctions == computer_action:
        print(f"Both players selected {uctions}. It's a tie!")
        print(" X | O ")
    elif uctions == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
            print("   | O ")
    elif uctions == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
            print("   | O ")
    elif uctions == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1
            print("   | O ")

    #score
    print(f"\nScoreboard:")
    print(f" You: {user_score} | Computer: {computer_score}")
