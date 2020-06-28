from app import db
from datetime import datetime

penyakitgejala = db.Table('penyakitgejala',
	    db.Column('penyakit_id', db.BigInteger, db.ForeignKey('penyakit.id')),
	    db.Column('gejala_id', db.BigInteger, db.ForeignKey('gejala.id'))
	)

class Penyakit(db.Model):
	id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	penyakit = db.Column(db.String(140), nullable=False)
	gejalas = db.relationship('Gejala', secondary=penyakitgejala, lazy='dynamic', backref=db.backref('gejalas', lazy=True))
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Gejala(db.Model):
	id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	gejala = db.Column(db.String(200), nullable=False)
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)