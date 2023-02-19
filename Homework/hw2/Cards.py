import random
class Card(object):
    ''' 
    A class representing a standard playing card.
    '''
    def __init__(self, value, suit):
        ''' 
        Initializes a new instance of the `Card` class.
        '''
        self.value = value
        self.suit = suit

    def __repr__(self):
        '''
        Returns a string representation of the `Card` object.
        
        '''
        return f'Card({self.value} of {self.suit})'
    def __lt__(self,other):
        '''Compares two `Card` objects to determine which is 'less than' the other.'''
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        elif self.suit == other.suit:
            if self.value > other.value:
                return True 
            elif self.value < other.value:
                return False




class Deck(object):
    ''' 
    A class representing a deck of cards.'''
    def __init__(self,value = list(range(1,14)), suits = ('clubs', 'diamonds', 'hearts')):
        '''
        The constructor for the Deck class.
        Creates a list of all the cards in the deck.
        '''
        self.card_list = [Card(v,s)for v in value for s in suits]
    def __len__(self):
        '''
         A special method that returns the length of the deck.
        '''
        return len(self.card_list) 
    def sort(self): 
        '''
        Sorts the deck of cards in ascending order.
        '''
        return self.card_list.sort()
    def __repr__(self): #this is wrong
        '''
        A special method that returns a string representation of the deck.
        '''
        return f'Deck: [{",".join([repr(i) for i in self.card_list])}]'
    def shuffle(self):
        '''
        Shuffles the deck of cards randomly.
        '''
        random.shuffle(self.card_list)
    def draw_top(self):
        '''
        Draws the top card from the deck.
        '''
        try:
            return self.card_list[-1]  
        except: 
            raise RuntimeError('Cannot draw from empty deck')
        

     

class Hand(Deck):
    '''A class representing players hand'''
    def __init__(self,card_list):
        '''
        The constructor for the Hand class.
        Creates a list of cards in hand
        '''
        self.card_list = card_list
    def __repr__(self):
        '''
        
        A special method that returns a string representation of the hand
        
        '''
        return f'Hand: {self.card_list}'
    def play(self, card):
        '''
        plays hand 
        '''
        try:
            return self.card_list.pop(self.card_list.index(card))
        except ValueError:
            raise RuntimeError (f'Attempt to play {repr(card)} that is not in {self.__repr__()}')