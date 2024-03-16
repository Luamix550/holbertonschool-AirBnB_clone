#!/usr/bin/python3
""" This class provides  a state.  """

from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """Name of the state. """
    name = ""
