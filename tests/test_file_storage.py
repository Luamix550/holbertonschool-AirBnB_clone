import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os
import json


class TestFileStorage(unittest.TestCase):
    """ This class testing fileStorage """
    def setUp(self):
        """Preparar el entorno antes de cada prueba"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the environment after each test"""
        del self.storage

    def testFilePath(self):
        """Test to check the file path"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test__objects(self):
        """Test to verify the __objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_all(self):
        """Test to verify the all() method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test to verify the new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test to verify the save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        key = f"{obj.__class__.__name__}.{obj.id}"
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn(key, content)

    @patch('builtins.input', side_effect=["BaseModel"])
    def test_reload(self, mock_input):
        """Test to verify the reload() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
