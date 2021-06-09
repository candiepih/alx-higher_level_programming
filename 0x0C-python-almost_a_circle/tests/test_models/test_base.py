"""Unittest for the `Base` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Handling of `Base` class test cases"""
    def test_with_no_arguments(self):
        """Tests with no argument passed to object"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_argument(self):
        """Test with one object created but with argument"""
        Base._Base__nb_objects = 0
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_and_without_argument(self):
        """Test with multiple objects with object with argument
        and one without argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_multiple_obj_with_arg_last(self):
        """Test with multiple objects with the one with
        the argument last"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_multiple_obje_with_arg(self):
        """Test with multiple objects both with arguments"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_multiple_with_arg_and_one_last_without(self):
        """Tests for multiple object with arguments then one last
        doesn't have any argument"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_for_private_attribute(self):
        """Check if attribute exists in an object"""
        self.assertFalse(hasattr(Base, '__nb_objects'))

    def test_save_to_file(self):
        """Tests saving of json representation of objects to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(r2.to_dictionary(), my_list[1])
