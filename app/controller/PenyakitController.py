from app import app, model, db
from flask import request, render_template

def index(pesan=None, status=None):
	try:
		penyakit = model.Penyakit.query.all()
		return render_template('penyakit.html', penyakit=penyakit, pesan=pesan, status=status)
	except Exception as e:
		print(e)

def create():
	return render_template('form_penyakit.html')

def store():
	try:
		nama_penyakit = request.form['penyakit']
		penyakit = model.Penyakit(penyakit=nama_penyakit)
		db.session.add(penyakit)
		db.session.commit()
		return index("Berhasil menyimpan", True)
	except Exception as e:
		print(e)

def show(id):
	try:
		penyakit = model.Penyakit.query.filter_by(id=id).first()
		if not penyakit:
			return index("Tidak ditemukan", False)

		return render_template('form_penyakit.html', penyakit=penyakit)
	except Exception as e:
		print(e)

def delete(id):
	try:
		penyakit = model.Penyakit.query.filter_by(id=id).first()
		if not penyakit:
			return index("Tidak ditemukan", False)

		db.session.delete(penyakit)
		db.session.commit()

		return index("Berhasil menghapus", True)
	except Exception as e:
		print(e)

def update():
	try:
		id = request.form['id']
		nama_penyakit = request.form['penyakit']

		penyakit = model.Penyakit.query.filter_by(id=id).first()
		penyakit.penyakit = nama_penyakit

		db.session.commit()

		return index("Berhasil mengedit data", True)
	except Exception as e:
		print(e)

def with_gejala(id):
	try:
		penyakit = model.Penyakit.query.filter_by(id=id).first()
		return render_template('penyakit_gejala.html', penyakit=penyakit)
	except Exception as e:
		print(e)