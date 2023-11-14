#!/usr/bin/python3
"""Module for unit testing the Base class."""

import unittest
from models.base import Base
import json

class TestBase_1(unittest.TestCase):
    """Test the Base class and its initialization method."""
    
    a1 = Base()
    a2 = Base()
    a3 = Base()
    a4 = Base(30)
    a5 = Base()

    def test_instantiation(self):
        """
        Test if instances are created correctly.
        """
        self.assertIsInstance(TestBase_1.a1, Base)
    
    def test_id_attr(self):
        """
        Test if instances have the 'id' attribute.
        """
        self.assertTrue(hasattr(TestBase_1.a2, "id"))
    
    def test_attr__nb_objects(self):
        """
        Test if the '__nb_objects' attribute is present in the Base class.
        """
        self.assertTrue(hasattr(Base, '_Base__nb_objects'))

    def test_id_None(self):
        """
        Test if the 'id' attribute is incremented when not explicitly provided.
        """
        self.assertEqual(TestBase_1.a3.id, 3)
    
    def test_id_not_None(self):
        """
        Test if the 'id' attribute is set when explicitly provided.
        """
        self.assertEqual(TestBase_1.a4.id, 30)

    def test_id_after_assigning(self):
        """
        Test if the 'id' attribute is incremented after assigning an explicit value.
        """
        self.assertEqual(TestBase_1.a5.id, 4)

class TestBase_2(unittest.TestCase):
    """Test the methods from the Base class."""
    
    dict_list = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
    dict_list_str = json.dumps([{"a": 1, "b": 2}, {"c": 3, "d": 4}])

    def test_to_json_string_is_static(self):
        """
        Test if the to_json_string method is static.
        """
        self.assertTrue(hasattr(Base, "to_json_string"))

    def test_to_json_str_1(self):
        """
        Test common use cases for the to_json_string method.
        """
        self.assertEqual(TestBase_2.dict_list_str,
                        Base.to_json_string(TestBase_2.dict_list))
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string([]))
    
    def test_to_json_str_2(self):
        """
        Test for non-list of dictionaries objects.
        """
        int1 = 4
        self.assertEqual(str(int1), Base.to_json_string(int1))

if __name__ == "__main__":
    unittest.main()
