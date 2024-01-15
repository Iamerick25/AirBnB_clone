#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
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

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place_))
        self.assertNotIn("city_id", place_.__dict__)

    def test_user_id_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place_))
        self.assertNotIn("user_id", place_.__dict__)

    def test_name_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place_))
        self.assertNotIn("name", place_.__dict__)

    def test_description_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place_))
        self.assertNotIn("desctiption", place_.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place_))
        self.assertNotIn("number_rooms", place_.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place_))
        self.assertNotIn("number_bathrooms", place_.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place_))
        self.assertNotIn("max_guest", place_.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place_))
        self.assertNotIn("price_by_night", place_.__dict__)

    def test_latitude_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place_))
        self.assertNotIn("latitude", place_.__dict__)

    def test_longitude_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place_))
        self.assertNotIn("longitude", place_.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        place_ = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place_))
        self.assertNotIn("amenity_ids", place_.__dict__)

    def test_two_places_unique_ids(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_two_places_different_created_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.created_at, place_2.created_at)

    def test_two_places_different_updated_at(self):
        place_1 = Place()
        sleep(0.05)
        place_2 = Place()
        self.assertLess(place_1.updated_at, place_2.updated_at)

    def test_str_representation(self):
        date_ = datetime.today()
        date_rep = repr(date_)
        place_ = Place()
        place_.id = "777777"
        place_.created_at = place_.updated_at = date_
        date_str = place_.__str__()
        self.assertIn("[Place] (777777)", date_str)
        self.assertIn("'id': '777777'", date_str)
        self.assertIn("'created_at': " + date_rep, date_str)
        self.assertIn("'updated_at': " + date_rep, date_str)

    def test_args_unused(self):
        place_ = Place(None)
        self.assertNotIn(None, place_.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_ = datetime.today()
        date_iso = date_.isoformat()
        place_ = Place(id="777", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place_.id, "777")
        self.assertEqual(place_.created_at, date_)
        self.assertEqual(place_.updated_at, date_)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
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

    def test_one_save(self):
        place_ = Place()
        sleep(0.05)
        first_updated_at = place_.updated_at
        place_.save()
        self.assertLess(first_updated_at, place_.updated_at)

    def test_two_saves(self):
        place_ = Place()
        sleep(0.05)
        first_updated_at = place_.updated_at
        place_.save()
        second_updated_at = place_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place_.save()
        self.assertLess(second_updated_at, place_.updated_at)

    def test_save_with_arg(self):
        place_ = Place()
        with self.assertRaises(TypeError):
            place_.save(None)

    def test_save_updates_file(self):
        place_ = Place()
        place_.save()
        place__id = "Place." + place_.id
        with open("file.json", "r") as f:
            self.assertIn(place__id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class.
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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        place_ = Place()
        self.assertIn("id", place_.to_dict())
        self.assertIn("created_at", place_.to_dict())
        self.assertIn("updated_at", place_.to_dict())
        self.assertIn("__class__", place_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        place_ = Place()
        place_.middle_name = "Johnson"
        place_.my_number = 777
        self.assertEqual("Johnson", place_.middle_name)
        self.assertIn("my_number", place_.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        place_ = Place()
        place_dict = place_.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        date_ = datetime.today()
        place_ = Place()
        place_.id = "777777"
        place_.created_at = place_.updated_at = date_
        to_dict = {
            'id': '777777',
            '__class__': 'Place',
            'created_at': date_.isoformat(),
            'updated_at': date_.isoformat(),
        }
        self.assertDictEqual(place_.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        place_ = Place()
        self.assertNotEqual(place_.to_dict(), place_.__dict__)

    def test_to_dict_with_arg(self):
        place_ = Place()
        with self.assertRaises(TypeError):
            place_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
