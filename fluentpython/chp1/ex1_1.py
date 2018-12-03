#!/usr/bin/env python3

import collections as col
import time

Card = col.namedtuple('Card', 'rank suit')

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def timing(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    # __len__ and __getitem__ allows the object to be treated like a Python
    # standard sequence
    
    # Allows use of len(<FrenchDeck instance>)
    def __len__(self):
        return len(self._cards)

    # Allows iteration using for card in deck
    # Allows slicing since we're deferring to self._cards which is a list
    # Allows deck[<index>] to retrieve a card
    def __getitem__(self, position):
        return self._cards[position]

def spades_high(card):
    # Gets the rank from the card and looks up the index
    # in the list of ranks
    rank_value = FrenchDeck.ranks.index(card.rank) 
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDeck2:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]
        self._index = dict(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __contains(self, item):
        return self._index.get(item)

@timing
def deck_test1():
    print('Deck test 1')
    deck = FrenchDeck()
    Card('Q', 'hearts') in deck

@timing
def deck_test2():
    print('Deck test 2')
    deck = FrenchDeck2()
    Card('Q', 'hearts') in deck

if __name__ == '__main__':
    main()
