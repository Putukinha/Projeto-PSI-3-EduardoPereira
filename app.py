from flask import Flask, redirect, url_for
from database import init_db
from controllers import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "segredo_dos_livros"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(app)
    register_blueprints(app)

    @app.route("/")
    def index():
        return redirect(url_for("main.dashboard"))

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
