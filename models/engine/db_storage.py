#!/usr/bin/python3
"""DB storage module
"""

from os import getenv

from sqlalchemy import create_engine
from models.base_model import Base

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """database storage for mysql conversion
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializer"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = getenv("HBNB_ENV")
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """list all instances of cls
        """
        result = {}
        if cls:
            for row in self.__session.query(cls).all():
                key = f"{cls.__name__}.{row.id}"
                # row.to_dict()
                result.update({key: row})
        else:
            from models.city import City
            from models.review import Review
            from models.state import State
            from models.user import User
            from models.place import Place
            from models.amenity import Amenity
            classes_dict = {"states": State, "cities": City,
                            "users": User, "places": Place,
                            "reviews": Review, "amenities": Amenity}
            for table in classes_dict:
                cls = classes_dict[table]
                for row in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{row.id}"
                    # row.to_dict()
                    result.update({key: row})
        return result
