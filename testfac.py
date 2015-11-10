import application
import unittest

class Testfactorial(unittest.TestCase):

    def test_verific_number(self):
        self.assertTrue(application.verific_number("5"))
        self.assertFalse(application.verific_number("hi"))



if __name__ == '__main__':
    unittest.main()
