#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import storage

class BaseModel():
        def __init__(self, *args, **kwargs):
            self.id = str(uuid.uuid4())
            if not kwargs:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                return
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                continue
            self.__dict__[key] = value

        def __str__(self):
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            storage.save()
            storage.new(self)
            self.updated_at = datetime.now()

        def to_dict(self):
            new_dict = self.__dict__.copy()
            new_dict['__class__'] = self.__class__.__name__
            new_dict['created_at'] = self.created_at.isoformat()
            new_dict['updated_at'] = self.updated_at.isoformat()
            return new_dict
