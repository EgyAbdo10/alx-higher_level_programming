#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test teh base class and its init method"""
    a1 = Base()
    a2 = Base()
    a3 = Base()
    a4 = Base(30)
    a5 = Base()

    def test_instantiation(self):
        
        self.assertIsInstance(TestBase.a1, Base)
    
    def test_id_attr(self):
        self.assertTrue(hasattr(TestBase.a2, "id"))
    
    def test_attr__nb_objects(self):
        self.assertTrue((Base, '_Base__nb_objects'))

    def test_id_None(self):
        self.assertEqual(TestBase.a3.id, 3)
    
    def test_id_not_None(self):

        self.assertEqual(TestBase.a4.id, 30)

    def test_id_after_assigning(self):
        
        self.assertEqual(TestBase.a5.id, 4) # do not know why this not equal 4

if __name__ == "__main__":
    unittest.main()
