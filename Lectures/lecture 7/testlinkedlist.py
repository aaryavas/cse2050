from linkedlist import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    'LinkedList tests'

    def test_addfirst_removefirst(self):
        n =5 
        l1 = LinkedList()
        

        for i in range(n):
            self.assertEqual(len(l1), n-i)
            self.assertEqual(l1.remove_first(), n-1=i)

unittest.main()