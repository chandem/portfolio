from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False, default='user')

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    condition = db.Column(db.String(64), nullable=False)
    last_inspection_date = db.Column(db.DateTime, nullable=True)
    work_orders = db.relationship('WorkOrder', backref='asset', lazy=True)

class WorkOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(64), nullable=False, default='pending')
    assigned_to = db.Column(db.String(64), nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    inspection_id = db.Column(db.Integer, db.ForeignKey('inspection.id'), nullable=True)

class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    inspector = db.Column(db.String(64), nullable=False)
    inspection_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    condition = db.Column(db.String(64), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    work_orders = db.relationship('WorkOrder', backref='inspection', lazy=True)