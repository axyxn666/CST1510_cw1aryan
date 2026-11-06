import random

while True:
    number1 = random.randint(2, 10)
    number2 = random.randint(2, 10)

    x = int(input(f"What is the sum of {number1} and {number2}?: "))

    if x == number1 + number2:
        print("Wow, nice! You got it right.")

        y = int(input(f"What is the product of {number1} and {number2}?: "))

        if y == number1 * number2:
            print("Amazing! You got it right again.")
            break
        else:
            print(f"Sorry, you got it wrong. The correct answer is {number1 * number2}.")
            

    else:
        print(f"Sorry, you got it wrong. The correct answer is {number1 + number2}.")