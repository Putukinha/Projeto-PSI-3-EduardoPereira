from datetime import date, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Loan, User, Book

loans_bp = Blueprint("loans", __name__)

def parse_date(value, fallback):
    try:
        return date.fromisoformat(value) if value else fallback
    except ValueError:
        return fallback

@loans_bp.route("/")
def index():
    loans = Loan.query.order_by(Loan.loan_date.desc(), Loan.id.desc()).all()
    return render_template("loans/index.html", loans=loans)

@loans_bp.route("/novo", methods=["GET", "POST"])
def create():
    users = User.query.order_by(User.name).all()
    books = Book.query.order_by(Book.title).all()
    if not users or not books:
        flash("Cadastre pelo menos um usuário e um livro antes de criar um empréstimo.", "error")
        return redirect(url_for("loans.index"))
    if request.method == "POST":
        user = User.query.get(request.form.get("user_id", type=int))
        selected_ids = request.form.getlist("book_ids", type=int)
        selected_books = Book.query.filter(Book.id.in_(selected_ids)).all() if selected_ids else []
        if not user or not selected_books:
            flash("Selecione um usuário e pelo menos um livro.", "error")
        else:
            loan_date = parse_date(request.form.get("loan_date"), date.today())
            due_date = parse_date(request.form.get("due_date"), loan_date + timedelta(days=14))
            loan = Loan(user=user, books=selected_books, loan_date=loan_date, due_date=due_date,
                        status="Em andamento")
            db.session.add(loan)
            db.session.commit()
            flash("Empréstimo criado com os livros selecionados.", "success")
            return redirect(url_for("loans.index"))
    return render_template("loans/form.html", loan=None, users=users, books=books)

@loans_bp.route("/<int:loan_id>")
def detail(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    return render_template("loans/detail.html", loan=loan)

@loans_bp.route("/<int:loan_id>/editar", methods=["GET", "POST"])
def edit(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    users = User.query.order_by(User.name).all()
    books = Book.query.order_by(Book.title).all()
    if request.method == "POST":
        user = User.query.get(request.form.get("user_id", type=int))
        selected_ids = request.form.getlist("book_ids", type=int)
        selected_books = Book.query.filter(Book.id.in_(selected_ids)).all() if selected_ids else []
        if not user or not selected_books:
            flash("Selecione um usuário e pelo menos um livro.", "error")
        else:
            loan.user = user
            loan.books = selected_books
            loan.loan_date = parse_date(request.form.get("loan_date"), loan.loan_date)
            loan.due_date = parse_date(request.form.get("due_date"), loan.due_date)
            loan.status = request.form.get("status", "Em andamento")
            if loan.status == "Devolvido":
                loan.return_date = date.today()
            else:
                loan.return_date = None
            db.session.commit()
            flash("Empréstimo atualizado.", "success")
            return redirect(url_for("loans.index"))
    return render_template("loans/form.html", loan=loan, users=users, books=books)

@loans_bp.route("/<int:loan_id>/devolver", methods=["POST"])
def return_loan(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    loan.status = "Devolvido"
    loan.return_date = date.today()
    db.session.commit()
    flash("Empréstimo marcado como devolvido.", "success")
    return redirect(url_for("loans.index"))

@loans_bp.route("/<int:loan_id>/excluir", methods=["POST"])
def delete(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    db.session.delete(loan)
    db.session.commit()
    flash("Empréstimo excluído.", "success")
    return redirect(url_for("loans.index"))
