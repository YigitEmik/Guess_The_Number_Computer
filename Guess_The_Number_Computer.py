import random

def guess(x):
    random_number = random.randint(1, (x))
    guess = 0
    attempt = 0
    while guess != random_number:
        guess = int(input((f"Please enter your guess between 1 and {x}: ")))
        attempt += 1
        if attempt == 3 and guess != random_number:
            print(f"You do not have any more attempts,the number was {random_number} you FAILED")
            break
        elif guess > random_number:
            print("Your guess is too high from the Secret Number " + str(attempt) + "/3 attempts")
        elif guess < random_number:
            print("Your guess is too low from the Secret Number "  + str(attempt) + "/3 attempts")
        
        else:
            print("Your Gues Is CORRECT. Congrats! You have found in " + str(attempt) + "/3 attempts")

guess(10)
            