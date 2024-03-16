#!/usr/bin/python3
"""Module for a review"""


from models.base_model import BaseModel


class Review(BaseModels):
    """Representation of review of all
    previous classes"""
    place_id = ""
    user_id = ""
    text = ""