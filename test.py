import unittest
from Markov import run

class TestCode(unittest.TestCase):

    # This test will check if length is correct
    def testwillWork(self):
        length = run()
        self.assertTrue(len(length) <=160)

    # This test should fail as 5 equals 8 not 7
    def testwillNotWork(self):
        length = run()
        self.assertTrue(len(length) ==10)


if __name__ == '__main__':
    unittest.main()
