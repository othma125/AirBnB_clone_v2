# #!/usr/bin/python3
# """This is the amenity module."""
# from os import environ
#
#
# from models.base_model import BaseModel
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
# from models.place import place_amenity
#
#
# class Amenity(BaseModel):
#     """ Amenity Class """
#
#     if environ.get("HBNB_TYPE_STORAGE") == "db":
#         __tablename__ = "amenities"
#         name = Column(String(128), nullable=False)
#         place_amenities = relationship(
#             "Place",
#             secondary=place_amenity, back_populates="amenities")
#     else:
#         name = ""
