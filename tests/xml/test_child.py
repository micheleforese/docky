import unittest


from docky import utility
from docky.console import console


class Test1(unittest.TestCase):
    def test_area(self):
        console.print(utility.hash("42543"))
        self.assertAlmostEqual(1, 1)
        self.assertAlmostEqual(1, 2)
