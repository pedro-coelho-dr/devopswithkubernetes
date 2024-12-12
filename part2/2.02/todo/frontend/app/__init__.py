from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    with app.app_context():
        from .routes import init_routes
        init_routes(app)

    return app
