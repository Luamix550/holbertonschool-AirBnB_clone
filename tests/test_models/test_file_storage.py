#!/usr/bin/python3
from models.engine.file_storage import FileStorage
import unittest

class test_FileStorage(unittest.TestCase):
    """ This class testing fileStorage """
    def test_file_path(self):
        """Method to test if the file_path method from
        file_storage module is actually working in order
        to succesfully create this file"""
        instance = FileStorage()
        desired_file_path = "file.json"
        self.assertFalse(hasattr(instance, '__file_path'))
        instance.save()
        self.assertTrue(hasattr(instance, '__file_path' ))
        self.assertEqual(instance.__file_path, desired_file_path)
