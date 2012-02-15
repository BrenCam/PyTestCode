#!/usr/bin/python
# cards.py

suits = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [ '2', '3','4','5','6','7','8', '9','10', 'Jack', 'Queen', 'King', 'Ace']

rows = 'ABCD'
digits = '1234'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    # how todo this in ruby?
    return [a+ ' of ' + b for a in A for b in B]


if __name__ == '__main__':

    carddeck = cross(ranks, suits)
    
#    for card in carddeck:
#      print card 
    # create a generator object to deliver/iterate over list
    # ??ruby equivalent for this?? - ?require Generator library?
    cards = (card for card in carddeck)
    for c in cards:
        print c
            
    #c = b.next()
    #print carddeck
    print len(c)


