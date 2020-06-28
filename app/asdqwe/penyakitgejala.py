from app import db
from datetime import datetime
from app.model.gejala import Gejala
from app.model.penyakit import Penyakit

class PenyakitGejala():
	penyakitgejala = db.Table('penyakitgejala',
	    db.Column('penyakit_id', db.Integer, db.ForeignKey(Penyakit.id)),
	    db.Column('gejala_id', db.Integer, db.ForeignKey(Gejala.id))
	)
	# id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
	# penyakit_id = db.Column(db.BigInteger, db.ForeignKey(Penyakit.id))
	# penyakit = db.relationship("Penyakit", backref="penyakit_id")
	# gejala_id = db.Column(db.BigInteger, db.ForeignKey(Gejala.id))
	# gejala = db.relationship("Gejala", backref="gejala_id")
	# created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	# updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
		