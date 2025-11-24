from models.models import Usuario, db

class UsuarioRepository:
    def get_all(self):
        usuarios=Usuario.query.all()
        return usuarios
    
    def create_user(self, nome,email,senha_hash,is_admin):
        novo_usuario=Usuario(
            nome=nome,
            email=email,
            senha_hash=senha_hash,
            is_admin=is_admin
        )
        db.session.add(novo_usuario)
        db.session.flush()
        return True