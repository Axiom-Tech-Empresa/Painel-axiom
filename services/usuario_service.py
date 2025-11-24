from repositories.usuario_repository import UsuarioRepository, db
import hashlib

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()
    
    def create_user(self, nome, email, senha, is_admin):
        if not nome or not email or not senha or not is_admin:
            return False
        hash_senha=hashlib.sha256(senha.encode('utf-8')).hexdigest()

        create=self.repo.create_user(nome, email, hash_senha, is_admin)
        if create:
            db.session.commit()
            return True
        return False
    def get_user_by_nome(self, nome):
        if not nome:
            return None
        usuario=self.repo.get_user_by_nome(nome)
        return usuario
    def check_password(self, nome, senha):
        if not nome or not senha:
            return False
        hash_senha=hashlib.sha256(senha.encode('utf-8')).hexdigest()
        is_valid=self.repo.check_password(nome, hash_senha)
        return is_valid