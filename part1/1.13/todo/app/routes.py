from flask import render_template, send_from_directory
from .services.image_service import get_cached_image

def init_routes(app):
    @app.route("/todo")
    def todo():
        image_path = get_cached_image()
        return render_template("index.html", image_path="image.jpg")
    
    @app.route("/image.jpg")
    def serve_image():
        return send_from_directory("/usr/src/app/data", "image.jpg")