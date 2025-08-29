from sqlalchemy.orm import Session
from .import Role_Crud, Rol_Schemas, Rol_Models
from fastapi import HTTPException, status


# Crear un rol con validación de duplicado
def create_role_service(db: Session, role: Rol_Schemas.RoleCreate):
    existing_role = db.query(Rol_Models.Role).filter(
        Rol_Models.Role.name == role.name).first()
    if existing_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol '{role.name}' ya existe."
        )
    return Role_Crud.create_rol(db, role)


# Listar todos los roles

def get_roles_service(db: Session):
    return Role_Crud.get_roles(db)


# listar solo rol por el id

def get_role_service(db: Session, role_id: int):
    role = Role_Crud.get_role(db, role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El rol con id {role_id} no existe"
        )
    return role

# Eliminar un rol


def delete_role_service(db: Session, role_id: int):
    deleted = Role_Crud.delete_role(db, role_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return deleted
