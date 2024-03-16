#!/usr/bin/python3
from models.engine.file_storage import FileStorage
import unittest

class testFileStorage(unittest.TestCase):
    """ This class testing fileStorage """
    def test_file_path(self):
        """Method to test if the file_path method from
        file_storage module is actually working in order
        to succesfully create this file"""
        instance = FileStorage()
        desired_result = instance.save()
        self.assertTrue(hasattr(desired_result, __file_path))
