#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.state import State


class City(BaseModel, models.Base):
    """ The city class, contains state ID and name """
    if models.storage_engine == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
