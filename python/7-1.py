# OOP Design
# Deck of Cards 

import random

# Used for 52 card deck implementation
suits = ["Diamond", "Spade", "Clover", "Heart"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    def __init__(self, value=None, suit=None):
        '''
            optional value and suit in case Card is being
            used for different card deck other than standard 52
        '''
        self.value = value
        self.suit = suit

    def set(self, value, suit):
        self.value = value
        self.suit = suit


class Deck:
    def __init__(self, num_cards=52):
        '''
            optional number of cards in case different than
            standard 52 deck
        '''
        self.num_cards = num_cards
        self.cards = [Card(value, suit) for value in values for suit in suits]
        self.discard_pile = []
        self.shuffle()

    def reset(self):
        ''' concats card and discard pile, shuffles deck '''
        self.cards += self.discard_pile
        self.discard_pile = []
        self.shuffle()

    def shuffle(self):
        ''' shuffles deck 100 times for better shuffle outcome '''
        for j in range(100):
            for i in range(len(self.cards)):
                idx = random.randint(0, len(self.cards)-1)
                self.cards[idx], self.cards[i] = self.cards[i], self.cards[idx]

    def draw(self):
        ''' returns top card from deck, shuffles discard pile if deck empty '''
        card = self.cards.pop(0)

        if len(self.cards) ==  0:
            self.reset()
            
        return card

    def discard(self, card):
        ''' adds card to discard pile '''
        self.discard_pile.append(card)
                

        
if __name__ == "__main__":
    failures = 0

    d = Deck()

    # testing correct num of suits and values after init
    print '----------------- testing init --------------------------'
    for suit in suits:
        if 13 != [c.suit for c in d.cards].count(suit): failures += 1
    for value in values:
        if 4 != [c.value for c in d.cards].count(value): failures += 1

    d.shuffle()

    # testing correct num of suits and values after shuffle
    print '----------------- testing shuffle function--------------------------'
    for suit in suits:
        if 13 != [c.suit for c in d.cards].count(suit): failures += 1
    for value in values:
        if 4 != [c.value for c in d.cards].count(value): failures += 1

    d.reset()

    # testing correct num of suits and values after reset 
    print '----------------- testing reset function--------------------------'
    for suit in suits:
        if 13 != [c.suit for c in d.cards].count(suit): failures += 1
    for value in values:
        if 4 != [c.value for c in d.cards].count(value): failures += 1

    print '----------------- testing draw and discard function--------------------------'
    for _ in range(60):
        expected = d.cards[0]
        card = d.draw()
        d.discard(card)
        if expected != card: failures += 1

   
    print 'Total failed tests:', failures
