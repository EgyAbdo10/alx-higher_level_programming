#!/usr/bin/python3

"""this module is for defining the sqaure class
, inheriting the rectangle class"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class creates instances of squares
    with specific characteristics and inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """define a square instance of size and x, y and id"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """get the str repr of the shape which reoresent all the attrs"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        """get the size of the square"""
        return self.width
    @size.setter
    def size(self, new_size):
        """set the size of the square"""
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """update the shape attributes by args or kwargs"""
        my_args = ["id", "size", "x", "y"]
        if len(args) != 0:
            for i in range(len(my_args)):
                setattr(self, my_args[i], args[i])
        else:
            for item in kwargs.items():
                if (hasattr(self, item[0])):
                    setattr(self, item[0], item[1])
    
    def to_dictionary(self):
        """turn the shape into a dict of attrs"""
        return {"id" : self.id, "size" : self.width,
                "x" : self.x, "y" : self.y}