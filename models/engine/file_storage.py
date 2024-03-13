#!/usr/bin/python3
import json
import os

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__} {obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as write_file:
            json.dump(self.__objects,write_file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as read_file:
                data = json.load(read_file)
