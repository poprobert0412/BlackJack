import random


def deal_cards():
    """Deal a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def money():
    """Return the player's available money."""
    return 2500


def adjust_ace(cards):
    """Adjust the value of an Ace card if needed."""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return cards


def calculate_result(dealer, player):
    """Calculate and print the game result."""
    dealer_sum = sum(dealer)
    player_sum = sum(player)
    print(f"Dealer cards are: {dealer}")

    if dealer_sum == player_sum or (dealer_sum <= 21 and dealer_sum >= player_sum):
        print("You lost!")
    elif player_sum > 21:
        print("You lost!")
    elif player_sum > dealer_sum or dealer_sum > 21:
        print("You win!")


def game():
    """Main function to play the Blackjack game."""
    while True:
        if input("Do you want to play Blackjack? 'y' or 'n': ").lower() != "y":
            break

        while True:
            try:
                bet = int(input(f"Place your bet, you have {money()}: "))
                if bet > money():
                    raise ValueError(f"Not enough money! The maximum bet is {money()}. Please try again.")
                break
            except ValueError as error:
                print(error)

        player_cards = [deal_cards(), deal_cards()]
        dealer_cards = [deal_cards(), deal_cards()]
        print(f"Your cards are {player_cards}")
        print(f"Dealer first card is {dealer_cards[0]}")

        while True:  # Loop for player's turn
            if input("Would you like to draw another card? 'y' or 'n': ").lower() != "y":
                break

            player_cards.append(deal_cards())
            player_cards = adjust_ace(player_cards)
            print(f"Your cards are {player_cards}")
            if sum(player_cards) > 21:
                print("You busted!")
                break

        while sum(dealer_cards) <= 16:  # Dealer's turn
            dealer_cards.append(deal_cards())

        calculate_result(dealer_cards, player_cards)


game()
