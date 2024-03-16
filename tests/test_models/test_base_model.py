#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):

    def test_do_save(self):
        instance = BaseModel()
        instance.save()
        self.assertIsNotNone(instance.updated_at)

if __name__ == '__main__':
    unittest.main()