import application
import unittest

class Testfactorial(unittest.TestCase):

    def test_verific_number(self):
        self.assertTrue(application.verific_number("5"))
        self.assertFalse(application.verific_number("hi"))

    def test_factorial(self):
        self.assertNotAlmostEqual(application.factorial(5),0)


if __name__ == '__main__':
    unittest.main()
