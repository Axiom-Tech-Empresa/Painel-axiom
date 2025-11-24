from db_config import app
from flask import Blueprint
from routes.usuario import usuario_bp
from routes.sistema import sistema_bp
from routes.sistemausuario import sistema_usuario_bp
from routes.auth import auth_bp
import os

app.register_blueprint(usuario_bp, url_prefix='/usuarios')
app.register_blueprint(sistema_bp, url_prefix='/sistemas')
app.register_blueprint(sistema_usuario_bp, url_prefix='/sistemas-usuario')
app.register_blueprint(auth_bp, url_prefix='/validate')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port))