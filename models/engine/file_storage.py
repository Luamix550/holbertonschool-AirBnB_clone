#!/usr/bin/python3
import json
import os
"""
Class responsible for managing serialization and deserialization of objects to and from a JSON file.
"""


class FileStorage:

    def __init__(self):
        """
        Initializes the FileStorage class.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns all objects stored in the dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
            obj: Object to add.
        """
        key = f"{obj.__class__.__name__} {obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Saves the serialized objects to the JSON file.
        """
        with open(self.__file_path, "w") as write_file:
            json.dump(self.__objects, write_file)

    def reload(self):
        """
        Reloads serialized objects from the JSON file if it exists.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as read_file:
                data = json.load(read_file)
                self.__objects = data
