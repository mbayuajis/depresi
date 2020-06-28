from app import app, model, db
from flask import request, render_template, url_for, redirect

def index(pesan=None, status=None):
	try:
		gejala = model.Gejala.query.all()
		return render_template('gejala.html', gejala=gejala, pesan=pesan, status=status)
	except Exception as e:
		raise e

def create(id):
	try:
		penyakit = model.Penyakit.query.filter_by(id=id).first()
		gejala = model.Gejala.query.all()
		return render_template('form_gejala.html', penyakit=penyakit, gejala=gejala)
	except Exception as e:
		print(e)

def create_gejala_without_penyakit():
	return render_template('form_gejala_buat_baru.html');

def store():
	try:
		penyakit_id = request.form['penyakit_id']
		penyakit = model.Penyakit.query.filter_by(id=penyakit_id).first()
		if "checkgejala" in request.form:
			gejala_id = request.form['gejala']
			gejala = model.Gejala.query.filter_by(id=gejala_id).first()
		else:
			nama_gejala = request.form['bgejala']
			gejala = model.Gejala(gejala=nama_gejala)
			db.session.add(gejala)
		gejala.gejalas.append(penyakit)
		db.session.commit()
		return redirect(url_for('show_penyakit_with_gejala', id=penyakit_id))
	except Exception as e:
		print(e)

def store_gejala_without_penyakit():
	try:
		nama_gejala = request.form['gejala']
		gejala = model.Gejala(gejala=nama_gejala)
		db.session.add(gejala)
		db.session.commit()

		return index("Berhasil menyimpan gejala baru", True)
	except Exception as e:
		raise e

def show(id):
	try:
		gejala = model.Gejala.query.filter_by(id=id).first()
		if not gejala:
			return index("Tidak ditemukan", False)

		return render_template('form_gejala_buat_baru.html', gejala=gejala)
	except Exception as e:
		raise e

def delete(id):
	try:
		gejala = model.Gejala.query.filter_by(id=id).first()
		if not gejala:
			return index("Tidak ditemukan", False)

		db.session.delete(gejala)
		db.session.commit()

		return index("Berhasil menghapus gejala", True)
	except Exception as e:
		raise e

def update():
	try:
		id = request.form['id']
		nama_gejala = request.form['gejala']

		gejala = model.Gejala.query.filter_by(id=id).first()
		gejala.gejala = nama_gejala

		db.session.commit()

		return index("Berhasil mengubah gejala", True)
	except Exception as e:
		raise e