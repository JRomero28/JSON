#Muestra todos los títulos de las películas.
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
contador=0
for bloque in data["peliculas"]:
	contador=contador+1
	print("Título de la película",contador,":",bloque["nombre"])
