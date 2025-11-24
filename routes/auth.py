from flask import Blueprint, request, jsonify
from services.sistemas_usuario_service import SistemasUsuarioService
from services.usuario_service import UsuarioService

sistemas_usuarios_service = SistemasUsuarioService()
usuario_service = UsuarioService()
auth_bp = Blueprint('Auth', __name__)

@auth_bp.route('/', methods=['POST'])
def validate_user():
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'message': 'Dados inválidos'
        }), 400
    
    nome = data.get('nome')
    senha = data.get('senha')
    id_sistema = data.get('id_sistema')

    if not nome or not senha:
        return jsonify({
            'success': False,
            'message': 'Email e senha são obrigatórios'
        }), 400
    
    user = usuario_service.get_user_by_nome(nome)
    
    if not user or not usuario_service.check_password(nome, senha):
        return jsonify({
            'success': False,
            'message': 'Falha na autenticação do usuário'
        }), 400
    
    association = sistemas_usuarios_service.get_association_by_user_and_sistema(user.id, id_sistema)

    if association and association.status_ativo == 1:
        return jsonify({
            'success': True,
            'message': 'Usuário autenticado com sucesso'
        }), 200

    return jsonify({
        'success': False,
        'message': 'Email ou senha incorretos'
    }), 401