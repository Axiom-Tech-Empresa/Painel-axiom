from db_config import app
from flask import Blueprint
from routes.usuario import usuario_bp
from routes.sistema import sistema_bp
from routes.sistemausuario import sistema_usuario_bp

app.register_blueprint(usuario_bp, url_prefix='/usuarios')
app.register_blueprint(sistema_bp, url_prefix='/sistemas')
app.register_blueprint(sistema_usuario_bp, url_prefix='/sistemas-usuario')

if __name__=="__main__":
    app.run(debug=True)