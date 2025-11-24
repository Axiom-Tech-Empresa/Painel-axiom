from flask import Blueprint, request, jsonify
from services.sistemas_usuario_service import SistemasUsuariosService
from services.usuario_service import UsuarioService

sistemas_usuarios_service = SistemasUsuariosService()
usuario_service = UsuarioService()
auth_bp = Blueprint('Auth', __name__)

@auth_bp.route('/validate', methods=['POST'])
def validate_user():
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'message': 'Dados inválidos'
        }), 400
    
    nome = data.get('nome')
    senha = data.get('senha')
    
    if not nome or not senha:
        return jsonify({
            'success': False,
            'message': 'Email e senha são obrigatórios'
        }), 400
    
    user = usuario_service.get_user_by_nome(nome)
    
    if user and usuario_service.check_password(user, senha):
        return jsonify({
            'success': True,
            'message': 'Usuário validado com sucesso',
            'user_id': user.id,
            'is_admin': user.is_admin
        }), 200
    
    return jsonify({
        'success': False,
        'message': 'Email ou senha incorretos'
    }), 401