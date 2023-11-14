#!/usr/bin/python3
"""this module test class square by unittesting"""


import unittest
from models.square import Square
import io
import contextlib

class TestSquare(unittest.TestCase):
    """this class tests the square class and its instances"""
    def test_instance(self):
        s1 = Square(3)
        self.assertIsInstance(s1, Square)