#!/usr/bin/python3
"""User module that represent an user"""


from models.base_model import BaseModel


class User(BaseModel):
    """Since BaseModel already handles the initialization
    of attributes and serialization to JSON, we don't need
    to override the __init__ method."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
