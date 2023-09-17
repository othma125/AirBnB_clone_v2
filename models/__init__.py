#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

storage = DBStorage() if storage_engine == 'db' else FileStorage()
storage.reload()
