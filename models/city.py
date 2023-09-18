#!/usr/bin/python3
""" City Module for HBNB project """
from os import environ

from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.state import State


class City(BaseModel):
    """ The city class, contains state ID and name """
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
