from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ...db.database import get_db
from .schemas import (
    PaisCreate, PaisUpdate, PaisResponse,
    CiudadCreate, CiudadUpdate, CiudadResponse,
    SedeCreate, SedeUpdate, SedeResponse
)
from .service import PaisService, CiudadService, SedeService

router = APIRouter(prefix="/api")

# ==========================================================
# ------------------------- PAISES --------------------------
# ==========================================================
@router.get("/paises", response_model=list[PaisResponse], tags=["Pais"])
def list_paises(db: Session = Depends(get_db)):
    service = PaisService(db)
    return service.get_all()


@router.get("/paises/{pais_id}", response_model=PaisResponse, tags=["Pais"])
def get_pais(pais_id: int, db: Session = Depends(get_db)):
    service = PaisService(db)
    return service.get_pais(pais_id)


@router.post("/paises", response_model=PaisResponse, status_code=status.HTTP_201_CREATED, tags=["Pais"])
def create_pais(pais: PaisCreate, db: Session = Depends(get_db)):
    service = PaisService(db)
    return service.create_pais(pais)


@router.put("/paises/{pais_id}", response_model=PaisResponse, tags=["Pais"])
def update_pais(pais_id: int, pais: PaisUpdate, db: Session = Depends(get_db)):
    service = PaisService(db)
    return service.update_pais(pais_id, pais)


@router.delete("/paises/{pais_id}", tags=["Pais"])
def delete_pais(pais_id: int, db: Session = Depends(get_db)):
    service = PaisService(db)
    return service.delete_pais(pais_id)


# ==========================================================
# ------------------------ CIUDADES -------------------------
# ==========================================================
@router.get("/ciudades", response_model=list[CiudadResponse], tags=["Ciudad"])
def list_ciudades(db: Session = Depends(get_db)):
    service = CiudadService(db)
    return service.get_all()


@router.get("/ciudades/{ciudad_id}", response_model=CiudadResponse, tags=["Ciudad"])
def get_ciudad(ciudad_id: int, db: Session = Depends(get_db)):
    service = CiudadService(db)
    return service.get_ciudad(ciudad_id)


@router.post("/ciudades", response_model=CiudadResponse, status_code=status.HTTP_201_CREATED, tags=["Ciudad"])
def create_ciudad(ciudad: CiudadCreate, db: Session = Depends(get_db)):
    service = CiudadService(db)
    return service.create_ciudad(ciudad)


@router.put("/ciudades/{ciudad_id}", response_model=CiudadResponse, tags=["Ciudad"])
def update_ciudad(ciudad_id: int, ciudad: CiudadUpdate, db: Session = Depends(get_db)):
    service = CiudadService(db)
    return service.update_ciudad(ciudad_id, ciudad)


@router.delete("/ciudades/{ciudad_id}", tags=["Ciudad"])
def delete_ciudad(ciudad_id: int, db: Session = Depends(get_db)):
    service = CiudadService(db)
    return service.delete_ciudad(ciudad_id)


# ==========================================================
# -------------------------- SEDES --------------------------
# ==========================================================
@router.get("/sedes", response_model=list[SedeResponse], tags=["Sede"])
def list_sedes(db: Session = Depends(get_db)):
    service = SedeService(db)
    return service.get_all()


@router.get("/sedes/{sede_id}", response_model=SedeResponse, tags=["Sede"])
def get_sede(sede_id: int, db: Session = Depends(get_db)):
    service = SedeService(db)
    return service.get_sede(sede_id)


@router.post("/sedes", response_model=SedeResponse, status_code=status.HTTP_201_CREATED, tags=["Sede"])
def create_sede(sede: SedeCreate, db: Session = Depends(get_db)):
    service = SedeService(db)
    return service.create_sede(sede)


@router.put("/sedes/{sede_id}", response_model=SedeResponse, tags=["Sede"])
def update_sede(sede_id: int, sede: SedeUpdate, db: Session = Depends(get_db)):
    service = SedeService(db)
    return service.update_sede(sede_id, sede)


@router.delete("/sedes/{sede_id}", tags=["Sede"])
def delete_sede(sede_id: int, db: Session = Depends(get_db)):
    service = SedeService(db)
    return service.delete_sede(sede_id)
