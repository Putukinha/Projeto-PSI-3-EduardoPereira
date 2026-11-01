from datetime import datetime
from database import db

class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(160), unique=True, nullable=False)
    phone = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    loans = db.relationship(
        "Loan", back_populates="user", cascade="all, delete-orphan",
        order_by="Loan.loan_date.desc()"
    )

    def __repr__(self):
        return f"<User {self.name}>"
