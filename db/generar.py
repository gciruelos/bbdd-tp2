from random import seed,randint
from copy import copy
from collections import defaultdict
from pprint import pprint
from json import dump

seed(10)

escuelas = [
        { "CodigoEscuela": 0, "Nombre": 'Escuela X', "pais": 'Argentina' },
        { "CodigoEscuela": 1, "Nombre": 'Schule X', "pais": 'Alemania' },
        { "CodigoEscuela": 2, "Nombre": 'Koulu X', "pais": 'Finlandia' },
        ]

for escuela in escuelas:
    escuela["Resultados"] = []

def obtener_dni():
    return randint(20000000, 39000000)

def obtener_nrocert():
    return randint(1, 10000000)



def generar_estudiantes(nombres):
    for nom,ape in nombres:
        nroCertificado = obtener_nrocert()
        estudiante = {}
        estudiante['nroCertificado'] = obtener_nrocert()
        estudiante['Nombre'] = nom
        estudiante['Apellido'] = ape
        estudiante['DNI'] = obtener_dni()
        escuela = {}
        escuela_i = randint(0,2);
        escuela['Nombre'] = escuelas[escuela_i]['Nombre']
        escuela['CodigoEscuela'] = escuelas[escuela_i]['CodigoEscuela']
        estudiante['Escuela'] = escuela
        estudiante['ResultadosPorMundial'] = []
        yield estudiante

mundiales = {
    2015: { 'nombre' : 'Chelyabinsk' },
    2013: { 'nombre' : 'Puebla' },
    2011: { 'nombre' : 'Gyeongju'},
}
def to_cat(x):
    return {
            "idCategoria": x[0],
            "Genero": x[1],
            "Dan": x[2],
            "EdadMinima": x[3],
            "EdadMaxima": x[4],
            "pesoMinimo": x[5],
            "pesoMaximo": x[6]
            }

competencias_ = [
  {
      "idCompetencia" : 1,
      "Categoria" : to_cat((0, 'Femenino', 1, 20, 30, 50, 65)),
      "TipoCompetencia": 'Salto'
  }, {
      "idCompetencia" : 2,
      "Categoria" : to_cat((1, 'Masculino', 1, 20, 30, 65, 80)),
      "TipoCompetencia": 'Salto'
  },
  {
      "idCompetencia" : 3,
      "Categoria" : to_cat((0, 'Femenino', 1, 20, 30, 50, 65)),
      "TipoCompetencia": 'Combate'
  }, {
      "idCompetencia" : 4,
      "Categoria" : to_cat((1, 'Masculino', 1, 20, 30, 65, 80)),
      "TipoCompetencia": 'Combate'
  }
]

def generar_competencias(cs):
    for c in cs:
        for year in mundiales.keys():
            cp = copy(c)
            cp["idCompetencia"] = randint(1, 1000)
            cp["Mundial"] = {
                    "Nombre": mundiales[year]['nombre'],
                    "Year": year
            }
            cp["Arbitros"] = []
            yield cp

competencias = list(generar_competencias(competencias_))


def producto_cartesiano(xs, ys):
    for x in xs:
        for y in ys:
            yield x, y


nombresM = ['Nombro', 'Pepe', 'Juan', 'Carlitos', 'Carlos', 'Juancito', 'Pepito']
nombresF = ['Nombra', 'Pepa', 'Juana', 'Maria', 'Juanita', 'Pepita']
apellidos = ['Apellido', 'Perez', 'Rodriguez', 'Gonzalez', 'Alvarez', 'Asdf']

estudiantesF = list(generar_estudiantes(list(producto_cartesiano(nombresF, apellidos))))
estudiantesM = list(generar_estudiantes(list(producto_cartesiano(nombresM, apellidos))))

# print(list(generar_estudiantes(estudiantesF)))


puestosPorEscuela = {}

def add_combate(estudiantes, genero):
    global puestosPorEscuela
    for m in mundiales.keys():
        comps = defaultdict(list)
        for c in competencias:
            if c['Mundial']['Year'] != m or c['Categoria']['Genero'] != genero or c['TipoCompetencia'] != 'Combate': continue
            enfrentamientos = defaultdict(list)
            ganados = defaultdict(int)
            for e1 in estudiantes:
                for e2 in estudiantes:
                    if e1['DNI'] < e2['DNI']: # e1 gana
                        enfrentamientos[e1['DNI']].append({
                            "nroCertificadoDelOponente": e2["nroCertificado"],
                            "NombreDelOponente": e2["Nombre"],
                            "Gano": 1
                            })
                        ganados[e1['DNI']] += 1
                        enfrentamientos[e2['DNI']].append({
                            "nroCertificadoDelOponente": e1["nroCertificado"],
                            "NombreDelOponente": e1["Nombre"],
                            "Gano": 0
                            })
                ganados[e1['DNI']] += 1
                ganados[e1['DNI']] -= 1
            ganados_s = list(
                    map(lambda x: x[0],
                        sorted(ganados.items(), key=lambda x: x[1])))

            for e in estudiantes:
                puesto = ganados_s.index(e['DNI']) + 1
                comps[e['DNI']].append({
                        "TipoCompetencia": c['TipoCompetencia'],
                        "Puesto": puesto,
                        "Enfrentamientos": enfrentamientos[e['DNI']]
                })
                codigoEscuela = e['Escuela']['CodigoEscuela']
                if codigoEscuela not in puestosPorEscuela.keys():
                    puestosPorEscuela[codigoEscuela] = defaultdict(list)
                puestosPorEscuela[codigoEscuela][m].append(puesto)

        for e in estudiantes:
            e["ResultadosPorMundial"].append(
                {"Mundial" : {
                    "Nombre": mundiales[m]['nombre'],
                    "Year": m
                 },
                 "Competencias" : comps[e['DNI']]
                 })


add_combate(estudiantesF, 'Femenino')
add_combate(estudiantesM, 'Masculino')


for e in escuelas:
    for m in mundiales.keys():
        resultado = {
            "Mundial" : {
                "Nombre": mundiales[m]['nombre'],
                "Year": m },
            "Puestos" : puestosPorEscuela[e['CodigoEscuela']][m]
        }
        e["Resultados"].append(resultado)

nombresArbitros = list(map(lambda x: x[0]+' '+x[1], producto_cartesiano(
    ['Jorge', 'Carlos', 'Manuel', 'Antonio', 'Carmen', 'Josefa', 'Isabel', 'R'],
    ['Perez', 'Rodriguez', 'Smith', 'Robertson', 'X', 'Y', 'Z', 'W', 'A', 'B'])))

mundiales_struct = [{ "Nombre": mundiales[m]['nombre'], "Year": m }
        for m in mundiales.keys()]

paisesArbitros = ['Argentina', 'Corea del Norte', 'Belgica', 'Bolivia', 'Mexico']

arbitros = [{
    'nroPlaca': randint(1000, 1000000),
    'Nombre': nom,
    'pais': paisesArbitros[randint(0,4)],
    'Mundiales': mundiales_struct[:randint(0,2)]} for nom in nombresArbitros]

for a in arbitros:
    for c in competencias:
        if c['Mundial'] in a['Mundiales']:
            c['Arbitros'].append(a['nroPlaca'])




with open('estudiante.json', 'w') as est_file:
    dump(estudiantesF+estudiantesM, est_file)

with open('arbitro.json', 'w') as arb_file:
    dump(arbitros, arb_file)

with open('competencia.json', 'w') as com_file:
    dump(competencias, com_file)

with open('escuela.json', 'w') as esc_file:
    dump(escuelas, esc_file)


