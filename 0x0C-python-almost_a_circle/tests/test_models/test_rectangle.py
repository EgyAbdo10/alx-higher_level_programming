#!/usr/bin/python3
"""this module test class rectangle by unittesting"""


import unittest
from models.rectangle import Rectangle
import io
import contextlib

class TestRectangle(unittest.TestCase):
    """test the rectangle class attributes"""
    rec1 = Rectangle(5, 3, 2, 1, 20)
    rec2 = Rectangle(10, 20, 0, 0)
    rec5 = Rectangle(4, 3, 0, 0, 60)
    rec6 = Rectangle(4, 3)
    rec7 = Rectangle(4, 3, 0, 0, 300)

    def test_instantiation(self):
        """test instantion of objects"""
        self.assertIsInstance(TestRectangle.rec1, Rectangle)

    def test_width(self):
        self.assertEqual(TestRectangle.rec1.width, 5)
    def test_height(self):
        self.assertEqual(TestRectangle.rec1.height, 3)
    def test_x(self):
        self.assertEqual(TestRectangle.rec1.x, 2)
    def test_y(self):
        self.assertEqual(TestRectangle.rec1.y, 1) 

    def test_x_0(self):
        self.assertEqual(TestRectangle.rec2.x, 0)
    def test_y_0(self):
        self.assertEqual(TestRectangle.rec2.y, 0)


    def test_width_not_int(self):
        try:
            rec3 = Rectangle("4", 3)
        except Exception as e:
            self.assertEqual("[TypeError] width must be an integer",
                        "[{}] {}".format(e.__class__.__name__, e))
    def test_width_lt_0(self):
        try:
            rec4 = Rectangle(-1, 3)
        except Exception as e:
            self.assertEqual("[ValueError] width must be > 0",
                "[{}] {}".format(e.__class__.__name__, e))
    def test_width_eq_0(self):
        try:
            rec5 = Rectangle(0, 3)
        except Exception as e:
            self.assertEqual("[ValueError] width must be > 0",
                "[{}] {}".format(e.__class__.__name__, e))
            

    def test_height_not_int(self):
        try:
            rec3 = Rectangle(4, "3")
        except Exception as e:
            self.assertEqual("[TypeError] height must be an integer",
                        "[{}] {}".format(e.__class__.__name__, e))
    def test_height_lt_0(self):
        try:
            rec4 = Rectangle(1, -3)
        except Exception as e:
            self.assertEqual("[ValueError] height must be > 0",
                "[{}] {}".format(e.__class__.__name__, e))
    def test_height_eq_0(self):
        try:
            rec5 = Rectangle(3, 0)
        except Exception as e:
            self.assertEqual("[ValueError] height must be > 0",
                "[{}] {}".format(e.__class__.__name__, e))
            

    def test_x_not_int(self):
        try:
            rec3 = Rectangle(4, 3, "0", 0, 50)
        except Exception as e:
            self.assertEqual("[TypeError] x must be an integer",
                        "[{}] {}".format(e.__class__.__name__, e))
    def test_x_lt_0(self):
        try:
            rec4 = Rectangle(4, 3, -1, 0, 70)
        except Exception as e:
            self.assertEqual("[ValueError] x must be >= 0",
                "[{}] {}".format(e.__class__.__name__, e))

    def test_x_eq_0(self):
        self.assertEqual(TestRectangle.rec5.x, 0)

    def test_x_not_assigned(self):
        
        self.assertEqual(TestRectangle.rec6.x, 0)


    def test_y_not_int(self):
        try:
            rec3 = Rectangle(4, 3, 0, "0", 100)
        except Exception as e:
            self.assertEqual("[TypeError] y must be an integer",
                        "[{}] {}".format(e.__class__.__name__, e))
    def test_y_lt_0(self):
        try:
            rec4 = Rectangle(4, 3, 1, -2, 200)
        except Exception as e:
            self.assertEqual("[ValueError] y must be >= 0",
                "[{}] {}".format(e.__class__.__name__, e))
    def test_y_eq_0(self):

        self.assertEqual(TestRectangle.rec7.x, 0)
    
    def test_y_not_assigned(self):
        self.assertEqual(TestRectangle.rec6.y, 0)

    def test_area_inst(self):
        self.assertTrue(hasattr(TestRectangle.rec6, "area"))

    def test_area(self):
        self.assertEqual(TestRectangle.rec6.area(), 12)

class TestIds(unittest.TestCase):
    """test the rectangle class id attributes for various cases"""
    rec1 = Rectangle(5, 3, 2, 1, 20)
    rec2 = Rectangle(10, 20, 0, 0)
    def test_id_notNone(self):
        self.assertEqual(TestRectangle.rec1.id, 20)
    def test_idNone(self):
        self.assertEqual(TestRectangle.rec2.id, 5)
    
class TestRectangle_2(unittest.TestCase):
    """test the rectangle class methods for various cases"""
    r1 = Rectangle(4, 6, 2, 1, 12)
    def test_str(self):
        self.assertEqual(str(TestRectangle_2.r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        f = io.StringIO()
        f2 = io.StringIO()
        rec = Rectangle(2, 2, 1, 1, 20)
        rec2 = Rectangle(2, 3)
        with contextlib.redirect_stdout(f):
            rec.display()
        printed = f.getvalue()
        # x and y - 0
        self.assertEqual(printed, "\n ##\n ##\n")
        with contextlib.redirect_stdout(f2):
            rec2.display()
        printed = f2.getvalue()
        self.assertEqual(printed, "##\n##\n##\n")

class TestRectangle_3(unittest.TestCase):
    """test the rectangle update method and more for various cases"""
    def test_update_args(self):
        rec1 = Rectangle(2, 3, 1, 2, 100)
        # all aruments provided
        rec1.update(5, 4, 6, 7, 50)
        self.assertEqual((5, 4, 6, 7, 50),
            (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        rec1.update()
        self.assertEqual((5, 4, 6, 7, 50),
            (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        # not all aruments provided
        rec1.update(33, 10)
        self.assertEqual((33, 10, 6, 7, 50),
            (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        # unacceptable args
        with self.assertRaises(ValueError) as context:
            rec1.update(2, -2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_update_kwargs(self):
        rec1 = Rectangle(2, 3, 1, 2, 100)
        # all kwargs in order
        kwargs = {"id": 30, "width": 5, "height": 6, "x": 13, "y": 12}
        rec1.update(**kwargs)
        self.assertEqual((30, 5, 6, 13, 12),
                        (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        # all kwargs not in order
        kwargs_2 = {"width": 7, "id": 20, "x": 15, "height": 8, "y": 1}
        rec1.update(**kwargs_2)
        self.assertEqual((20, 7, 8, 15, 1),
                        (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        # not full kwargs
        kwargs_3 = {"width": 23, "y": 20}
        rec1.update(**kwargs_3)
        self.assertEqual((20, 23, 8, 15, 20),
                        (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))
        # skip kwargs if args exists adn empty
        rec1.update(10, 20, **kwargs_3)
        self.assertEqual((10, 20, 8, 15, 20),
                        (rec1.id, rec1.width, rec1.height, rec1.x, rec1.y))

if __name__ == "__main__":
    unittest.main()