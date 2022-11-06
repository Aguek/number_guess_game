#Number Guessing Game Objectives:
from art import logo
import random

print(logo)



correct_number = random.randint(1,100)
print("Welcome to the number guess game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"pssss the correct number is {correct_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
number_of_attempts = 0
if level == "easy":
    number_of_attempts = 10
else:
    number_of_attempts = 5

print(f"You have {number_of_attempts} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))

while correct_number != guess and number_of_attempts != 0:
    
    if guess > correct_number:
        print("Too High.")
        print("Guess again")
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        number_of_attempts -= 1
    elif guess < correct_number:
        print("Too Low.")
        print("Guess again")
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        number_of_attempts -= 1
    
if guess == correct_number:
    print(f"You win with {number_of_attempts} attempts left")
else:
    print("You ran out of lives.")