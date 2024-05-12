import unittest
from unittest import TestCase
from code_4_zad_2 import folder_creation


class TestFolderCreation(TestCase):
    # Создание папки
    def test_API_positive(self):
        folder_name = "test"
        ya_token = ""
        self.assertEqual(folder_creation(folder_name, ya_token), 201)

    # Повторное создание папки
    def test_API_negative(self):
        folder_name = "test"
        ya_token = ""
        self.assertNotEqual(folder_creation(folder_name, ya_token), 409)


if __name__ == "__main__":
    unittest.main()
