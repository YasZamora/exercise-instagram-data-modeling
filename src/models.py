import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

tabla_Posts_favoritos = Table('posts_favoritos', Base.metadata,
    Column('usuarios', ForeignKey('usuarios'), primary_key=True),
    Column('posts', ForeignKey('posts'), primary_key=True)
)      

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mail = Column(String(50), nullable=False, unique =True)
    contrasena = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    amigos = relationship('amigos')
    comentarios = relationship('comentarios')
    posts = relationship('posts', secondary=tabla_Posts_favoritos)

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    descripción = Column(String(250), nullable=True)
    crated_at = Column(DateTime(), default=datetime.now())
    post_code = Column(String(250), nullable=False)
    comentarios = relationship('comentarios')

class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    descripción = Column(String(250), nullable=True)
    crated_at = Column(DateTime(), default=datetime.now())
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)    
    posts_id = Column(Integer, ForeignKey('posts.id'))

class Amigos(Base):
    __tablename__ = 'amigos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)


    def to_dict(self):
        return {}
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e