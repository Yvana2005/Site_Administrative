# from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class User(Base):
#     __tablename__= 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

# class Work(Base):
#     __tablename__= 'works'
#     id = Column(Integer, primary_key=True, index=True)
#     name_work = Column(String)

from sqlalchemy import Column, Integer, String, DATE, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    forename = Column(String)
    num_TelUser = Column(Integer)
    dtecreatedUser = Column(DATE)
    hashed_password = Column(String)

class Ordre(Base):
    __tablename__ = 'ordre'

    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, ForeignKey('users.id'))
    users = relationship('User', backref='ordre')
    StatutOrdre = Column(String)

class Paiement(Base):
    __tablename__ = 'paiement'

    id = Column(Integer, primary_key=True)
    date_paiement = Column(DATE)
    montant = Column(Float)

class Piece_Jointe(Base):
    __tablename__='piece_jointe'

    id = Column(Integer, primary_key=True)
    nom_pj = Column(DATE)
 