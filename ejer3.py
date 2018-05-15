#Muestra todas las películas del genero “Documental”
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
for bloque in data["peliculas"]:
	if bloque["clasificacion"] == "Documental":
		print("El título del documental es:",bloque["nombre"])
