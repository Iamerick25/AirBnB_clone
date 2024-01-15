#!/usr/bin/python3
"""
Module for State unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the State class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        state_ = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state_.__dict__)

    def test_two_states_unique_ids(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def test_two_states_different_created_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.created_at, state_2.created_at)

    def test_two_states_different_updated_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.updated_at, state_2.updated_at)

    def test_str_representation(self):
        date_ = datetime.today()
        date_rep = repr(date_)
        state_ = State()
        state_id = "777777"
        state_.created_at = state.updated_at = date_
        state_str = state_.__str__()
        self.assertIn("[State] (777777)", state_str)
        self.assertIn("'id': '777777'", state_str)
        self.assertIn("'created_at': " + date_rep, state_str)
        self.assertIn("'updated_at': " + date_rep, state_str)

    def test_args_unused(self):
        state_ = State(None)
        self.assertNotIn(None, state_.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_ = datetime.today()
        date__iso = date_.isoformat()
        state_ = State(id="345", created_at=date__iso, updated_at=date__iso)
        self.assertEqual(state_id, "345")
        self.assertEqual(state_.created_at, date_)
        self.assertEqual(state_.updated_at, date_)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """
    Unittests for testing save method of the State class.
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
        state_ = State()
        sleep(0.05)
        first_updated_at = state_.updated_at
        state_.save()
        self.assertLess(first_updated_at, state_.updated_at)

    def test_two_saves(self):
        state_ = State()
        sleep(0.05)
        first_updated_at = state_.updated_at
        state_.save()
        second_updated_at = state_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        state_.save()
        self.assertLess(second_updated_at, state_.updated_at)

    def test_save_with_arg(self):
        state_ = State()
        with self.assertRaises(TypeError):
            state_.save(None)

    def test_save_updates_file(self):
        state_ = State()
        state_.save()
        state_id = "State." + state_id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class TestState_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the State class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        state_ = State()
        self.assertIn("id", state_.to_dict())
        self.assertIn("created_at", state_.to_dict())
        self.assertIn("updated_at", state_.to_dict())
        self.assertIn("__class__", state_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        state_ = State()
        state_.middle_name = "Johnson"
        state_.my_number = 777
        self.assertEqual("Johnson", state_.middle_name)
        self.assertIn("my_number", state_.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        state_ = State()
        state_dict = state.to_dict()
        self.assertEqual(str, type(state_dict["id"]))
        self.assertEqual(str, type(state_dict["created_at"]))
        self.assertEqual(str, type(state_dict["updated_at"]))

    def test_to_dict_output(self):
        date_ = datetime.today()
        state_ = State()
        state_id = "777777"
        state_.created_at = state_.updated_at = date_
        tdict = {
            'id': '777777',
            '__class__': 'State',
            'created_at': date_.isoformat(),
            'updated_at': date_.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        state_ = State()
        self.assertNotEqual(state.to_dict(), state_.__dict__)

    def test_to_dict_with_arg(self):
        state_ = State()
        with self.assertRaises(TypeError):
            state_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
