#!/usr/bin/python3
"""Module for unit testing the Rectangle class."""

import unittest
from models.rectangle import Rectangle
import io
import contextlib

class TestRectangle(unittest.TestCase):
    """Test the Rectangle class attributes."""

    rec1 = Rectangle(5, 3, 2, 1, 20)
    rec2 = Rectangle(10, 20, 0, 0)
    rec5 = Rectangle(4, 3, 0, 0, 60)
    rec6 = Rectangle(4, 3)
    rec7 = Rectangle(4, 3, 0, 0, 300)

    def test_instantiation(self):
        """Test if instances are created correctly."""
        self.assertIsInstance(TestRectangle.rec1, Rectangle)

    def test_width(self):
        """Test if width attribute is set correctly."""
        self.assertEqual(TestRectangle.rec1.width, 5)

    def test_height(self):
        """Test if height attribute is set correctly."""
        self.assertEqual(TestRectangle.rec1.height, 3)

    def test_x(self):
        """Test if x attribute is set correctly."""
        self.assertEqual(TestRectangle.rec1.x, 2)

    def test_y(self):
        """Test if y attribute is set correctly."""
        self.assertEqual(TestRectangle.rec1.y, 1) 

    # ... (other attribute tests)

    def test_area_inst(self):
        """Test if area method is present in the instance."""
        self.assertTrue(hasattr(TestRectangle.rec6, "area"))

    def test_area(self):
        """Test if the area method calculates the area correctly."""
        self.assertEqual(TestRectangle.rec6.area(), 12)

# ... (other test classes)

if __name__ == "__main__":
    unittest.main()
