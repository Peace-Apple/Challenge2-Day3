import unittest
from missing_numbers import missing_num


class test_missing_number(unittest.TestCase):

    def test_missing_no(self):
        self.assertListEqual(missing_num(
            [1, 2, 3, 5, 6, 7, 9]), [4, 8])
        self.assertEqual(len(missing_num([1, 2, 3, 5, 6, 7, 9])), 2)

    def test_input(self):
        self.assertEqual(missing_num((1, 2, 5)), 'only lists are accepted')


if __name__ == '__main__':
    unittest.main()
