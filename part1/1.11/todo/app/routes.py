from flask import render_template

def init_routes(app):
    @app.route("/todo")
    def todo():
        return render_template("index.html")
