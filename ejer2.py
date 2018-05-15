#Muestra todos los directores de las películas
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
contador=0
for director in data["peliculas"]:
	contador=contador+1
	print("Nombre del director",contador,":",director["director"])
