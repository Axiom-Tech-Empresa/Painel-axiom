from flask import Blueprint, request, jsonify
from services.sistema_service import SistemaService

sistema_service=SistemaService()
sistema_bp=Blueprint('Sistema',__name__)

@sistema_bp.route('/',methods=['POST'])
def create_sistema():
    data=request.get_json()
    if not data:
        return jsonify({
            'sucess':False,
            'message':'Dados inválidos'
        }),400
    nome=data.get('nome')
    descricao=data.get('descricao')
    if not nome:
        return jsonify({
            'sucess':False,
            'message':'O campo nome é obrigatório'
            }),400
    created=sistema_service.create_sistema(nome,descricao)
    if created:
        return jsonify({
            'sucess':True,
            'message':'Sistema criado com sucesso'
            }),201
    return jsonify({
        'sucess':False,
        'message':'Erro ao criar sistema'
        }),500