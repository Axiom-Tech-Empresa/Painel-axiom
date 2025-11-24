from models.models import Sistema, db

class SistemaRepository:
    def get_all(self):
        sistemas=Sistema.query.all()
        return sistemas
    def create(self, nome, descricao, data_criacao):
        novo_sistema=Sistema(
            nome=nome,
            descricao=descricao,
            data_criacao=data_criacao
        )
        db.session.add(novo_sistema)
        db.session.flush()
        return True