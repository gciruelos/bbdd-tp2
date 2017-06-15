jsons: generar.py
	python generar.py

upservers:
	#rethinkdb
	#rethinkdb --port-offset 1 --directory rethinkdb_data2 --join localhost:29015
	#rethinkdb --port-offset 2 --directory rethinkdb_data3 --join localhost:29015

all: upservers jsons
	rethinkdb import -f estudiante.json --table TP2.estudiante --pkey nroCertificado
	rethinkdb import -f competencia.json --table TP2.competencia --pkey idCompetencia
	rethinkdb import -f arbitro.json --table TP2.arbitro --pkey nroPlaca
	rethinkdb import -f escuela.json --table TP2.escuela --pkey CodigoEscuela

clean:
	rm -f *.json
