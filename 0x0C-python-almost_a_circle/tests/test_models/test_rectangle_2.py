import unittest
from models.rectangle import Rectangle

class TestRectangle_2(unittest.TestCase):
    r1 = Rectangle(4, 6, 2, 1, 12)
    def test_str(self):
        self.assertEqual(str(TestRectangle_2.r1), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
