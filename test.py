import unittest
from unittest import TestCase
from code_1_zad_1 import vote
from code_2_zad_1 import solution
from code_3_zad_1 import check_email


class TestMain(TestCase):
    def test_vote(self):
        self.assertEqual(vote([1, 1, 1, 2, 3]), "1")

    def test_solution(self):
        self.assertEqual(solution(1, -13, 12), (12.0, 1.0))

    def test_email(self):
        self.assertEqual(check_email("Helloworld@.ru"), True)


if __name__ == "__main__":
    unittest.main()
