#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
        def __init__(self, *args, **kwargs):
            if not kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            else:
                for key, value in kwargs.items():
                    if key == 'updated_at' or key == 'created_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

        def __str__(self):
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            self.updated_at = datetime.now()

        def to_dict(self):
            new_dict = self.__dict__.copy()
            new_dict['__class__'] = self.__class__.__name__
            new_dict['created_at'] = self.created_at.isoformat()
            new_dict['updated_at'] = self.updated_at.isoformat()
            return new_dict
