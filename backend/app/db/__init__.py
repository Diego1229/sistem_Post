from app.db.database import Base, engine

def init():
    print("Creando tablas en la base de datos...")
    from app.modules.Users import models
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")
