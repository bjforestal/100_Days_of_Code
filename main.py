import art
import random

print(art.logo)
print("Welcome to Braxton's Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
rand_num = random.randint(1,100)
#print(rand_num)

attempts = 10
if difficulty == 'hard':
    attempts = 5
    print(f"hard mode selected. You have {attempts} attempts. Good Luck!")
else:
    print(f"easy mode selected. You have {attempts} attempts. Good Luck!")

while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess > rand_num:
        attempts -= 1
        print(f"Too High. You have {attempts} guesses remaining")
    elif guess < rand_num:
        attempts -= 1
        print(f"Too Low. You have {attempts} guesses remaining")
    elif guess == rand_num:
        print("Great job! You guessed correctly!")
        attempts = 0