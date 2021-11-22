from application import db
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash

# TODO: Create db again :(


class Users(db.Model):
    # Table columns
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwrd_hash = db.Column(db.String(128), nullable=False)
    cash = db.Column(db.Float, nullable=False, default=10000.00)

    # Table relations
    owned_stock = db.relationship("OwnedStock", backref="owner", lazy=True)
    user_transactions = db.relationship("Transactions", backref="user", lazy=True)

    def __repr__(self):
        return f"Users('{self.username}', '{self.email}' with '{self.cash}')"


class OwnedStock(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    stock_symbol = db.Column(db.String(8), nullable=False)
    cost_on_purchase = db.Column(db.Float, nullable=False)
    num_of_shares = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"OwnedStock('{self.user_id}', '{self.stock_symbol}', '{self.cost_on_purchase}', '{self.num_of_shares}')"


class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    stock_symbol = db.Column(db.String(8), nullable=False)
    action = db.Column(db.String(8), nullable=False)
    affected_number = db.Column(db.Integer, nullable=False)
    cost_on_action = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Transactions('{self.user_id}', '{self.stock_symbol}', '{self.action}', '{self.affected_number}', '{self.cost_on_action}', '{self.date}')"
