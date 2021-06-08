"""Contains test cases of `Rectangle` class which extends the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the ractangle class"""
    def width_height_integers(self):
        """Tests for width and height as integers"""
        Base._Base.__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def with_all_arguments(self):
        """Test with all valid arguments"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_for_private_width(self):
        """Testing for width as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_for_private_height(self):
        """Test for height as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def test_for_private_x(self):
        """Test for x as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_for_private_y(self):
        """Test for y as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def width_setter_getter_with_int(self):
        """Test width setter and getter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.width = 5
        self.assertEqual(r3.width, 5)

    def width_setter_getter_with_other_type(self):
        """Test width setter and geter with other data type"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.width = "5"

    def width_with_negative(self):
        """Test with seter and getter with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(-2, 3)

    def width_with_zero(self):
        "Test setter and getter with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 3)

    def height_with_string(self):
        """Test height setter and geter with other data type"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, "2")

    def height_with_negative(self):
        """Test height with seter and getter with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, -3)

    def height_with_zero(self):
        "Test setter and getter with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 3)

    def test_with_no_argument(self):
        """Test with no argument supplied"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle()
