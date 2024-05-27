from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/Marketplace'

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from controller.produto_controller import produto_bp
        from controller.vendedor_controller import vendedor_bp

        app.register_blueprint(produto_bp)
        app.register_blueprint(vendedor_bp)

        return app