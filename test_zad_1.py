import unittest
from code_1_zad_1 import vote
from code_2_zad_1 import solution
from code_3_zad_1 import check_email


def code_1_zad_1(votes, expected):
    result = vote(votes)
    try:
        assert result == expected
        print(f"Test for {votes} passed with result {result}")
    except AssertionError:
        print(f"Test for {votes} failed. Correct result {result}")


def code_2_zad_1(a, b, c, expected):
    result = solution(a, b, c)
    try:
        assert result == expected
        print(f"Test for {a}, {b}, {c} passed with result {result}")
    except AssertionError:
        print(f"Test for {a}, {b}, {c} failed. Correct result {result}")


def code_3_zad_1(email, expected):
    result = check_email(email)
    try:
        assert result == expected
        print(f"Test for {email} passed with result {result}")
    except AssertionError:
        print(f"Test for {email} failed. Correct result {result}")


if __name__ == "__main__":

    code_1_zad_1([1, 1, 1, 2, 3], 1)
    code_1_zad_1([1, 2, 3, 2, 2], 2)

    code_2_zad_1(1, -13, 12, (12.0, 1.0))
    code_2_zad_1(-4, 28, -49, 3.5)
    code_2_zad_1(1, 1, 1, "корней нет")

    code_3_zad_1("Helloworld@.ru", True)
    code_3_zad_1("Helloworld@.com", False)
