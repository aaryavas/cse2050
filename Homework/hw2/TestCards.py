from Cards import Card, Deck, Hand
import unittest
import random

#tests Card
class TestCard(unittest.TestCase):
    '''
    The class tests the `Card` class from the `Cards` module.
    '''
    def test_init(self):
        '''
        The method tests the initialization of a `Card` object. 
        The test verifies that the `value` and `suit` attributes are set correctly.
        '''
        c1 = Card(3, 'hearts')
        self.assertEqual(c1.value,3)
        self.assertEqual(c1.suit,'hearts')
    def test_repr(self):
        '''
        The method tests the `repr` method of the `Card` object.
        The test verifies that the representation of the `Card` object is as expected.
        '''

        c1 = Card(3, 'hearts')
        self.assertEqual(repr(c1),'Card(3 of hearts)')
    def test_lt(self):
        '''
        The method tests the `lt` method of the `Card` object.
        The test verifies that the comparison of two `Card` objects is as expected.
        '''
        c1 = Card(3, 'hearts')
        c2 = Card(3, 'spades')
        self.assertTrue(c1<c2, True)  
    
    
#tests Deck
class TestDeck(unittest.TestCase):
    '''
    The class tests the `Deck` class from the `Cards` module.
    '''
    def test_init(self):
        '''
        The method tests the initialization of a `Deck` object. 
        The test verifies that the deck length is as expected.
        '''
        d1 = Deck()
        self.assertTrue(len(d1), 52)  
        d2= Deck([2, 1], ['triangles', 'dots'])
        self.assertTrue(len(d2), 4)
        '''
        The method tests the `repr` method of the `Deck` object.
        The test verifies that the representation of the `Deck` object is as expected.
        '''
    def test_repr(self):
        d2= Deck([2, 1], ['triangles', 'dots'])
        self.assertTrue(repr(d2),'Deck: [Card(2 of triangles), Card(1 of dots), Card(2 of dots), Card(1 of triangles)]')
        '''
        The method tests the `shuffle` method of the `Deck` object.
        The test verifies that the order of the deck changes after shuffling.
        '''
    def test_shuffle(self):
        d2 = Deck([2, 1], ['triangles', 'dots'])
        d2.shuffle()
        self.assertNotEqual(repr(d2),'Deck: [Card(2 of triangles), Card(1 of dots), Card(2 of dots), Card(1 of triangles)]')
        """
        Test if the first card of the deck is correctly represented after being drawn from the top.
        """  
  
    def test_drawtop(self):
        d2 = Deck([2, 1], ['triangles', 'dots'])
        self.assertTrue(repr(d2),'Card(1 of triangles)')
    """
    Test if the deck is correctly sorted.
    """
 
 
    def test_sort(self):
        d2 = Deck([2, 1], ['triangles', 'dots'])
        d3 = d2.sort()
        self.assertNotEqual(repr(d3),'Deck: [Card(2 of triangles), Card(1 of dots), Card(2 of dots), Card(1 of triangles)]')

#test Hand 
class TestHand(unittest.TestCase):
    """
    Test if the Hand is initialized correctly.
    """
    def test_init(self):
        h_clubs = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])
        self.assertTrue(repr(h_clubs),'Hand: [Card(5 of clubs), Card(4 of clubs), Card(3 of clubs), Card(2 of clubs)')
    """
    Test if the correct card is played from the Hand and the correct behavior occurs when playing a card.
    """  
 
    def test_play(self):
        h1 = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])

        card = h1.play(Card(3, 'clubs'))
        self.assertEqual(repr(card), "Card(3 of clubs)")
        self.assertEqual(len(h1), 4)
        self.assertEqual(h1.play(Card(1, 'clubs')), Card(1, 'clubs'))

        with self.assertRaises(RuntimeError):
            h1.play(Card(1, 'clubs'))

    """
    Test if the string representation of the Hand is correct.
    """


    def test_repr(self):
        h_clubs = Hand([Card(value, 'clubs') for value in range(1, 5, 1)])
        self.assertEqual(repr(h_clubs),'Hand: [Card(1 of clubs), Card(2 of clubs), Card(3 of clubs), Card(4 of clubs)]')
unittest.main() #Runs all tests