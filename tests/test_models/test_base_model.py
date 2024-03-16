#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):

    def test_save(self):
        instance = BaseModel()
        instance.save()
        self.assertIsNotNone(instance.updated_at)
        
    def test_dict(self):
    
    
    

if __name__ == '__main__':
    unittest.main()