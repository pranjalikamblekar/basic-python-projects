import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Type Rock/Paper/Scissors to play or Q to quit\n").lower()
    if user_choice == "q":
        break

    if user_choice not in options:
        continue

    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print(f"Computer picked {computer_choice}")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("Computer won!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times")
print("Goodbye!")

