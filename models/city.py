#!/usr/bin/python3
"""Class module for the city."""

from models.base_model import BaseModel


class City(BaseModel):
    """Clas City that inherits from BaseModel."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        