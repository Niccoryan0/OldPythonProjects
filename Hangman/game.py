import random
# suits = ['Hearts', 'Diamonds', 'Spades', 'Clovers']
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
game_on = True

from GameClasses.card import Card
from GameClasses.deck import Deck
from GameClasses.hand import Hand
from GameClasses.chips import Chips


def take_bet(chips):
    while True:
        try:
            print(f'You have: {chips.total} chips')
            chips.bet = int(input('How much would you like to bet? '))
        except ValueError:
            print("Invalid input, please enter an integer")
            continue
        else:
            if chips.bet > chips.total:
                print(f'Not enough chips! Your total: {chips.total}')
                continue
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    hitorstand = input('Hit or stand? ').lower()
    if hitorstand.startswith('h'):
        hit(deck,hand)
    elif hitorstand.startswith('s'):
        playing = False
    else:
        print('Invalid input, please try again')


def show_some(player, dealer):
    print("\nDealer's hand:")
    print('<card face down>')
    print(*dealer.cards[1:], sep='\n')
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Hand total: ", player.value)


def show_all(player, dealer):
    print("\nDealer's hand:", *dealer.cards, sep='\n')
    print("Dealer's hand total: ", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Hand total: ", player.value)


def player_busts(player, chips):
    if p_hand.value > 21:
        print('\nYou busted!')
        chips.lose_bet()
        return True


def player_wins(player,dealer,chips):
    if 21 >= p_hand.value > d_hand.value:
        print('\nYou win!')
        chips.win_bet()

def dealer_busts(dealer, chips):
    if d_hand.value > 21:
        print('\nDealer busted!')
        chips.win_bet()
        return True


def dealer_wins(player, dealer, chips):
    if 21 >= d_hand.value > p_hand.value:
        print('\nDealer wins!')
        chips.lose_bet()


def tie():
    if p_hand == d_hand:
        print("It's a tie!")

def replay():
    while True:
        try:
            restart = input('Play again? y/n: ').lower().startswith('y')
        except ValueError:
            print('Invalid input, please enter y for yes or n for no')
            continue
        else:
            return restart


chips = Chips()  # Automatically set to 100 but can be changed, kept outside so it doesnt refresh to 100 every replay
deck = Deck()  # Kept outside so that the deck doesnt restock every replay
deck.shuffle()
while True:
    print('Welcome to BlackJack!')
    if len(deck) == 0:
        deck = Deck()  # Refreshes deck if it runs out
        deck.shuffle()
    p_hand = Hand()
    p_hand.add_card(deck.deal())
    p_hand.add_card(deck.deal())

    d_hand = Hand()
    d_hand.add_card(deck.deal())
    d_hand.add_card(deck.deal())

    chips = Chips(chips.total)
    take_bet(chips)

    show_some(p_hand, d_hand)
    playing = True

    while playing:
        hit_or_stand(deck, p_hand)
        show_some(p_hand, d_hand)

        if player_busts(p_hand, chips):
            break

        if d_hand.value <= 16:
            hit(deck, d_hand)
            if dealer_busts(d_hand, chips):
                break
    show_all(p_hand, d_hand)
    dealer_wins(p_hand, d_hand, chips)
    player_wins(p_hand, d_hand, chips)
    tie()
    print(f'\nYou have: {chips.total} chips')
    if chips.total == 0:
        print('Out of chips')
        break
    elif not replay():
        break
    print('\n\n')
print('Thanks for playing!')
