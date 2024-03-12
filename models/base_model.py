#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
        def __init__(self, *args, **kwargs):
            if not kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, value)
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

        def __str__(self):
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            self.updated_at = datetime.now()

        def to_dict(self):
            self.created_at = self.created_at.isoformat()
            self.updated_at = self.updated_at.isoformat()

            self.__dict__.__setitem__('__class__', self.__class__.__name__)
            return self.__dict__
