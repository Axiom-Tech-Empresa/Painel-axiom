from repositories.sistemas_usuario_repository import SistemasUsuariosRepository, db
from datetime import datetime, timedelta

class SistemasUsuarioService:
    def __init__(self):
        self.repo = SistemasUsuariosRepository()
    
    def create_sistema_usuario(self, id_sistema, id_usuario, status_ativo=1):
        # Lógica 1: Define a data de vínculo como AGORA
        data_vinculo = datetime.now()
        
        # Lógica 2: Define a expiração para 30 dias após o vínculo
        data_expira = data_vinculo + timedelta(days=30)

        # Chama o repositório passando os OBJETOS datetime (não strings)
        try:
            created = self.repo.create(
                id_sistema, 
                id_usuario, 
                status_ativo, 
                data_vinculo, 
                data_expira
            )
            
            if created:
                db.session.commit() # Confirma a transação
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao criar vinculo: {e}")
            return False