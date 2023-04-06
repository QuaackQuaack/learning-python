import collections

Card = collections.namedtuple('Card',['rank','suit'])

#to understand how special method name are written 
# to understand the abtraction of python 
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamond clubs hearts'.split() # this is to convert str suits to list suits 
    suit_values = dict(spades=3, hearts = 2, diamonds = 1, clubs = 0)
#dict assign way 
    def __init__(self):
        self._cards= [Card(rank,suit) for suit in self.suits  # suit it to iterate from spades to diamond
                      for rank in self.ranks] # rank is to iterate from 2 to 11

    def __len__(self):
        return len(self._cards) 

    def __getitem__(self, position): # to getitem when user used cards[1] 
        return self._cards[position] 

    def spades_high(card): # to understand sorting 
        rank_value = FrenchDeck.ranks.index(card.rank) # index help to find the rank of card from ranks
        return rank_value * len(suit_values) + suit_values[card.suit]   
