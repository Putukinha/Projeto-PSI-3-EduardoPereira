from flask import Blueprint, render_template
from database import db
from models import User, Book, Loan

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def dashboard():
    stats = {
        "users": User.query.count(),
        "books": Book.query.count(),
        "loans": Loan.query.count(),
        "active": Loan.query.filter(Loan.status != "Devolvido").count(),
    }
    recent_loans = Loan.query.order_by(Loan.id.desc()).limit(5).all()
    return render_template("dashboard.html", stats=stats, recent_loans=recent_loans)
