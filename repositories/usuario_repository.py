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
    
    def get_user_by_nome(self,nome):
        usuario=Usuario.query.filter_by(nome=nome).first()
        return usuario
    def check_password(self,nome,senha):
        usuario=Usuario.query.filter_by(nome=nome).first()
        if not usuario:
            return False
        return usuario.senha_hash == senha