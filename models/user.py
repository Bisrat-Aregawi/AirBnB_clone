#!/usr/bin/python3
from base_model import BaseModel


class User(BaseModel):
    """this is the user class that inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
