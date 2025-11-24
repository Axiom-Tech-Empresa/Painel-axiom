from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

usuario_service=UsuarioService()
usuario_bp=Blueprint('User',__name__)

@usuario_bp.route('/',methods=['POST'])
def create_user():
    data=request.get_json()
    if not data:
        return jsonify({'sucess':False,'message':'Dados inválidos'}),400
    nome=data.get('nome')
    email=data.get('email')
    senha=data.get('senha')
    is_admin=data.get('is_admin')
    if not nome or not email or not senha or is_admin is None:
        return jsonify({'sucess':False,'message':'Todos os campos são obrigatórios'}),400
    created=usuario_service.create_user(nome,email,senha,is_admin)
    if created:
        return jsonify({'sucess':True,'message':'Usuário criado com sucesso'}),201
    return jsonify({'sucess':False,'message':'Erro ao criar usuário'}),500