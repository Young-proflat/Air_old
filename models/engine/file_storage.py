#!/usr/bin/python3
"""Module for filestorage class."""
import datetime
import json
import os


class FileStorage:
    """class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file1:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, file1)

    def classes(self):
        """return a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        classes = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}
        return classes

    def reload(self):
        """reloads the stored object"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file2:
            obj_dict = json.load(file2)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Return the valid attributes and their types for classname"""
        attributes = {
                "BaseModel":
                        {"id": str,
                         "created_at": datetime.datetime,
                         "updated_at": datetime.datetime},
                "User":
                        {"email": str,
                         "password": str,
                         "first_name": str,
                         "last_name": str}
                "State":
                        {"name": str},

                "City":
                        {"state_id": str,
                         "name": str},

                "Amenity":
                        {"name": str},

                "Place":
                        {"city_id": str,
                         "user_id": str,
                         "name": str,
                         "description": str,
                         "number_rooms": int,
                         "max_guest": int,
                         "price_by_night": int,
                         "latitude": float,
                         "longitude": float,
                         "amenity_ids":list},

                "Review":
                        {"Place_id": str,
                         "user_id": str,
                         "text":str}
        }
        return attributes
                         
