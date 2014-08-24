# Poker program
# Hand ranks

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

def card_rank(hand):
    "Return a list of ranks of the cards"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks

def straight(ranks):
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5


def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return n
    return None


def two_pairs(ranks):
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return (pair, low_pair)
    else:
        return None


def hand_rank(hand):
    "Return a value indicating the rank of the hand"
    ranks = card_rank(hand)
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
    elif two_pairs(ranks):
        return (2, two_pairs(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def poker(hands):
    return max(hands, key=hand_rank)


def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 4, 1)
    assert hand_rank(fh) == (6, 3, 2)
    assert card_rank(sf) == [10, 9, 8, 7, 6]
    return "Test pass"

print test()

