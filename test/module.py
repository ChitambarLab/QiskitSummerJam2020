import unittest

from module import test


class module_test_cases(unittest.TestCase):
    def test_hello(self):
        test.hello()
        pass
    
    def test_add_two(self):
        self.assertEqual(4, test.add_two(2))
        self.assertEqual(7, test.add_two(5))
