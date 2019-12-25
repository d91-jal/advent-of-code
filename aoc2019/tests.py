import unittest
from aoc2019 import day01, day02, day03, day04, day05, day06, day07, day08, day09, day10


class RegTestSolutions(unittest.TestCase):
    def test_d1p1(self):
        self.assertEqual(day01.part_1(), 3271095)

    def test_d1p2(self):
        self.assertEqual(day01.part_2(), 4903759)

    def test_d2p1(self):
        self.assertEqual(day02.part_1(), 5305097)

    def test_d2p2(self):
        self.assertEqual(day02.part_2(), 4925)

    def test_d3p1(self):
        self.assertEqual(day03.part_1(), 258)

    def test_d3p2(self):
        self.assertEqual(day03.part_2(), 12304)

    def test_d4p1(self):
        self.assertEqual(day04.part_1(), 594)

    def test_d4p2(self):
        self.assertEqual(day04.part_2(), 364)

    def test_d5p1(self):
        self.assertEqual(day05.part_1(), 15426686)

    def test_d5p2(self):
        self.assertEqual(day05.part_2(), 11430197)

    def test_d6p1(self):
        self.assertEqual(day06.part_1(), 135690)

    def test_d6p2(self):
        self.assertEqual(day06.part_2(), 298)

    def test_d7p1(self):
        self.assertEqual(day07.part_1(), 34852)

    def test_d7p2(self):
        self.assertEqual(day07.part_2(), 44282086)

    def test_d8p1(self):
        self.assertEqual(day08.part_1(), 2460)

    def test_d8p2(self):
        self.assertEqual(day08.part_2()[0:20], [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0])


if __name__ == '__main__':
    unittest.main()





