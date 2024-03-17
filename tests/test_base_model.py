#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class testBaseModel(unittest.TestCase):

    def test_save(self):
        instance = BaseModel()
        instance.save()
        self.assertIsNotNone(instance.updated_at)

    def test_to_dict(self):
        """Testing to_dict method creatin a directory
        from the instance atributtes and checking if
        it is the desired result"""
        instance = BaseModel()
        instance.id = '123'
        instance.__class__ = 'Luis'
        instance.created_at = datetime(2024, 3, 3)
        instance.updated_at = datetime(2024, 3, 3)

        actual_result = instance.to_dict()

        desired_result = {
            'id': '123'
            '__class__': 'Luis'
            'created_at': '2024, 3, 3'
            'updated_at': '2024, 3, 3'
        }

        self.assertEqual(actual_result, desired_result)


if __name__ == '__main__':
    unittest.main()