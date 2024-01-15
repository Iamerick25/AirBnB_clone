#!/user_r/bin/python3
"""
Module for User class
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the User class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_Users_unique_ids(self):
        user_1 = User()
        user_2 = User()
        self.assertNotEqual(user_1.id, user_2.id)

    def test_two_Users_different_created_at(self):
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertLess(user_1.created_at, user_2.created_at)

    def test_two_Users_different_updated_at(self):
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertLess(user_1.updated_at, user_2.updated_at)

    def test_str_representation(self):
        date_ = datetime.today()
        date_rep = repr(date_)
        user_1 = User()
        user_1.id = "777777"
        user_1.created_at = User_1.updated_at = date_
        user_1_str = user_1.__str__()
        self.assertIn("[User] (777777)", user_1_str)
        self.assertIn("'id': '777777'", user_1_str)
        self.assertIn("'created_at': " + date_rep, user_1_str)
        self.assertIn("'updated_at': " + date_rep, User_1_str)

    def test_args_unuser_ed(self):
        user_1 = User(None)
        self.assertNotIn(None, user_1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_ = datetime.today()
        date_iso = date_.isoformat()
        user_1 = User(id="777", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(user_1.id, "777")
        self.assertEqual(user_1.created_at, date_)
        self.assertEqual(user_1.updated_at, date_)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user_ = User()
        sleep(0.05)
        first_updated_at = user_.updated_at
        user_.save()
        self.assertLess(first_updated_at, user_.updated_at)

    def test_two_saves(self):
        user_ = User()
        sleep(0.05)
        first_updated_at = user_.updated_at
        user_.save()
        second_updated_at = user_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user_.save()
        self.assertLess(second_updated_at, user_.updated_at)

    def test_save_with_arg(self):
        user_ = User()
        with self.assertRaises(TypeError):
            user_.save(None)

    def test_save_updates_file(self):
        user_ = User()
        user_.save()
        user_id = "User." + user_.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user_ = User()
        self.assertIn("id", user_.to_dict())
        self.assertIn("created_at", user_.to_dict())
        self.assertIn("updated_at", user_.to_dict())
        self.assertIn("__class__", user_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user_ = User()
        user_.middle_name = "Holberton"
        user_.my_number = 98
        self.assertEqual("Holberton", user_.middle_name)
        self.assertIn("my_number", user_.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user_ = User()
        user_dict = user_.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        date_ = datetime.today()
        user_ = User()
        user_.id = "777777"
        user_.created_at = user_.updated_at = date_
        tdict = {
            'id': '777777',
            '__class__': 'User',
            'created_at': date_.isoformat(),
            'updated_at': date_.isoformat(),
        }
        self.assertDictEqual(user_.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        user_ = User()
        self.assertNotEqual(user_.to_dict(), user_.__dict__)

    def test_to_dict_with_arg(self):
        user_ = User()
        with self.assertRaises(TypeError):
            user_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
