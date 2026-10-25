import art;
import random;
import os;
cards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"];

def card_value(card):
    if card in ("Jack", "Queen", "King"):
        return 10
    if card == "Ace":
        return 11
    return card

def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    aces = hand.count("Ace")
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


def client_turn(client_hand,computer_hand):
    print(f"Your cards: {client_hand}, current score: {calculate_score(client_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")
    add_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if add_card == 'y':
        client_hand.append(random.choice(cards));
        client_turn(client_hand, computer_hand);
    else:
        client_score = calculate_score(client_hand)
        if client_score > 21:
            print(f"You lose! Your score is {client_score}")
            return

        computer_score = calculate_score(computer_hand)
        while computer_score < 17:
            computer_hand.append(random.choice(cards))
            computer_score = calculate_score(computer_hand)

        print(f"Computer's hand: {computer_hand}, score: {computer_score}")
        if computer_score > 21 or client_score > computer_score:
            print(f"You win! Computer: {computer_score}, You: {client_score}")
        elif client_score == computer_score:
            print(f"Draw! Both have {client_score}")
        else:
            print(f"You lose! Computer: {computer_score}, You: {client_score}")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo);
    client_hand = [random.choice(cards),random.choice(cards)]
    computer_hand = [random.choice(cards)];
    client_turn(client_hand, computer_hand)
    