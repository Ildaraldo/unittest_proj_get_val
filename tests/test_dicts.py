import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({'A': 1, 'B': 2, 'C': 3}, 'B'), 2)
        self.assertEqual(dicts.get_val({'A': 1, 'B': 2, 'C': 3}, 'R', 'Z'), 'Z')
        self.assertEqual(dicts.get_val({'A': 1, 'B': 2, 'C': 3}, 3, 'Z'), 'Z')
