#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from sqlalchemy.orm import declarative_base
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")
Base = declarative_base() if storage_engine == 'db' else object

storage = DBStorage() if storage_engine == 'db' else FileStorage()
storage.reload()
