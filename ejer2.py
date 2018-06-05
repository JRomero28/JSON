#Contar la información. Todos los directores de las películas
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
lista=[]
contador=0
for director in data["peliculas"]:
	contador=contador+1
	lista.append(director)
print(len(lista), "directores en total")
