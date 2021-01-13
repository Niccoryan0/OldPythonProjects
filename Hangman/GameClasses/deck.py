from .card import Card
import random
suits = ['Hearts', 'Diamonds', 'Spades', 'Clovers']
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return f'Deck: {self.deck}'

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def deal(self):
        single_card = self.deck.pop()
        return single_card
