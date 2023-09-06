import unittest

# Fake, just for pass IDE
# def solution(q):
#     for q in text
#     run main with (q) 
#     pass
solution = ["test","test2"]

class TestBinaryGap(unittest.TestCase):
    MAXINT = 2147483647  # The largest input we need worry about.

    def test_dataset(self):
        self.assertEqual(solution[0], "test")

    def test_nodataset(self):
        self.assertEqual(solution[1], "test")