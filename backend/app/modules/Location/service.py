from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .models import Pais, Ciudad, Sede
from .schemas import (
    PaisCreate, PaisUpdate,
    CiudadCreate, CiudadUpdate,
    SedeCreate, SedeUpdate
)
from .crud import PaisCrud, CiudadCrud, SedeCrud


# ------------PAISES------------------------------------------------------------------------------------------------------------------------

class PaisService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = PaisCrud(db)

    def get_pais(self, pais_id: int):
        pais = self.crud.get(pais_id)
        if not pais:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"País con id {pais_id} no encontrado"
            )
        return pais

    def get_all(self):
        return self.crud.get_all()

    def create_pais(self, data: PaisCreate):
        # Validar duplicado por nombre
        existing = self.db.query(Pais).filter(Pais.nombre == data.nombre).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un país con ese nombre"
            )
        return self.crud.create(data)

    def update_pais(self, pais_id: int, data: PaisUpdate):
        pais = self.get_pais(pais_id)
        return self.crud.update(pais, data)

    def delete_pais(self, pais_id: int):
        pais = self.get_pais(pais_id)
        self.crud.delete(pais)
        return {"message": "País eliminado correctamente"}


# ------------CIUDADES------------------------------------------------------------------------------------------------------------------------

class CiudadService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = CiudadCrud(db)
        self.pais_crud = PaisCrud(db)

    def get_ciudad(self, ciudad_id: int):
        ciudad = self.crud.get(ciudad_id)
        if not ciudad:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Ciudad con id {ciudad_id} no encontrada"
            )
        return ciudad

    def get_all(self):
        return self.crud.get_all()

    def create_ciudad(self, data: CiudadCreate):
        # ⚙️ Validar que el país exista antes de crear la ciudad
        pais = self.pais_crud.get(data.pais_id)
        if not pais:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El país con id {data.pais_id} no existe."
            )

        # Validar duplicado por nombre
        existing = self.db.query(Ciudad).filter(Ciudad.nombre == data.nombre).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe una ciudad llamada '{data.nombre}'."
            )

        return self.crud.create(data)

    def update_ciudad(self, ciudad_id: int, data: CiudadUpdate):
        ciudad = self.get_ciudad(ciudad_id)
        return self.crud.update(ciudad, data)

    def delete_ciudad(self, ciudad_id: int):
        ciudad = self.get_ciudad(ciudad_id)
        self.crud.delete(ciudad)
        return {"message": "Ciudad eliminada correctamente"}


# ------------SEDES------------------------------------------------------------------------------------------------------------------------

class SedeService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = SedeCrud(db)
        self.ciudad_crud = CiudadCrud(db)

    def get_sede(self, sede_id: int):
        sede = self.crud.get(sede_id)
        if not sede:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Sede con id {sede_id} no encontrada"
            )
        return sede

    def get_all(self):
        return self.crud.get_all()

    def create_sede(self, data: SedeCreate):
        # ⚙️ Validar que la ciudad exista antes de crear la sede
        ciudad = self.ciudad_crud.get(data.ciudad_id)
        if not ciudad:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"La ciudad con id {data.ciudad_id} no existe."
            )

        # Validar duplicado por nombre o teléfono
        existing = self.db.query(Sede).filter(
            (Sede.nombre == data.nombre) | (Sede.telefono == data.telefono)
        ).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una sede con ese nombre o teléfono"
            )

        return self.crud.create(data)

    def update_sede(self, sede_id: int, data: SedeUpdate):
        sede = self.get_sede(sede_id)
        return self.crud.update(sede, data)

    def delete_sede(self, sede_id: int):
        sede = self.get_sede(sede_id)
        self.crud.delete(sede)
        return {"message": "Sede eliminada correctamente"}
