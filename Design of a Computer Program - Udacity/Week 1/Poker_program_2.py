# Writing a Poker program

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
	return max(hand_rank(hands)