from db import conectar
from models import Contacto, Pertenece


def seleccionar_contactos(id_usuario,campo,orden):
    try:
        session = conectar()
        
        if campo == "ID" and orden == "ASC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all()
        elif campo == "NOMBRE" and orden == "ASC": 
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()
        elif campo == "NOMBRE" and orden == "DESC": 
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()
    except Exception as e:
        print(e)
    finally:
        session.close()
        
    return contactos

def seleccionar_contacto(id):
    try:
        session = conectar()
        contacto = session.query(Contacto).filter(Contacto.id == id).all()[0]
    except Exception as e:
        print(e)
    finally:
        session.close()
    return contacto


def busqueda_contactos(id_usuario,value):
    try:
        session = conectar()
        contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto ).filter(Pertenece.id_usuario == id_usuario).filter((Contacto.nombre.ilike('%'+value+'%')) | (Contacto.apellidos.ilike('%'+value+'%')) | (Contacto.nombre.ilike('%'+value+'%')) | (Contacto.email.ilike('%'+value+'%'))).order_by(Contacto.nombre).all()
    except Exception as e:
        print(e)
    finally:
        session.close()   
    return contactos     


def insertar_contacto(id_usuario,nombre,apellidos,direccion,email,telefono):
    try:
        contacto = Contacto(
            nombre = nombre,
            apellidos = apellidos,
            direccion = direccion,
            email = email,
            telefono = telefono
        )
        session = conectar()
        session.add(contacto)
        session.commit()
        
        session.refresh(contacto)
        id_contacto = contacto.id
        
        pertenece = Pertenece(
            id_usuario = id_usuario,
            id_contacto = id_contacto
        )
        
        session.add(pertenece)
        session.commit()
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
        return True
    
    
def actualizar_contacto(id,nombre,apellidos,direccion,email,telefono):
    try:
        session = conectar()
        contacto = session.query(Contacto).get(id)
        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono
        
        session.add(contacto)
        session.commit()
        
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
        return True
    

def eliminar_contacto(id_usuario,id_contacto):
    try:
        session = conectar()
        session.query(Pertenece).filter(Pertenece.id_contacto == id_contacto).filter(Pertenece.id_usuario == id_usuario).delete()
        contacto = session.query(Contacto).get(id_contacto)
        session.delete(contacto)
        session.commit()
        
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
        return True
        
        