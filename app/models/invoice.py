# app/models/invoice.py
from app import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    storename = db.Column(db.String(100), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    
    # Audit fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Optional: User relationship if you want to track who created the invoice
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    # user = db.relationship('User', backref=db.backref('invoices', lazy=True))
    
    def __init__(self, item, quantity, price, storename):
        self.item = item
        self.quantity = quantity
        self.price = price
        self.storename = storename
        self.total_amount = quantity * price
    
    def __repr__(self):
        return f'<Invoice {self.id}: {self.item} from {self.storename}>'
    
    def to_dict(self):
        """Convert invoice object to dictionary"""
        return {
            'id': self.id,
            'item': self.item,
            'quantity': self.quantity,
            'price': self.price,
            'storename': self.storename,
            'total_amount': self.total_amount,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }