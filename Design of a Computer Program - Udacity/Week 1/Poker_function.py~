
'''
Hand rank
0- High Card
1- One Pair
2- Two Pair
3- Three of a Kind
4- Straight (5 consecutively ranked cards, suite don't matter)
5- Flush (All five cards of same suite, ranks don't matter)
6- Full House
7- Four of a Kind
8- Straight Flush
'''

def poker(hands):
    'returns the best hand'
    hand_rank(hands)
    return max(hands, key = hand_rank)



def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, kind(2, ranks)))
    else:
        return (0, ranks)

def card_ranks(hands):
    ranks = ['--23456789QKA'.index(r) for r,s in hands] # Really cool trick. Peter Norvig is a Genius
    ranks.sort(reverse = True)
    if ranks == [14, 5, 4, 3, 2]:  # fix for the ace-low situation
        return [5, 4, 3, 2, 1]
    else:
        return ranks

print card_ranks("6C 7C 8C TC QC".split())



def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

print test()
