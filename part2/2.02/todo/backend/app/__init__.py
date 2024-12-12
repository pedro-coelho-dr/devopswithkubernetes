from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import backend_routes
        app.register_blueprint(backend_routes)

    return app