from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    cards_sum = sum(card_list)
    if cards_sum == 21 and len(card_list) == 2:
        return 0
    if cards_sum > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "User Loses, computer has Blackjack!"
    elif user_score == 0:
        return "Computer Loses, user has Blackjack!"
    elif user_score > 21:
        return "You Lose! Your score is over 21"
    elif computer_score > 21:
        return "You Win! Computer's score is over 21"
    elif computer_score > user_score:
        return "Computer Wins!"
    else:
        return "You Win!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            third_card = input("Would you like another card? Type yes/no: ").lower()
            if third_card == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()







