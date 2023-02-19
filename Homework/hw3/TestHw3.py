from hw3 import find_pairs_naive, find_pairs_optimized
import unittest

class testhw3(unittest.TestCase):
    #tests functions find_pairs_naive and find_pairs_optimized
    def test_func(self):
        
        
        # tests if functions output the right values
        L =[6,5,2,8,9,1]
        self.assertEqual(find_pairs_optimized(L,7),{(6, 1), (5, 2)})
        self.assertEqual(find_pairs_naive(L,7),{(6, 1), (2, 5)})

        #tests if functions output right values when list is empty
        Lempty = []
        s = set() 
        self.assertEqual(find_pairs_optimized(Lempty,7),s)
        self.assertEqual(find_pairs_naive(Lempty,7),s)

        #tests if target is 0
        L =[6,5,2,8,9,1]
        s = set() 
        self.assertEqual(find_pairs_optimized(L,0),s)
        self.assertEqual(find_pairs_naive(L,0),s) 

        #test case for expect duplicate values 
        L =[1,2,3,4,5]
        self.assertEqual(find_pairs_optimized(L,10),s)
        self.assertEqual(find_pairs_naive(L,10),s)

        #test case for double numbers 
        L =[1,2,3,4,5]
        self.assertEqual(find_pairs_optimized(L,6),{(2, 4), (1, 5)})
        self.assertEqual(find_pairs_naive(L,6),{(4, 2), (1, 5)})

unittest.main()
