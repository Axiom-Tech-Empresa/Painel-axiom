from repositories.sistema_repository import SistemaRepository, db
from datetime import datetime

class SistemaService:
    def __init__(self):
        self.repo = SistemaRepository()
    
    def create_sistema(self, nome, descricao):
        if not nome:
            return False
        data_criacao=datetime.utcnow()
        create=self.repo.create(nome, descricao, data_criacao)
        if create:
            db.session.commit()
            return True
        return False