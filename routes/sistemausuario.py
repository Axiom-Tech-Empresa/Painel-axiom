from flask import Blueprint, request, jsonify
from services.sistemas_usuario_service import SistemasUsuarioService

sistema_usuario_service=SistemasUsuarioService()
sistema_usuario_bp=Blueprint('SistemasUsuarios',__name__)

@sistema_usuario_bp.route('/', methods=['POST'])
def create_sistema_usuario():
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'message': 'Dados inválidos'
        }), 400
    
    id_sistema = data.get('id_sistema')
    id_usuario = data.get('id_usuario')
    # Se não enviar status, assume 1 (ativo)
    status_ativo = data.get('status_ativo', 1) 

    # Validação simplificada (datas não são mais necessárias aqui)
    if not id_sistema or not id_usuario:
        return jsonify({
            'success': False,
            'message': 'id_sistema e id_usuario são obrigatórios'
        }), 400
        
    created = sistema_usuario_service.create_sistema_usuario(id_sistema, id_usuario, status_ativo)
    
    if created:
        return jsonify({
            'success': True,
            'message': 'Associação criada com sucesso'
        }), 201
        
    return jsonify({
        'success': False,
        'message': 'Erro ao criar associação'
    }), 500