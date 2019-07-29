from django.test import TestCase

from app.calc import add, subtract


# functions in the test class have to start with
# "test" so python can run them as tests
class CalcTest(TestCase):

    def test_add_numbers(self):
        """
        Test that two numbers are added together
        """
        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """
        Test that two numbers are subtracted and returned
        """
        self.assertEqual(subtract(4, 3), 1)
