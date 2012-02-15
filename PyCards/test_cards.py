# nose testing examples
import CardClass


suit_names = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades']
rank_names = [ None, '2', '3','4','5','6','7','8', '9','10', 'Jack', 'Queen', 'King', 'Ace']    

def test_full_deck():
    """
    Create a fresh deck of 52 cards
    """
    # check size of deck
    deck = CardClass.Deck()
    #deck = Deck()
    assert len(deck.cards) == 52
    
def test_pop_card():
    """
    Deal a card and recheck deck size
    """
    deck = CardClass.Deck()
    card =  deck.pop_card()
    #assert len(card) ==1
    assert len(deck.cards) == 51
    
def test_suit():
    """
    Verify suit is valid
    """
    deck = CardClass.Deck()
    card =  deck.pop_card()
    #assert val_suit(card.suit, suit_names) == True
    assert val_suit(card.suit) == True
    
def test_rank():
    """
    Verify rank is valid
    """
    deck = CardClass.Deck()
    card =  deck.pop_card()
    assert val_rank(card.rank) == True

def test_nodups():
    """
    Verify no dups in the deck
    """
    print '>>> test nodups <<<'
    #Deal complete deck - confirm no duplicates in the deck
    deck = CardClass.Deck()
    assert val_nodups(deck) == True

def val_suit (suit):
    #print "Suit: %s" %suit
    sn = suit_names[suit]
    if sn in suit_names:
        return True
    return False

def val_rank(rank):
    rn = rank_names[rank]
    if rn in rank_names:
        return True
    return False

def val_nodups(deck):
    print '>>> Val nodups <<<'
    card_dict = {}
    # check failure -  duplicate a card
    #c = deck.pop_card()
    #deck.add_card(c)
    #deck.add_card(c)
    while len(deck.cards) > 0:
        c =  deck.pop_card()
        #kv = suit_names[c.suit] + rank_names[c.rank]
        kv = str(c)
        print 'checking card: %s' %kv
        # check for duplicate - key already in dictionary
        if card_dict.has_key(kv):
            return False
        # add card to dict
        card_dict[kv] = kv
        
    print card_dict
    return True
   