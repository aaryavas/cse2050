from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                assert puzzle([3, 6, 4, 1, 3, 4, 2, 0])

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                assert puzzle([1,0,0])

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                assert puzzle([3,0,2,0,0])
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                assert not puzzle([0, 0])

unittest.main()