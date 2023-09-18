#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models


class Amenity(BaseModel, models.Base):
    name = ""
