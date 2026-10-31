from controllers.main import main_bp
from controllers.users import users_bp
from controllers.books import books_bp
from controllers.loans import loans_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix="/usuarios")
    app.register_blueprint(books_bp, url_prefix="/livros")
    app.register_blueprint(loans_bp, url_prefix="/emprestimos")
