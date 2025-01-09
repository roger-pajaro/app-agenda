from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass

Base = declarative_base()

@dataclass
class Usuario(Base):
    id: int
    nombre: str
    apellidos: str
    email: str
    password: str
    
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos},"\
               f" email={self.email}, password={self.password})"

@dataclass    
class Contacto(Base):
    id: int  # Cambié el tipo de `id` a `int` porque es la clave primaria
    nombre: str
    apellidos: str
    direccion: str
    email: str
    telefono: str
    fechaCreacion: datetime
    
    __tablename__ = 'contacto'
    id = Column(Integer, primary_key=True)  # Cambié el tipo de `id` a `Integer`
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaCreacion = Column(DateTime, default=datetime.utcnow)  # Usando `utcnow`
    
    def __repr__(self):
        return f"<Contacto(id={self.id}, nombre={self.nombre}, apellidos={self.apellidos}, "\
               f"direccion={self.direccion}, email={self.email}, telefono={self.telefono}, fechaCreacion={self.fechaCreacion})"

@dataclass        
class Pertenece(Base):
    id: int
    id_usuario: int
    id_contacto: int 
    
    __tablename__ = 'pertenece'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)  # Referencia a Usuario
    id_contacto = Column(Integer, ForeignKey('contacto.id'), nullable=False)  # Referencia a Contacto
