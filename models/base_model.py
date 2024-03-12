#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
        def __init__(self, *args, **kwargs):
            if not kwargs:
                self.id = str(uuid.uuid4())
                self.create_at = datetime.now()
                self.update_at = datetime.now()

            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'update_at' or key == 'create_at':
                    self.__dict__[key] == datetime.strptime
                    self.__dict__[key] == datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                self.__dict__[key] = value

        def __str__(self):
            return(f"{[self.__class__.__name__]},{(self.id)},{self.__dict__}")

        def save(self):
            self.update_at = datetime.now()
            
        def to_dict(self):
            self.create_at = self.create_at.isoformat()
            self.update_at = self.update_at.isoformat()
            
            self.__dict__.__setitem__('__class__', self.__class__.__name__)
            return dict(self.__dict__)
