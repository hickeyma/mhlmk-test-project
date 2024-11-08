import unittest

from test_project.dog import dog

class TestDog(unittest.TestCase):

    def setUp(self):
        self.dog = dog.Dog()

    def test_what_am_i(self):
        expected_output = "I am a dog first but also a mammal"
        actual_output = self.dog.what_am_i()
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()