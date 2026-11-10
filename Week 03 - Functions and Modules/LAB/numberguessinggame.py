import random

secret = random.randint(1, 100)
guess = None

while guess != secret:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")