import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFileStorage(unittest.TestCase):
    """ This class testing fileStorage """
    def setUp(self):
        """Preparar el entorno antes de cada prueba"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Limpiar el entorno después de cada prueba"""
        del self.storage

    def test_file_path(self):
        """Method to test if the file_path method from
        file_storage module is actually working in order
        to succesfully create this file"""
        instance = FileStorage()
        desired_file_path = "file.json"
        instance.save()
        self.assertTrue(hasattr(instance, '__file_path'))
        self.assertEqual(instance._FileStorage__file_path, desired_file_path)

    def test__objects(self):
        """Test para verificar el atributo __objects"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_all(self):
        """Test para verificar el método all()"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test para verificar el método new()"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test para verificar el método save()"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        key = f"{obj.__class__.__name__}.{obj.id}"
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn(key, content)

    @patch('builtins.input', side_effect=["BaseModel"])
    def test_reload(self, mock_input):
        """Test para verificar el método reload()"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
