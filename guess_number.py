import random

import time  #to add pauses

print("Hi!! Welcome to the guessing game. I'm going to pick a number between 1 and 100")
time.sleep(2)
print("Picking a number..")
time.sleep(3)
guess = int(input("What's your guess? "))
correct_number = random.randint(1,100)
guess_count = 1


while guess != correct_number:
  guess_count += 1
  if guess < correct_number:
    guess = int(input("Wrong. You need to guess higher. What's your guess? "))
  else:
    guess = int(input("Wrong. You need to guess lower. What's your guess? "))

print(f"Congrats!! The right answer was {correct_number}. And it took you {guess_count} guesses")