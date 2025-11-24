from models.models import SistemasUsuarios, db

class SistemasUsuariosRepository:
    def get_all(self):
        return SistemasUsuarios.query.all()
    
    def create(self, id_sistema, id_usuario, status_ativo, data_vinculo, data_expira):
        novo_sistema_usuario = SistemasUsuarios(
            id_sistema=id_sistema,
            id_usuario=id_usuario,
            status_ativo=status_ativo,
            data_vinculo=data_vinculo,
            data_expira=data_expira   
        )
        db.session.add(novo_sistema_usuario)
        db.session.flush()
        return True