#Number Guessing Game Objectives:
from art import logo
import random

print(logo)


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
correct_number = random.randint(1,100)
print("Welcome to the number guess game!")
print("I'm thinking of a number between 1 and 100.")
print(f"pssss the correct number is {correct_number}")


def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS




def play_game():
    
    def check_answer(guess, correct_number, turns):
        if guess > correct_number:
            print("Too High.")
            return turns - 1
        elif guess < correct_number:
            print("Too Low.")
            return turns - 1
        else:
            print("You win....")
            return

    guess = 0
    number_of_turns = difficulty()
    while guess != correct_number:
        print(f"You have {number_of_turns} attempts remaining to guess the number.")
        print(number_of_turns)
        guess = int(input("Make a guess: "))
        number_of_turns = check_answer(guess, correct_number, number_of_turns)
        
        if number_of_turns == 0:
            print("You've run out of turns, you lose.")
            return
        
play_game()
