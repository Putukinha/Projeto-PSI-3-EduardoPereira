from datetime import date, timedelta
from database import db

loan_books = db.Table(
    "emprestimo_livro",
    db.Column("loan_id", db.Integer, db.ForeignKey("emprestimos.id", ondelete="CASCADE"), primary_key=True),
    db.Column("book_id", db.Integer, db.ForeignKey("livros.id", ondelete="CASCADE"), primary_key=True),
)

class Loan(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    loan_date = db.Column(db.Date, nullable=False, default=date.today)
    due_date = db.Column(db.Date, nullable=False, default=lambda: date.today() + timedelta(days=14))
    return_date = db.Column(db.Date)
    status = db.Column(db.String(30), nullable=False, default="Em andamento")

    user = db.relationship("User", back_populates="loans")
    books = db.relationship("Book", secondary=loan_books, back_populates="loans")

    @property
    def is_overdue(self):
        return self.status != "Devolvido" and self.due_date < date.today()

    def __repr__(self):
        return f"<Loan {self.id}>"
