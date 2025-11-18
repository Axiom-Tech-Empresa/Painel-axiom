from models.models import Usuario, db

class UsuarioRepository:
    def get_all(self):
        usuarios=Usuario.query.all()
        return usuarios
    
    def create_user(self):
        pass