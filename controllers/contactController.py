from db import conectar
from models import Contacto, Pertenece

def seleccionar_contactos(id_usuario, campo, orden):
    if not id_usuario or not isinstance(id_usuario, int):
        raise ValueError("El parámetro id_usuario debe ser un número entero válido")

    contactos = []
    try:
        session = conectar()
        query = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario)

        if campo == "ID" and orden == "ASC":
            contactos = query.order_by(Contacto.id).all()
        elif campo == "ID" and orden == "DESC":
            contactos = query.order_by(Contacto.id.desc()).all()
        elif campo == "NOMBRE" and orden == "ASC":
            contactos = query.order_by(Contacto.nombre).all()
        elif campo == "NOMBRE" and orden == "DESC":
            contactos = query.order_by(Contacto.nombre.desc()).all()
    except Exception as e:
        print(f"Error al seleccionar contactos: {e}")
    finally:
        session.close()
    return contactos

def seleccionar_contacto(id):
    if not id or not isinstance(id, int):
        raise ValueError("El parámetro id debe ser un número entero válido")
    try:
        session = conectar()
        contacto = session.query(Contacto).filter(Contacto.id == id).first()
        if not contacto:
            raise ValueError(f"No se encontró contacto con id {id}")
    except Exception as e:
        print(f"Error al seleccionar contacto: {e}")
        return None
    finally:
        session.close()
    return contacto

def busqueda_contactos(id_usuario, value):
    if not id_usuario or not isinstance(id_usuario, int):
        raise ValueError("El parámetro id_usuario debe ser un número entero válido")

    contactos = []
    try:
        session = conectar()
        contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(
            Pertenece.id_usuario == id_usuario,
            (Contacto.nombre.ilike(f'%{value}%')) | 
            (Contacto.apellidos.ilike(f'%{value}%')) | 
            (Contacto.email.ilike(f'%{value}%'))
        ).order_by(Contacto.nombre).all()
    except Exception as e:
        print(f"Error en la búsqueda de contactos: {e}")
    finally:
        session.close()
    return contactos

def insertar_contacto(id_usuario, nombre, apellidos, direccion, email, telefono):
    if not id_usuario or not isinstance(id_usuario, int):
        raise ValueError("El parámetro id_usuario debe ser un número entero válido")

    try:
        contacto = Contacto(
            nombre=nombre,
            apellidos=apellidos,
            direccion=direccion,
            email=email,
            telefono=telefono
        )
        session = conectar()
        session.add(contacto)
        session.commit()

        session.refresh(contacto)
        id_contacto = contacto.id

        pertenece = Pertenece(
            id_usuario=id_usuario,
            id_contacto=id_contacto
        )

        session.add(pertenece)
        session.commit()
    except Exception as e:
        print(f"Error al insertar contacto: {e}")
        return False
    finally:
        session.close()
    return True

def actualizar_contacto(id, nombre, apellidos, direccion, email, telefono):
    if not id or not isinstance(id, int):
        raise ValueError("El parámetro id debe ser un número entero válido")

    try:
        session = conectar()
        contacto = session.query(Contacto).get(id)
        if not contacto:
            raise ValueError(f"No se encontró contacto con id {id}")

        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono

        session.add(contacto)
        session.commit()
    except Exception as e:
        print(f"Error al actualizar contacto: {e}")
        return False
    finally:
        session.close()
    return True

def eliminar_contacto(id_usuario, id_contacto):
    if not id_usuario or not isinstance(id_usuario, int):
        raise ValueError("El parámetro id_usuario debe ser un número entero válido")
    if not id_contacto or not isinstance(id_contacto, int):
        raise ValueError("El parámetro id_contacto debe ser un número entero válido")

    try:
        session = conectar()
        session.query(Pertenece).filter(
            Pertenece.id_contacto == id_contacto,
            Pertenece.id_usuario == id_usuario
        ).delete()

        contacto = session.query(Contacto).get(id_contacto)
        if contacto:
            session.delete(contacto)
            session.commit()
    except Exception as e:
        print(f"Error al eliminar contacto: {e}")
        return False
    finally:
        session.close()
    return True
