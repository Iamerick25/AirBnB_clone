#!/usr/bin/python3
"""
Module for testing Review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Review class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        review_ = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review_))
        self.assertNotIn("place_id", review_.__dict__)

    def test_user_id_is_public_class_attribute(self):
        review_ = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review_))
        self.assertNotIn("user_id", review_.__dict__)

    def test_text_is_public_class_attribute(self):
        review_ = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review_))
        self.assertNotIn("text", review_.__dict__)

    def test_two_reviews_unique_ids(self):
        review_1 = Review()
        review_2 = Review()
        self.assertNotEqual(review_1.id, review_2.id)

    def test_two_reviews_different_created_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.created_at, review_2.created_at)

    def test_two_reviews_different_updated_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.updated_at, review_2.updated_at)

    def test_str_representation(self):
        date_ = datetime.today()
        date_rep = repr(date_)
        review_ = Review()
        review_.id = "777777"
        review.created_at = review_.updated_at = date_
        review_str = review.__str__()
        self.assertIn("[Review] (777777)", review_str)
        self.assertIn("'id': '777777'", review_str)
        self.assertIn("'created_at': " + date_rep, review_str)
        self.assertIn("'updated_at': " + date_rep, review_str)

    def test_args_unused(self):
        review_ = Review(None)
        self.assertNotIn(None, review_.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_ = datetime.today()
        date_iso = date_.isoformat()
        review_ = Review(id="777", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(review_.id, "777")
        self.assertEqual(review_.created_at, date_)
        self.assertEqual(review_.updated_at, date_)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    Unittests for testing save method of the Review class.
    """

    @classmethod
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
        review_ = Review()
        sleep(0.05)
        first_updated_at = review_.updated_at
        review_.save()
        self.assertLess(first_updated_at, review_.updated_at)

    def test_two_saves(self):
        review_ = Review()
        sleep(0.05)
        first_updated_at = review_.updated_at
        review_.save()
        second_updated_at = review_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review_.save()
        self.assertLess(second_updated_at, review_.updated_at)

    def test_save_with_arg(self):
        review_ = Review()
        with self.assertRaises(TypeError):
            review_.save(None)

    def test_save_updates_file(self):
        review_ = Review()
        review_.save()
        review_id = "Review." + review_.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        review_ = Review()
        self.assertIn("id", review_.to_dict())
        self.assertIn("created_at", review_.to_dict())
        self.assertIn("updated_at", review_.to_dict())
        self.assertIn("__class__", review_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        review_ = Review()
        review_.middle_name = "Johnson"
        review_.my_number = 777
        self.assertEqual("Johnson", review_.middle_name)
        self.assertIn("my_number", review_.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        review_ = Review()
        review_dict = review_.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        date_ = datetime.today()
        review_ = Review()
        review_.id = "777777"
        review_.created_at = review_.updated_at = date_
        to_dict = {
            'id': '777777',
            '__class__': 'Review',
            'created_at': date_.isoformat(),
            'updated_at': date_.isoformat(),
        }
        self.assertDictEqual(review_.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        review_ = Review()
        self.assertNotEqual(review_.to_dict(), review_.__dict__)

    def test_to_dict_with_arg(self):
        review_ = Review()
        with self.assertRaises(TypeError):
            review_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
