from app import app, model, db
from flask import jsonify

# class NaifBayes():
def proses(gejala):
	# langkah 1
	m = model.Gejala.query.count()
	pern = model.Penyakit.query.count()
	penyakit = transform(model.Penyakit.query.all())
	data = {}
	for i in penyakit:
		p = 1/pern
		data[i['id']] = {'p':p,'ncs':{}}
		for k in gejala:
			data[i['id']]['ncs'][k] = {'nc':0}
			for j in i['gejala']:
				if j['id'] == k:
					data[i['id']]['ncs'][k]['nc'] = 1

	# langkah 2
	for i in data:
		for j in data[i]['ncs']:
			data[i]['ncs'][j]['P'] = (float(data[i]['ncs'][j]['nc'])+float(m)+float(data[i]['p']))/(1+float(m))

	# # langkah 3
	for i in data:
		data[i]['hasil'] = data[i]['p']
		for j in data[i]['ncs']:
			data[i]['hasil'] = data[i]['hasil']*data[i]['ncs'][j]['P']

	# langkah 4
	nilaitertinggi = 0
	keynilaitertinggi = 0
	for i in data:
		if data[i]['hasil'] > nilaitertinggi:
			nilaitertinggi = data[i]['hasil']
			keynilaitertinggi = i

	return jsonify(data);

def transform(datas):
	array = []
	for i in datas:
		array.append(singleTransform(i))
	return array

def singleTransform(datas, penyakitWithgejala=True):
	data = {
		'id': datas.id
	}

	if penyakitWithgejala:
		gejala = []
		for i in datas.gejalas:
			gejala.append({
				'id': i.id
				})
		data['gejala'] = gejala

	return data