from sqlalchemy.orm import Session
from .Rol_Models import Role
from .Rol_Schemas import RoleCreate, RoleUpdate

# Crear rol


def create_rol(db: Session, role: RoleCreate):
    db_role = Role(
        name=role.name,
        description=role.description,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# Listar roles
def get_roles(db: Session):
    return db.query(Role).all()


# listar por id

def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()


# actualizar rol


def update_role(db: Session, role_id: int, role: RoleUpdate):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return None

    # Tomamos solo los campos que el usuario envió
    update_data = role.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)
    return db_role


# eliminarlo
def delete_role(db: Session, role_id: int):
    db_role = db.get(Role, role_id)  # busca directo por primary key
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
