#!/usr/bin/python3
""" script indicating Base code """

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """class that would be inherited by other classes"""

    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs is not None and kwargs!={}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation"""
        return "[{}]({}){}".\
            format(type(self).__name__,self.id,self.__dict__)

    def save(self):
        """updated the public instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of the key"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
