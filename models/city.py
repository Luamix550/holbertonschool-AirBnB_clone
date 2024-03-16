#!/usr/bin/python3
"""Module that represent a city """


from models.base_model import BaseModel


class City(BaseModel):
    """Representation of a city"""
    state_id = ""
    name = ""