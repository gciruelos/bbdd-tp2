

%.json: generar.py
	python generar.py

upservers:
	#rethinkdb
	#rethinkdb --port-offset 1 --directory rethinkdb_data2 --join localhost:29015

all: upservers estudiante.json
	rethinkdb import -f estudiante.json --table TP2.estudiante

clean:
	rm *.json
