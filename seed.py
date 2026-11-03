"""Popula o banco com exemplos demonstrativos. Seguro para executar mais de uma vez."""
from datetime import date, timedelta
from app import app
from database import db
from models import User, Book, Loan

with app.app_context():
    if User.query.count() == 0:
        users = [
            User(name="Ana Souza", email="ana@example.com", phone="(84) 99999-1111"),
            User(name="Carlos Lima", email="carlos@example.com", phone="(84) 98888-2222"),
            User(name="Marina Alves", email="marina@example.com", phone="(84) 97777-3333"),
        ]
        db.session.add_all(users)
    if Book.query.count() == 0:
        books = [
            Book(title="Dom Casmurro", author="Machado de Assis", genre="Romance", isbn="9780000000011", copies=3),
            Book(title="O Pequeno Príncipe", author="Antoine de Saint-Exupéry", genre="Fábula", isbn="9780000000012", copies=5),
            Book(title="A Hora da Estrela", author="Clarice Lispector", genre="Romance", isbn="9780000000013", copies=2),
            Book(title="O Hobbit", author="J. R. R. Tolkien", genre="Fantasia", isbn="9780000000014", copies=4),
        ]
        db.session.add_all(books)
    db.session.commit()

    if Loan.query.count() == 0:
        ana = User.query.filter_by(email="ana@example.com").first()
        carlos = User.query.filter_by(email="carlos@example.com").first()
        dom = Book.query.filter_by(isbn="9780000000011").first()
        principe = Book.query.filter_by(isbn="9780000000012").first()
        hobbit = Book.query.filter_by(isbn="9780000000014").first()
        if ana and carlos and dom and principe and hobbit:
            db.session.add_all([
                Loan(user=ana, books=[dom, principe], loan_date=date.today()-timedelta(days=2),
                     due_date=date.today()+timedelta(days=12), status="Em andamento"),
                Loan(user=carlos, books=[hobbit], loan_date=date.today()-timedelta(days=20),
                     due_date=date.today()-timedelta(days=6), status="Em andamento"),
            ])
            db.session.commit()
    print("Seed concluído. Dados de demonstração disponíveis.")
