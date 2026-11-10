alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar(direction, text, shift):
    result = ""
    if direction == "decode":
        shift = -shift

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += char   # leave spaces, numbers, punctuation alone

    print(f"The {direction}d text is: {result}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    again = input("Type 'yes' to go again, or 'no' to stop:\n").lower()
    if again == "no":
        should_continue = False
        print("Goodbye!")