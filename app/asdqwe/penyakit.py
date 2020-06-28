from app import db
from datetime import datetime
from app.model.gejala import Gejala
from app.model.penyakitgejala import PenyakitGejala

class Penyakit(db.Model):
	id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	penyakit = db.Column(db.String(140), nullable=False)
	gejalas = db.relationship('Gejala', secondary=PenyakitGejala.penyakitgejala, lazy='dynamic', backref=db.backref('gejalas', lazy=True))
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)	