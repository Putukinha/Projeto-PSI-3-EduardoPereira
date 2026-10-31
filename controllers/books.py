from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from database import db
from models import Book

books_bp = Blueprint("books", __name__)

@books_bp.route("/")
def index():
    books = Book.query.order_by(Book.title).all()
    return render_template("books/index.html", books=books)

@books_bp.route("/novo", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        isbn = request.form.get("isbn", "").strip() or None
        try:
            copies = max(1, int(request.form.get("copies", "1")))
        except ValueError:
            copies = 1
        book = Book(title=title, author=author, genre=request.form.get("genre", "").strip(),
                    isbn=isbn, copies=copies)
        if not title or not author:
            flash("Título e autor são obrigatórios.", "error")
        else:
            db.session.add(book)
            try:
                db.session.commit()
                flash("Livro cadastrado com sucesso.", "success")
                return redirect(url_for("books.index"))
            except IntegrityError:
                db.session.rollback()
                flash("Este ISBN já está cadastrado.", "error")
    return render_template("books/form.html", book=None)

@books_bp.route("/<int:book_id>/editar", methods=["GET", "POST"])
def edit(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        book.title = request.form.get("title", "").strip()
        book.author = request.form.get("author", "").strip()
        book.genre = request.form.get("genre", "").strip()
        book.isbn = request.form.get("isbn", "").strip() or None
        try:
            book.copies = max(1, int(request.form.get("copies", "1")))
        except ValueError:
            book.copies = 1
        if not book.title or not book.author:
            flash("Título e autor são obrigatórios.", "error")
        else:
            try:
                db.session.commit()
                flash("Livro atualizado.", "success")
                return redirect(url_for("books.index"))
            except IntegrityError:
                db.session.rollback()
                flash("Este ISBN já está cadastrado.", "error")
    return render_template("books/form.html", book=book)

@books_bp.route("/<int:book_id>/excluir", methods=["POST"])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Livro excluído.", "success")
    return redirect(url_for("books.index"))

@books_bp.route("/<int:book_id>")
def detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("books/detail.html", book=book)
