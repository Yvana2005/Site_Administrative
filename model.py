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

from sqlalchemy import Column, Integer, String, DATE, ForeignKey, Float, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    forename = Column(String(50), nullable=False)
    num_TelUser = Column(String(15), nullable=False)
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
    nom_pj = Column(String)

class Destinataire(Base):
    __tablename__='destinataire'

    id = Column(Integer, primary_key=True)
    statut = Column(String)
    nom_destinataire = Column(String)
    prenom_destinataire = Column(String)
    pays_Destinataire = Column(String)
    ville_destinataire = Column(String)
    code_Postale = Column(String)
    num_telephone = Column(String)
    TypActe = Column(String)
    Code_postale = Column(String)
    Adresse_email = Column(String)


class Acte(Base):
    __tablename__ = 'actes'
    id = Column(Integer, primary_key=True)
    typActe = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'acte',
        'polymorphic_on': typActe
    }

class Acte_Naissance(Acte):
    __tablename__ = 'acte_naissance'
    id = Column(Integer, ForeignKey('actes.id'), primary_key=True)
    Date_naissance = Column(DATE)
    nom_naissance = Column(String(50), nullable=False)
    prenom = Column(String(50))
    Pays = Column(String(50))
    commune_naissance = Column(String(50))
    pere_inconnue = Column(Boolean)
    nom_pere = Column(String(50), nullable=False)
    prenom_pere = Column(String(50), nullable=False)
    mere_inconnue = Column(Boolean)
    nom_mere = Column(String(50), nullable=False)
    prenom_mere = Column(String(50), nullable=False)
    nbrecopie = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'acte_naissance',
    }

class Acte_Deces(Acte):
    __tablename__ = 'acte_deces'
    id = Column(Integer, ForeignKey('actes.id'), primary_key=True)
    bark_volume = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'acte_deces',
    }

