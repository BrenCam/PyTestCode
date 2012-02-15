import random
#import PIL

#import Image

#import unittest

#t = unittest.

class Card:
    """ playing card class """
    
    suit_names = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [ None, '2', '3','4','5','6','7','8', '9','10', 'Jack', 'Queen', 'King', 'Ace']    
    
    def __init__ (self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
        
        
    def __str__(self):
        return "%s of %s" %( Card.rank_names[self.rank], Card.suit_names[self.suit]) 
    
    def __cmp__(self, other):
        if self.suit > other.suit:
            return 1
        
        if self.suit < other.suit:
            return -1
        
        if self.rank > other.rank:
            return 1
        
        if self.rank < other.rank:
            return -1

        return 0
    
class Deck:
    
    def __init__ (self):
        self.cards = []
        for suit in range(4): #range[4] error not detected in Wing IDE - ??why??
                              # error is detected if run in debug mode
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()
        
    def __str__ (self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
        
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def add_card(self, card):
        self.cards.append(card)
    
    
if __name__ == '__main__':
    tc = Card (2,11)
    print tc
    
    
    deck = Deck()
    #for i in range[3]:
        #print "test"
    print deck
    i = 0
    print ">>>> Deck contains %s cards" % len(deck.cards)
    
    print ">>>> Deal a hand of cards <<<<<"
    for i in range(5): 
        c = deck.pop_card()
        print ">>>>";
        print c
        
    #print length(deck)
    