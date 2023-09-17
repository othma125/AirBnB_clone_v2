#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from base_model import Base
from os import environ
from sqlalchemy import Column, String
import models

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if storage_engine == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """cities list
        """
        result = []
        for city in models.storage.all(models.city.City).values():
            if city.state_id == self.id:
                result.append(city)
        return result
