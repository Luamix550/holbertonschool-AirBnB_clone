#!/usr/bin/python3
"""Module that represent amenities"""


from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """Representation of Amenity"""
    name = ""