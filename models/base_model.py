#!/usr/bin/python3
"""class BaseModel that defines
all common attributes/methods for
other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ class BaseModel that defines all common attributes/methods """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            return
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                self.__dict__[key] = datetime.strptime(
                    value,
                    '%Y-%m-%dT%H:%M:%S.%f'
                )
            else:
                self.__dict__[key] = value

    def __str__(self):
        """Returns a string representation of the instance. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the instance by updating the update date and time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the instance into a serializable dictionary.
        Returns:
            dict: Dictionary containing all the instance attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
