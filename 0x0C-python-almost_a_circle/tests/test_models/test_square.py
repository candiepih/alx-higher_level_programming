"""Contains unittest cases for `Square` class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCases):
    """Tests all methods and attributes of the `Square`
    class
    """
    def test_size(self):
        """Test creating `Square` with integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_with_string(self):
        """Test size with string"""
        try:
            s1 = Square("5k")
        except TypeError as e:
            self.assertEqual(e, "width must be an integer")

    def test_printing_square(self):
        """Test string output of `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__init__(), "[Square] (1) 0/0 - 5")
