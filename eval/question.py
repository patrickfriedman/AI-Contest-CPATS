import unittest


# Fake, just for pass IDE
def solution():
    pass


class TestBinaryGap(unittest.TestCase):
    MAXINT = 2147483647  # The largest input we need worry about.

    def test_examples(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)

    def test_example1(self):
        self.assertEqual(5, solution(1041))

    def test_example2(self):
        self.assertEqual(0, solution(15))

    def test_extremes(self):
        self.assertEqual(0, solution(1))
        self.assertEqual(1, solution(5))
        self.assertEqual(0, solution(self.MAXINT))

    def test_trailing_zeros(self):
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(328), 2)

    def test_simple1(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(11), 1)
        self.assertEqual(solution(32), 0)

    def test_simple2(self):
        self.assertEqual(solution(19), 2)
        self.assertEqual(solution(42), 1)

    def test_simple3(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(5), 1)

    def test_medium1(self):
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(20), 1)

    def test_medium2(self):
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(9), 2)

    def test_medium3(self):
        self.assertEqual(solution(66561), 9)

    def test_large1(self):
        self.assertEqual(solution(6291457), 20)

    def test_large2(self):
        self.assertEqual(solution(74901729), 4)

    def test_large3(self):
        self.assertEqual(solution(805306369), 27)

    def test_large4(self):
        self.assertEqual(solution(1376796946), 5)

    def test_large5(self):
        self.assertEqual(solution(1073741825), 29)

    def test_large6(self):
        self.assertEqual(solution(1610612737), 28)
