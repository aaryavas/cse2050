import unittest
from waitlist import Waitlist

class Test_Waitlist(unittest.TestCase):
    
    def setUp(self):
        '''Instance variables to test with'''
        # waitlist with entries
        self.w = Waitlist()
        self.w.add_customer('Tom', '17:45')
        self.w.add_customer('Jerry', '20:30')
        self.w.add_customer('Ray', '16:15')
        self.w.add_customer('Aarya', '10:00')
        
        # waitlist with no entries
        self.w2 = Waitlist()


    def test_add_customer(self):
        '''Tests that the program correctly adds customers to queue'''
        # waitlist with entries
        self.assertEqual(len(self.w._entries), 4)
        self.w.add_customer('Jon', '20:00')
        self.assertEqual(len(self.w._entries), 5)

        # waitlist with no entries
        self.assertEqual(len(self.w2._entries), 0)
        self.w2.add_customer('Jon', '20:00')
        self.assertEqual(len(self.w2._entries), 1)
    

    def test_peek(self):
        '''Tests that the program correctly returns customer w/ the highest priority''' 
        # waitlist with entries
        self.assertEqual(self.w.peek(), ('Aarya', '10:00'))
        self.w.add_customer('Jon', '09:00')
        self.assertEqual(self.w.peek(), ('Jon', '09:00'))

        # waitlist with no entries
        self.assertEqual(self.w2.peek(), None)
        self.w2.add_customer('Jon', '09:00')
        self.assertEqual(self.w2.peek(), ('Jon', '09:00'))

        
    def test_seat_customer(self):
        '''
        Tests that the program correctly seats the highest priority customer
        and removes them from the waitlist
        '''
        # waitlist with entries
        self.assertEqual(self.w.seat_customer(), ('Aarya', '10:00'))
        self.assertEqual(len(self.w._entries), 3)

        # waitlist with no entries
        self.assertEqual(self.w2.seat_customer(), None)
        self.assertEqual(len(self.w2._entries), 0)


    def test_print_reservation_list(self):
        '''Tests that the program correctly prints the waitlist in order'''
        # waitlist with entries
        expected = [('Aarya', '10:00'), ('Ray', '16:15'), ('Tom', '17:45'), ('Jerry', '20:30')]
        self.assertEqual(self.w.print_reservation_list(), expected)

        # waitlist with no entries
        self.assertEqual(self.w2.print_reservation_list(), [])
        self.w2.add_customer('Michael', '13:00')
        self.assertEqual(self.w2.print_reservation_list(), [('Michael', '13:00')])


    def test_change_reservation(self):
        '''
        Tests that the program correctly changes a reservation and adjusts
        the waitlist accordingly
        '''
        # uses peek method to identify customer with highest priority (verifies correct order)
        self.w.change_reservation('Aarya', '18:00')
        self.assertEqual(self.w.peek(), ('Ray', '16:15'))
        self.w.change_reservation('Ray', '24:00')
        self.assertEqual(self.w.peek(), ('Tom', '17:45'))


if __name__ == '__main__':
    unittest.main()