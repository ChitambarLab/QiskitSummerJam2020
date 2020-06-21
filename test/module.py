import unittest

from module import example


class module_test_cases(unittest.TestCase):
    def test_hello(self):
        example.hello()
        pass
    
    def test_add_two(self):
        self.assertEqual(4, example.add_two(2))
        self.assertEqual(7, example.add_two(5))
