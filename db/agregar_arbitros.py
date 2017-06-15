import rethinkdb as r
import random

r.connect('localhost', 28015).repl()

arbs = []
for i in range(100):
    placa = random.randint(1, 1000000)
    arbitro = {
            "nroPlaca": placa,
            "nombre": 'Pepito '+str(placa),
            "pais": 'Republica de ' + str(random.randint(1, 100))
            }
    arbs.append(arbitro)

print(r.db('TP2').table('arbitro').insert(arbs).run())


