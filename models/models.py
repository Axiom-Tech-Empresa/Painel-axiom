from datetime import datetime
from db_config import db 

class Usuario(db.Model):
    """
    Modelo para a tabela 'Usuarios'.
    """
    __tablename__ = 'Usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Integer, nullable=False,default=0)
    sistemas_associados = db.relationship('SistemasUsuarios', back_populates='usuario',cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Usuario {self.email}>'


class Sistema(db.Model):
    __tablename__ = 'Sistemas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    usuarios_associados = db.relationship('SistemasUsuarios',back_populates='sistema',cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Sistema {self.nome}>'


class SistemasUsuarios(db.Model):
    """
    Modelo para a tabela de associação 'SistemasUsuarios'.
    """
    __tablename__ = 'SistemasUsuarios'
    
    id_sistema = db.Column(db.Integer, db.ForeignKey('Sistemas.id'), primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), primary_key=True)
    
    status_ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_vinculo = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # [NOVA COLUNA]
    # Armazena a data de expiração.
    # nullable=True permite que este campo seja Nulo (sem expiração).
    data_expira = db.Column(db.DateTime, nullable=True, default=None)

    # RELACIONAMENTOS (apontam de volta para os pais)
    sistema = db.relationship('Sistema', back_populates='usuarios_associados')
    usuario = db.relationship('Usuario', back_populates='sistemas_associados')

    def __repr__(self):
        return f'<SistemaUsuarios {self.id_usuario} <-> {self.id_sistema}>'