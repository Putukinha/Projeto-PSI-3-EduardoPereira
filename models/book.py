from database import db

class Book(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    author = db.Column(db.String(140), nullable=False)
    genre = db.Column(db.String(80))
    isbn = db.Column(db.String(30), unique=True)
    copies = db.Column(db.Integer, nullable=False, default=1)

    loans = db.relationship("Loan", secondary="emprestimo_livro", back_populates="books")

    def __repr__(self):
        return f"<Book {self.title}>"
