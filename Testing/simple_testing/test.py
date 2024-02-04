import unittest
import main

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(3, 5), 8)
        self.assertEqual(main.add(5, 5), 10)
        self.assertEqual(main.add(-5, 9), 4)

    def test_mul(self):
        result = main.mul(3, 7)
        self.assertEqual(result, 21)


if "__name__" == "__main__":
    unittest.main()