from sqlalchemy.orm import Session
from .models import Rol,  Usuario, UsuarioSede
from .schemas import RolCreate,RolUpdate, UsuarioCreate, UsuarioUpdate, UsuarioSedeCreate, UsuarioSedeUpdate

class RolCrud:
    def __init__(self, db:Session):
        self.db = db

    def get(self, rol_id: int)-> Rol | None:
        return self.db.query(Rol).filter(Rol.id == rol_id).first()
    
    def get_all(self):
        return self.db.query(Rol).all()
    
    def create(self, rol_data: RolCreate):
        rol = Rol(**rol_data.dict())
        self.db.add(rol)
        self.db.commit()
        self.db.refresh(rol)
        return rol
        
    def update(self, rol: Rol, rol_data: RolUpdate):
        for field, value in rol_data.dict(exclude_unset=True).items():
            setattr(rol, field, value)
        self.db.commit()
        self.db.refresh(rol)
        return rol

    def delete(self, rol: Rol):
        self.db.delete(rol)
        self.db.commit()
        

#------------USERS------------------------------------------------------------------------------------------------------------------------       

class UsuarioCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def get(self,  usuario_id: int)->  Usuario | None:
        return self.db.query(Usuario).filter(Usuario.id ==  usuario_id).first()

    def get_all(self):
        return self.db.query(Usuario).all()
    
    def create(self, usuario_data: UsuarioCreate):
        usuario = Usuario(**usuario_data.dict())
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario
        
    def update(self, usuario: Usuario, usuario_data: UsuarioUpdate):
        for field, value in usuario_data.dict(exclude_unset=True).items():
            setattr(usuario, field, value)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario: Usuario):
        self.db.delete(usuario)
        self.db.commit()

#-------------------------UsuarioSedes-----------------------------------------------------------------------


        
class UsuarioSedeCrud:
    def __init__(self, db: Session):
        self.db =  db
    
    def get(self,  UsuarioSede_id: int)->  UsuarioSede | None:
        return self.db.query(UsuarioSede).filter(UsuarioSede.id ==  UsuarioSede_id).first()

    def get_all(self):
        return self.db.query(UsuarioSede).all()
    
    def create(self, usuarioSede_data: UsuarioSedeCreate):
        usuariosede = UsuarioSede(**usuarioSede_data.dict())
        self.db.add(usuariosede)
        self.db.commit()
        self.db.refresh(usuariosede)
        return usuariosede
        
    def update(self, usuariosede: UsuarioSede, usuarioSede_data: UsuarioSedeUpdate):
        for field, value in usuarioSede_data.dict(exclude_unset=True).items():
            setattr(usuariosede, field, value)
        self.db.commit()
        self.db.refresh(usuariosede)
        return usuariosede

    def delete(self, usuariosede: UsuarioSede):
        self.db.delete(usuariosede)
        self.db.commit()
