import random


def deal_cards():
    """Deal a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def money(money_won, current_money):
    money_won2 = current_money + money_won
    return money_won2

def bet(the_bet, current_money):
    try:
        if the_bet > current_money:
            raise ValueError(f"Not enough money! The maximum bet is {current_money}$. Please try again.")
        return the_bet
    except ValueError as error:
        print(error)

def adjust_ace(cards):
    """Adjust the value of an Ace card if needed."""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return cards

def calculate_result(dealer, player):
    dealer_sum = sum(dealer)
    player_sum = sum(player)

    if dealer_sum == player_sum or (dealer_sum <= 21 and dealer_sum >= player_sum):
        return "You lost!"
    elif player_sum > 21:
        return "You lost!"
    elif player_sum > dealer_sum or dealer_sum > 21:
        return "You win!"

def game():
    current_money = 2500
    bet1 = int(input(f"Place your bet, you have {current_money}$: "))
    bet1 = bet(bet1, current_money)

    player_cards = [deal_cards(), deal_cards()]
    dealer_cards = [deal_cards(), deal_cards()]
    print(f"Your cards are {player_cards}")
    print(f"Dealer first card is {dealer_cards[0]}")

    while True:
        if input("Would you like to draw another card? 'y' or 'n': ").lower() != "y":
            break

        player_cards.append(deal_cards())
        player_cards = adjust_ace(player_cards)
        print(f"Your cards are {player_cards}")
        if sum(player_cards) > 21:
            break

    while sum(dealer_cards) <= 16:  # Dealer's turn
        dealer_cards.append(deal_cards())

    result = calculate_result(dealer_cards, player_cards)
    print(result)

    if result == "You win!":
        money_won = bet1 * 2
        print(f"You win {money_won}")
        current_money = money(money_won, current_money)
    else:
        money_lost_amount = bet1
        print(f"You lost {bet1}! Current money: {current_money - money_lost_amount}")


game()
