#!/usr/bin/python3
"""defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent an amenity.

    attributes:
        name (str)-  The name of the amenity.
    """

    name = ""
