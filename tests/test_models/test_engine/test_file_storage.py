#!/usr/bin/python3
"""
Module for FilStorage unittest
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model = BaseModel()
        user_ = User()
        state_ = State()
        place_ = Place()
        city_ = City()
        amenity_ = Amenity()
        review_ = Review()
        models.storage.new(base_model)
        models.storage.new(user_)
        models.storage.new(state_)
        models.storage.new(place_)
        models.storage.new(city_)
        models.storage.new(amenity_)
        models.storage.new(review_)
        self.assertIn("BaseModel." + base_model.id, models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + user_.id, models.storage.all().keys())
        self.assertIn(user_, models.storage.all().values())
        self.assertIn("State." + state_.id, models.storage.all().keys())
        self.assertIn(state_, models.storage.all().values())
        self.assertIn("Place." + place_.id, models.storage.all().keys())
        self.assertIn(place_, models.storage.all().values())
        self.assertIn("City." + city_.id, models.storage.all().keys())
        self.assertIn(city_, models.storage.all().values())
        self.assertIn("Amenity." + amenity_.id, models.storage.all().keys())
        self.assertIn(amenity_, models.storage.all().values())
        self.assertIn("Review." + review_.id, models.storage.all().keys())
        self.assertIn(review_, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base_model = BaseModel()
        user_ = User()
        state_ = State()
        place_ = Place()
        city_ = City()
        amenity_ = Amenity()
        review_ = Review()
        models.storage.new(base_model)
        models.storage.new(user_)
        models.storage.new(state_)
        models.storage.new(place_)
        models.storage.new(city_)
        models.storage.new(amenity_)
        models.storage.new(review_)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user_.id, save_text)
            self.assertIn("State." + state_.id, save_text)
            self.assertIn("Place." + place_.id, save_text)
            self.assertIn("City." + city_.id, save_text)
            self.assertIn("Amenity." + amenity_.id, save_text)
            self.assertIn("Review." + review_.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_model = BaseModel()
        user_ = User()
        state_ = State()
        place_ = Place()
        city_ = City()
        amenity_ = Amenity()
        review_ = Review()
        models.storage.new(base_model)
        models.storage.new(user_)
        models.storage.new(state_)
        models.storage.new(place_)
        models.storage.new(city_)
        models.storage.new(amenity_)
        models.storage.new(review_)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + user_.id, objs)
        self.assertIn("State." + state_.id, objs)
        self.assertIn("Place." + place_.id, objs)
        self.assertIn("City." + city_.id, objs)
        self.assertIn("Amenity." + amenity_.id, objs)
        self.assertIn("Review." + review_.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
