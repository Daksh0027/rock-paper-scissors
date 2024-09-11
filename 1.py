import random

# Initialize scoreboard
user_score = 0
computer_score = 0

while True:
    possible_actions = ["rock", "paper", "scissors"]
    user_action = input("\nEnter a choice (rock, paper, scissors) or 'quit' to end: ").lower()

    if user_action == "quit":
        print("\nFinal Score:")
        print(f" You: {user_score} | Computer: {computer_score}")
        break

    if user_action not in possible_actions:
        print("Invalid choice. Please select rock, paper, or scissors.")
        continue

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        print(" X | O ")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
            print("   | O ")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
            print("   | O ")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
            print(" X |   ")
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1
            print("   | O ")

    # Display current score
    print(f"\nScoreboard:")
    print(f" You: {user_score} | Computer: {computer_score}")
