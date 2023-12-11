#!usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represent the base model.
    Represents the "base" for all other classes in AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Base.
        Args:
            *args: as many arguments.
            **kwargs: key/pair value arguments.
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, fmt)
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return the print/str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """updates the current datetime after changes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values"""
        ndict = self.__dict__.copy()
        ndict.update({"created_at": self.created_at.isoformat()})
        ndict.update({"updated_at": self.updated_at.isoformat()})
        ndict.update({"__class__": self.__class__.__name__})
        return (ndict)
