from DLL import DoublyLinkedList as DLL
import unittest

class TestDLL(unittest.TestCase):
    'test cases for doubly-linked list'
    def test_addremovefirst(self):
        'add and remove from beginning of dll'
        n =8 
        dll = DLL()
        for i in range (n): 
            dll.add_first(i)

        for i in range(n):
            self.assertEqual(len(dll), n-i)
            self.assertEqual(dll.remove_first(), n-1-i)
            
unittest.main()