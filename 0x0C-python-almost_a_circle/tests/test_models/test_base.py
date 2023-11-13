#!/usr/bin/python3
import unittest
from models.base import Base
import json
class TestBase_1(unittest.TestCase):
    """Test teh base class and its init method"""
    a1 = Base()
    a2 = Base()
    a3 = Base()
    a4 = Base(30)
    a5 = Base()

    def test_instantiation(self):
        
        self.assertIsInstance(TestBase_1.a1, Base)
    
    def test_id_attr(self):
        self.assertTrue(hasattr(TestBase_1.a2, "id"))
    
    def test_attr__nb_objects(self):
        self.assertTrue((Base, '_Base__nb_objects'))

    def test_id_None(self):
        self.assertEqual(TestBase_1.a3.id, 3)
    
    def test_id_not_None(self):

        self.assertEqual(TestBase_1.a4.id, 30)

    def test_id_after_assigning(self):
        
        self.assertEqual(TestBase_1.a5.id, 4)

class TestBase_2(unittest.TestCase):
    """test the methods from base class"""
    dict_list = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
    dict_list_str = json.dumps([{"a": 1, "b": 2}, {"c": 3, "d": 4}])

    def test_to_json_string_is_static(self):
        self.assertTrue(hasattr(Base, "to_json_string"))

    def test_to_json_str_1(self):
        """test common use cases for base.to_json_str"""
        self.assertEqual(TestBase_2.dict_list_str,
                        Base.to_json_string(TestBase_2.dict_list))
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string([]))
    
    def test_to_json_str_2(self):
        """test for not list of dicts objects"""
        int1 = 4
        self.assertEqual(str(int1), Base.to_json_string(int1))

if __name__ == "__main__":
    unittest.main()
