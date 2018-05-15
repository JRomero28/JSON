#Muestra las películas del director “Tarantino”
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
for bloque in data["peliculas"]:
	if bloque["director"] == "Tarantino":
		print("Título de la pelicula de Trantino:",bloque["nombre"])
