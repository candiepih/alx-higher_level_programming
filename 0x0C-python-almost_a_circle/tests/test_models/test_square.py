"""Contains unittest cases for `Square` class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests all methods and attributes of the `Square`
    class
    """
    def test_size(self):
        """Test creating `Square` with integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_with_zero(self):
        """Test size with zero"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_size_with_negative(self):
        """Test size with negative number"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
            self.assertEqual(e, "width must be > 0")

    def test_size_string(self):
        """Test size with string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("5k")
            self.assertEqual(e, "width must be an integer")

    def test_size_list(self):
        """Test size with list"""
        with self.assertRaises(TypeError) as e:
            s1 = Square([3, 5, 2, 4])
            self.assertEqual(e, "width must be an integer")

    def test_size_dict(self):
        """Test size with dictionary"""
        with self.assertRaises(TypeError) as e:
            s1 = Square({"n": 2, "b": 4})
            self.assertEqual(e, "width must be an integer")

    def test_size_tuple(self):
        """Test size with tuple"""
        with self.assertRaises(TypeError) as e:
            s1 = Square((3, 5, 2, 4))
            self.assertEqual(e, "width must be an integer")

    def test_size_float(self):
        """Test size with float"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(6.96)
            self.assertEqual(e, "width must be an integer")

    def test_size_nan(self):
        """Test size with not a number(nan)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('nan'))
            self.assertEqual(e, "width must be an integer")

    def test_size_inf(self):
        """Test size with Infinity(inf)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('inf'))
            self.assertEqual(e, "width must be an integer")

    def test_printing_square(self):
        """Test string output of `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_size_with_no_argument(self):
        """Test without argument supplied"""
        with self.assertRaises(TypeError) as e:
            s1 = Square()
            self.assertEqual(e, "__init__() missing 1 required \
                             positional argument: 'size'")

    def test_size_private(self):
        """Tests if size is an attribute of Square"""
        self.assertFalse(hasattr(Square, "_Square__size"))

    def test_area(self):
        """Testing area of `Square`"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_with_id(self):
        """Test square string representation with id argument"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        s2 = Square(1)
        s3 = Square(3, 1, 3, 83)
        self.assertEqual(s3.__str__(), "[Square] (83) 1/3 - 3")

    def test_x_with_negative(self):
        """Test x with a negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, -5, 3, 83)
            self.assertEqual(e, "x must be >= 0")

    def test_x_with_string(self):
        """Test x with a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, "8", 3, 83)
            self.assertEqual(e, "x must be an integer")

    def test_y_with_negative(self):
        """Test y with a negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, 5, -3, 83)
            self.assertEqual(e, "y must be >= 0")

    def test_y_with_string(self):
        """Test y with a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, 8, "3", 83)
            self.assertEqual(e, "y must be an integer")
