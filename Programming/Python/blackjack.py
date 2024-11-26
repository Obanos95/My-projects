import random


def game(capital):
    cards_value = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11 
    }
    hearts = diamonds = clubs = spades = ['2','3','4','5','6','7','8','9','10','A','J','Q','K','Joker']
    deck = hearts + diamonds + clubs + spades
    first_card, second_card = random.choice(deck), random.choice(deck)
    deck.remove(first_card)
    deck.remove(second_card)
    first_card_dealer, second_card_dealer = random.choice(deck), random.choice(deck)
    deck.remove(first_card_dealer)
    deck.remove(second_card_dealer)
    player_hand = [first_card, second_card]
    dealer_hand = [first_card_dealer, second_card_dealer]
    dealer_score = 0
    player_score = 0
    if 'Joker' in dealer_hand:
        dealer_score = 21
    else:
        for i in dealer_hand:
            dealer_score += cards_value[i]
        if dealer_score > 21:
            dealer_score = 0
    player_choice = None
    player_bet = int(input('Put your bet: '))
    capital -= player_bet
    if capital < 0:
        print('You\'ll be punished for this')
    while player_choice != 'stay':
        print('Your hand:',player_hand)
        player_choice = input('Hold or hit? [stay/hit]').lower()
        if player_choice == 'stay':
            if 'Joker' in player_hand:
                player_score = 21
            else:
                for i in player_hand:
                    player_score += cards_value[i]
            if player_score < dealer_score or player_score > 21:
                print('You lost, but real gamblers never give up!')
                player_bet = 0
            else:
                print('You won!')
                player_bet *= 2
        elif player_choice == 'hit':
            card = random.choice(deck)
            deck.remove(card)
            player_hand += card
    capital += player_bet
    return capital

capital = 100
result = game(capital)
capital = 0
capital += result
print(capital)
play_again = None
while play_again != 'n':
    print('Your capital is',capital)
    play_again = input('Wanna play again? [y/n]')
    if play_again == 'y':
        result = game(capital)
        capital = 0
        capital += result