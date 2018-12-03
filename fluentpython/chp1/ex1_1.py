#!/usr/bin/env python3

import collections as col
import time

Card = col.namedtuple('Card', 'rank suit')

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

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

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
