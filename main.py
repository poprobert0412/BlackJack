import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def money():
    return 2500



def game():
    while True:
        if input("Do you want to play BlackJack? 'y' or 'n': ").lower() == "y":
            while True:
                try:
                    bet = int(input(f"Place your bet, you have {money()}: "))
                    if money() < bet:
                        raise ValueError(f"Not enough money! The maximum bet is {money()}. Please try again.")
                    break
                except ValueError as error:
                    print(error)

            player_cards = [deal_cards(), deal_cards()]
            dealer_cards = [deal_cards(), deal_cards()]
            print(f"Your cards are {player_cards}")
            print(f"Dealer first card is {dealer_cards[0]}")
            hit_again = ""




game()