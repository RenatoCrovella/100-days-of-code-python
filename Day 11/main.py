from random import choice

deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
game_over = False

def sum_cards(hand):
    current_sum = 0
    for card in hand:
        if card == 11 and current_sum >= 20:
            card = 1
        current_sum += card
    return current_sum

wanna_play = input("Do you want to play blackjack? Type 'y' or 'n': ")

if wanna_play.lower() == 'y' or wanna_play.lower() == 'yes':
    print("Welcome to Blackjack!")
else:
    print("Thank you and see you next time!")

# Function to draw cards:
def draw_cards(amount, hand):
    for number in range(amount):
        new_card = choice(deck_cards)
        hand.append(new_card)
draw_cards(2, player_hand)
draw_cards(2, computer_hand)

# Reveals the player's hand and the dealer's first card.
print(f"Your hand is now: {player_hand}")
print(f"Dealer's first card is: {computer_hand[0]}")

# Check if there's a winner:
def compare_results(p_hand, c_hand):
    print(f"Your total is {sum_cards(p_hand)} and dealer's total is {sum_cards(c_hand)}")
    if sum_cards(p_hand) == sum_cards(c_hand):
        print("You won!")
    elif sum_cards(p_hand) > 21:
        print("You lost!")
    elif sum_cards(c_hand) > 21:
        print("You won!")
    elif sum_cards(c_hand) < sum_cards(p_hand):
        print("You won!")
    else:
        print("Draw!")

while not game_over:
    player_choice = input("Would you like to draw a new card?")

    if player_choice.lower() == 'y' or player_choice.lower() == 'yes':
        draw_cards(1, player_hand)
        print(f"Your hand is now: {player_hand}")
        if sum_cards(player_hand) > 21:
            compare_results(player_hand, computer_hand)
            game_over = True

    else:
        if sum_cards(computer_hand) <= 11:
            print("The dealer bought a new card.")
            draw_cards(1, computer_hand)
        compare_results(player_hand, computer_hand)
        game_over = True
