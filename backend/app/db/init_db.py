from backend.app.db.database import Base, engine
from backend.app.modules import User, Role


def init():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print(" Tablas creadas correctamente.")


if __name__ == "__main__":
    init()
