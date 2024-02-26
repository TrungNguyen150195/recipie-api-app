"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """test case the calc module """

    def test_adding_number(self):
        """test adding number together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)