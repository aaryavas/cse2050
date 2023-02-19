import unittest 
from practice import sum_k
class Testsumk(unittest.TestCase):
    def test_expected_inputs(self):
        self.assertEqual(sum_k(5),15)

unittest.main()
