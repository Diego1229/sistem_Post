from sqlalchemy.orm import Session
from .models import Pais,  Ciudad, Sede
from .schemas import PaisCreate,PaisUpdate, CiudadCreate, CiudadUpdate, SedeCreate, SedeUpdate

#------------PAISES------------------------------------------------------------------------------------------------------------------------       

class PaisCrud:
    def __init__(self, db: Session):
        self.db = db

    def get(self, pais_id: int) -> Pais | None:
        return self.db.query(Pais).filter(Pais.id == pais_id).first()
    
    def get_all(self):
        return self.db.query(Pais).all()
    
    def create(self, pais_data: PaisCreate):
        pais = Pais(**pais_data.dict())
        self.db.add(pais)
        self.db.commit()
        self.db.refresh(pais)
        return pais
        
    def update(self, pais: Pais, pais_data: PaisUpdate):
        for field, value in pais_data.dict(exclude_unset=True).items():
            setattr(pais, field, value)
        self.db.commit()
        self.db.refresh(pais)
        return pais

    def delete(self, pais: Pais):
        self.db.delete(pais)
        self.db.commit()


#------------CIUDADES------------------------------------------------------------------------------------------------------------------------       

class CiudadCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def get(self, ciudad_id: int) -> Ciudad | None:
        return self.db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()

    def get_all(self):
        return self.db.query(Ciudad).all()
    
    def create(self, ciudad_data: CiudadCreate):
        ciudad = Ciudad(**ciudad_data.dict())
        self.db.add(ciudad)
        self.db.commit()
        self.db.refresh(ciudad)
        return ciudad
        
    def update(self, ciudad: Ciudad, ciudad_data: CiudadUpdate):
        for field, value in ciudad_data.dict(exclude_unset=True).items():
            setattr(ciudad, field, value)
        self.db.commit()
        self.db.refresh(ciudad)
        return ciudad

    def delete(self, ciudad: Ciudad):
        self.db.delete(ciudad)
        self.db.commit()


#------------SEDES------------------------------------------------------------------------------------------------------------------------       

class SedeCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def get(self, sede_id: int) -> Sede | None:
        return self.db.query(Sede).filter(Sede.id == sede_id).first()

    def get_all(self):
        return self.db.query(Sede).all()
    
    def create(self, sede_data: SedeCreate):
        sede = Sede(**sede_data.dict())
        self.db.add(sede)
        self.db.commit()
        self.db.refresh(sede)
        return sede
        
    def update(self, sede: Sede, sede_data: SedeUpdate):
        for field, value in sede_data.dict(exclude_unset=True).items():
            setattr(sede, field, value)
        self.db.commit()
        self.db.refresh(sede)
        return sede

    def delete(self, sede: Sede):
        self.db.delete(sede)
        self.db.commit()
