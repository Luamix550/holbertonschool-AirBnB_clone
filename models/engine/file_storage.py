#!/usr/bin/python3
"""This module is the file storage class"""


import json


class FileStorage:
    """FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        self.save()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.amenity import Amenity
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    from models.base_model import BaseModel
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
