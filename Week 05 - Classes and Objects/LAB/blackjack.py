import random

def deal_card():
    """Return a random card. Ace is 11, face cards are 10."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self):
        self.cards.append(deal_card())

    def score(self):
        total = sum(self.cards)

        # Ace handling: if total > 21 and there is an ace (11), count it as 1
        if total > 21 and 11 in self.cards:
            total -= 10

        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.score() == 21


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_hand = Hand()
    computer_hand = Hand()

    # Deal two cards each
    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    game_over = False

    while not game_over:
        user_score = user_hand.score()
        computer_score = computer_hand.score()

        print(f"Your cards: {user_hand.cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand.cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if choice == "y":
                user_hand.add_card()
            else:
                game_over = True

    # Dealer plays to 17
    while computer_hand.score() < 17 and computer_hand.score() != 0:
        computer_hand.add_card()

    print(f"\nYour final hand: {user_hand.cards}, final score: {user_hand.score()}")
    print(f"Computer's final hand: {computer_hand.cards}, final score: {computer_hand.score()}")
    print(compare(user_hand.score(), computer_hand.score()))


# Main loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 2)
    play_game()