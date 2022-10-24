import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    user_name = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_characters = Column(Integer, ForeignKey('characters.id'))
    characters = relationship('Characters')
    id_planets = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')
    id_vehicles = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship('Vehicles')
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    heigth = Column(Integer)
    hair_color = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    eyes_color = Column(String(50), nullable=False)
    skin_color = Column(String(50))
    birth_year = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    diameter = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100))
    crew = Column(Integer)
    length = Column(Integer)
    passengers = Column(Integer)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')