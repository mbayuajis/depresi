from app import db
from datetime import datetime

class Gejala(db.Model):
	id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	gejala = db.Column(db.String(200), nullable=False)
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
