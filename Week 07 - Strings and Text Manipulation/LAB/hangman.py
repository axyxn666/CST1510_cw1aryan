import random

word_list = ["apple", "banana", "camel", "python", "hangman", "computer"]
chosen_word = random.choice(word_list)

# Build the display with blanks
display = ["_"] * len(chosen_word)
lives = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display))

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(" ".join(display))
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
        print(" ".join(display))

if "_" not in display:
    print("You win!")
else:
    print(f"You lose. The word was: {chosen_word}")