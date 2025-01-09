from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URI = "postgresql://agendadb:iftpt8WFitmuUjXTjRy534bn4wPueGwJ@dpg-ctust3lds78s738k7vig-a.oregon-postgres.render.com/agenda"

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)

    try:
        # Intentar establecer una conexión realizando una operación simple
        session = Session()
        session.execute('SELECT 1')  # Simple query to check connection
        print("Conexión a base de datos OK")
        return session
    except OperationalError as e:
        print(f"Error en conexión a base de datos: {e}")
        return None
