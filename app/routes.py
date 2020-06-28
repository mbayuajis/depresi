from app import app
from app.controller import PenyakitController, GejalaController
from app import naifbayes

@app.route('/')
@app.route('/index')
def index():
	return "Hello"

@app.route('/penyakit', methods=['GET', 'POST'])
def penyakit():
	if request.method == 'GET':
		return PenyakitController.index()
	elif "id" in request.form:
		return PenyakitController.update()
	else:
		return PenyakitController.store()

@app.route('/penyakit/create')
def create_penyakit_page():
	return PenyakitController.create()

@app.route('/penyakit/<id>')
def show_penyakit(id):
	return PenyakitController.show(id)

@app.route('/penyakit/<id>/delete')
def delete_penyakit(id):
	return PenyakitController.delete(id)

@app.route('/penyakit/<id>/gejala')
def show_penyakit_with_gejala(id):
	return PenyakitController.with_gejala(id)

@app.route('/penyakit/<id>/gejala/tambah', methods=['GET', 'POST'])
def create_gejala(id):
	if request.method == 'GET':
		return GejalaController.create(id)
	else:
		return GejalaController.store()

@app.route('/gejala', methods=['GET', 'POST'])
def gejala():
	if request.method == 'GET':
		return GejalaController.index()
	elif request.form['id']:
		return GejalaController.update()
	else:
		return GejalaController.store_gejala_without_penyakit()

@app.route('/gejala/create')
def create_gejala_without_penyakit():
	return GejalaController.create_gejala_without_penyakit()

@app.route('/gejala/<id>')
def show_gejala(id):
	return GejalaController.show(id)

@app.route('/gejala/<id>/delete')
def delete_gejala(id):
	return GejalaController.delete(id)

@app.route('/checkgejala')
def checkgejala():
	return naifbayes.proses([1,2])