from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from database import db
from models import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/")
def index():
    users = User.query.order_by(User.name).all()
    return render_template("users/index.html", users=users)

@users_bp.route("/novo", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        if not name or not email:
            flash("Nome e e-mail são obrigatórios.", "error")
            return render_template("users/form.html", user=None)
        user = User(name=name, email=email, phone=phone or None)
        db.session.add(user)
        try:
            db.session.commit()
            flash("Usuário cadastrado com sucesso.", "success")
            return redirect(url_for("users.index"))
        except IntegrityError:
            db.session.rollback()
            flash("Já existe um usuário com esse e-mail.", "error")
    return render_template("users/form.html", user=None)

@users_bp.route("/<int:user_id>/editar", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.name = request.form.get("name", "").strip()
        user.email = request.form.get("email", "").strip().lower()
        user.phone = request.form.get("phone", "").strip() or None
        if not user.name or not user.email:
            flash("Nome e e-mail são obrigatórios.", "error")
        else:
            try:
                db.session.commit()
                flash("Usuário atualizado.", "success")
                return redirect(url_for("users.index"))
            except IntegrityError:
                db.session.rollback()
                flash("Este e-mail já está cadastrado para outro usuário.", "error")
    return render_template("users/form.html", user=user)

@users_bp.route("/<int:user_id>/excluir", methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuário e seus empréstimos foram excluídos.", "success")
    return redirect(url_for("users.index"))

@users_bp.route("/<int:user_id>")
def detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("users/detail.html", user=user)
