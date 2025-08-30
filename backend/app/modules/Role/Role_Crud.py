from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .Rol_Models import Role
from .Rol_Schemas import RoleCreate, RoleUpdate
from typing import Optional, List

# Crea un nuevo rol en la base de datos


def create_rol(db: Session, role: RoleCreate) -> Role:
    try:
        db_role = Role(
            name=role.name,
            description=role.description,
        )
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    except IntegrityError as e:
        db.rollback()
        raise e

# Obtiene una lista de roles, con paginación y opción de filtrar solo los activos


def get_roles(db: Session, skip: int = 0, limit: int = 100, active_only: bool = False) -> List[Role]:
    query = db.query(Role)
    if active_only:
        query = query.filter(Role.is_active == True)
    return query.offset(skip).limit(limit).all()


def get_role(db: Session, role_id: int) -> Optional[Role]:
    return db.query(Role).filter(Role.id == role_id).first()

# Obtiene un rol específico por su ID


def update_role(db: Session, role_id: int, role: RoleUpdate) -> Optional[Role]:
    try:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if not db_role:
            return None
        update_data = role.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role
    except IntegrityError as e:
        db.rollback()
        raise e

# Elimina un rol de la base de datos por su ID


def delete_role(db: Session, role_id: int) -> Optional[Role]:

    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()

    return db_role
