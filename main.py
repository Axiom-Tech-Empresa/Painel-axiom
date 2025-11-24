from db_config import app
from flask import Blueprint
from routes.usuario import usuario_bp

app.register_blueprint(usuario_bp, url_prefix='/usuarios')

if __name__=="__main__":
    app.run(debug=True)