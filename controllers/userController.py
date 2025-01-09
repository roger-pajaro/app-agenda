from db import conectar
from models import Usuario
from sqlalchemy.exc import SQLAlchemyError

def seleccionarUsuario(email, password):
    id = 0
    session = None
    try:
        session = conectar()
        
        # Si no se pudo establecer la conexión, retornamos id=0
        if session is None:
            print("No se pudo conectar a la base de datos.")
            return id
        
        # Realizar la consulta
        usuarios = session.query(Usuario).filter(Usuario.email == email, Usuario.password == password).all()
        
        # Si el usuario existe, obtenemos el id
        if usuarios:
            id = usuarios[0].id
    except SQLAlchemyError as e:
        # Manejo específico para errores de SQLAlchemy
        print(f"Error de SQLAlchemy: {e}")
    except Exception as e:
        # Manejo de otros errores generales
        print(f"Error al seleccionar usuario: {e}")
    finally:
        # Cerrar la sesión si fue abierta correctamente
        if session:
            session.close()
    
    return id
