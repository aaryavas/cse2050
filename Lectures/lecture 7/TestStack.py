from stack import stackSet as stack
from stack import Queue
import unittest

class TestStack(unittest.TestCase):
    'unittests for stack'

    def test_pushpop(self):
        s= stack()
        n=10 

        for i in range(n):
            s.push(i)

        # 0 
        for i in range(n):
            self.assertEqual(s.pop(), n-1-i) 

class TestQueue(unittest.TestCase):
    'unittests for stack'

    def test_pushpop(self):
        q= Queue()
        n=10 

        for i in range(n):
            q.enqueue(i)

        # 0 
        for i in range(n):
            self.assertEqual(q.enqueue(), i) 



unittest.main()       
