import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    rec1 = Rectangle(5, 3, 2, 1, 20)
    rec2 = Rectangle(10, 20, 0, 0)
    rec5 = Rectangle(4, 3, 0, 0, 60)
    rec6 = Rectangle(4, 3)
    rec7 = Rectangle(4, 3, 0, 0, 300)
    def test_instantiation(self):
        self.assertIsInstance(TestRectangle.rec1, Rectangle)
    
    def test_width(self):
        self.assertEqual(TestRectangle.rec1.width, 5)
    def test_height(self):
        self.assertEqual(TestRectangle.rec1.height, 3)
    def test_x(self):
        self.assertEqual(TestRectangle.rec1.x, 2)
    def test_y(self):
        self.assertEqual(TestRectangle.rec1.y, 1) 


    def test_id_notNone(self):
        self.assertEqual(TestRectangle.rec1.id, 20)
    # def test_idNone(self):
    #     self.assertEqual(TestRectangle.rec2.id, 1)


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

if __name__ == "__main__":
    unittest.main()