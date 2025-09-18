#!/usr/bin/python3
"""
FileStorage: serializes instances to JSON and deserializes back.
"""

import json


class FileStorage:
    """Serializes instances to JSON and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add new object to __objects."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize JSON file back to __objects."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

