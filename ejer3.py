#Buscar o filtrar información. Introduce una letra y buscará todas las peliculas que empiecen por esa letra
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
contador=0
lista=[]
letra=input("Introduce una letra: ").upper()
for bloque in data["peliculas"]:
	contador=contador+1
	lista.append(bloque["nombre"])
encontrado=False
for i in lista:
	if i[0] == letra:
		print(i)
		encontrado=True
if not encontrado:	
	print("No hay ninguna pelicula que empiece por esa letra")
