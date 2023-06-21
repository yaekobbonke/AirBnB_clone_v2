#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models import base_model
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, metadata
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128))
    password = Column(String(128))
    first_name = Column(128)
    last_name = Column(128)
    places = relationship(Place, backref='User', cascade='delete')


Base.metadata.create_all(engine)
