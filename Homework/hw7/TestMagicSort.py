import unittest
import random
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):

        #Testing a sorted list
        sorted_list = [1,2,3,4,5,6,7]
        self.assertEqual(linear_scan(sorted_list), 'sorted')

        #Testing a reverse list
        reversed_list = [7,6,5,4,3,2,1]
        self.assertEqual(linear_scan(reversed_list),'reverse_sorted')

         #Testing a list with less than 5 items out of place
        out_of_place_items = [1, 2, 3, 5, 4]
        self.assertEqual(linear_scan(out_of_place_items), 'insertion')


class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):

        #Testing to make sure the reversed list equals the function output
        pre_reverse = [1,2,3,4,5]
        expected_reverse = [5,4,3,2,1]
        reverse_list(pre_reverse)
        self.assertEqual(pre_reverse,expected_reverse)


class Test_insertionsort(unittest.TestCase):
    def test_insertion_sort(self):

        #Testing an ascending list
        lst1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expectedlst1 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        insertionsort(lst1, 0, len(lst1) - 1)
        self.assertEqual(lst1,expectedlst1)

        #Testing a descending list
        lst2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expectedlst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        insertionsort(lst2, 0, len(lst2) - 1)
        self.assertEqual(lst2,expectedlst2)

        #Testing an empty list
        lst3 = []
        expectedlst3 = []
        insertionsort(lst3, 0, len(lst3) - 1)
        self.assertEqual(lst3,expectedlst3)

        #Testing a single element
        lst4 = [42]
        expectedlst4 = [42]
        insertionsort(lst4, 0, len(lst4) - 1)
        self.assertEqual(lst4,expectedlst4)

        #Testing a list with duplicate elements
        lst5 = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
        expectedlst5 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        insertionsort(lst5, 0, len(lst5) - 1)
        self.assertEqual(lst5,expectedlst5)

class Test_quicksort(unittest.TestCase):
    def test_quicksort(self):

        #Testing an ascending list
        lst1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expectedlst1 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        quicksort(lst1, 0, len(lst1))
        self.assertEqual(lst1,expectedlst1)

        #Testing a descending list
        lst2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expectedlst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        quicksort(lst2, 0, len(lst2))
        self.assertEqual(lst2,expectedlst2)

        #Testing an empty list
        lst3 = []
        expectedlst3 = []
        quicksort(lst3, 0, len(lst3))
        self.assertEqual(lst3,expectedlst3)

        #Testing a single element
        lst4 = [42]
        expectedlst4 = [42]
        quicksort(lst4, 0, len(lst4))
        self.assertEqual(lst4,expectedlst4)

        #Testing a list with duplicate elements
        lst5 = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
        expectedlst5 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        quicksort(lst5, 0, len(lst5))
        self.assertEqual(lst5,expectedlst5)

class Test_mergesort(unittest.TestCase):
     def test_mergesort(self):
            # Test on a small list
        lst1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expectedlst1 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(mergesort(lst1), expectedlst1)

        # Test on a large list of random integers
        n = 10000
        lst2 = [random.randint(0, n) for _ in range(n)]
        expectedlst2 = sorted(lst2)
        self.assertEqual(mergesort(lst2), expectedlst2)

        # Test on an already sorted list
        lst3 = list(range(n))
        expectedlst3 = lst3
        self.assertEqual(mergesort(lst3), expectedlst3)

        # Test on a list with duplicates
        lst4 = [1, 3, 2, 1, 4, 2, 5, 3, 4, 1]
        expectedlst4 = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        self.assertEqual(mergesort(lst4), expectedlst4)

class Test_magic_sort(unittest.TestCase):
    def test_magic_sort(self):
        # Test sorting an already sorted list
        sorted_list = [1, 2, 3, 4, 5, 6, 7]
        algorithms_used1 = magic_sort(sorted_list)
        self.assertEqual(algorithms_used1, {'sorted'})

        # Test sorting a list with some elements out of place
        out_of_place_items = [1, 2, 3, 5, 4]
        expected_out_of_place_items = [1, 2, 3, 4, 5]
        algorithms_used2 = magic_sort(out_of_place_items)
        self.assertEqual(algorithms_used2, {'insertionsort'})
        self.assertEqual(out_of_place_items, expected_out_of_place_items)

        # Test sorting a list in reverse order
        reversed_list = [7, 6, 5, 4, 3, 2, 1]
        expected_reversed_list = [1, 2, 3, 4, 5, 6, 7]
        algorithms_used3 = magic_sort(reversed_list)
        self.assertEqual(algorithms_used3, {'mergesort','quicksort', 'reverse_list', 'insertionsort'})
        self.assertEqual(reversed_list, expected_reversed_list)

        # Test sorting an empty list
        empty_list = []
        algorithms_used1 = magic_sort(empty_list)
        self.assertEqual(algorithms_used1, {'sorted'})

        # Test sorting a list with one element
        one_element_list = [5]
        algorithms_used2 = magic_sort(one_element_list)
        self.assertEqual(algorithms_used2, {'sorted'})
        self.assertEqual(one_element_list, [5])

        # Test sorting a list with all equal elements
        equal_list = [3, 3, 3, 3, 3]
        algorithms_used3 = magic_sort(equal_list)
        self.assertEqual(algorithms_used3, {'sorted'})
        self.assertEqual(equal_list, [3, 3, 3, 3, 3])

        # Test sorting a list with multiple equal elements
        equal_list2 = [2, 1, 3, 2, 3]
        expected_equal_list2 = [1, 2, 2, 3, 3]
        algorithms_used4 = magic_sort(equal_list2)
        self.assertEqual(algorithms_used4, {'insertionsort'})
        self.assertEqual(equal_list2, expected_equal_list2)




unittest.main()