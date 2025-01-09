from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://agendadb:iftpt8WFitmuUjXTjRy534bn4wPueGwJ@dpg-ctust3lds78s738k7vig-a.oregon-postgres.render.com/agenda"


def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()
    
    if s != None:
        print("Conexion a base de datos OK")
    else:
        print("Error en conexion a base de datos")   
        
        
    return s