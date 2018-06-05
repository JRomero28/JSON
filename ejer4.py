#Buscar o filtrar relacionada. Todas las películas según su género
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)
print("¿Qué quieres buscar?")
print("[Drama, Comedia, Documental o Acción]")
busqueda=input("Introduce el género: ")
encontrado=False
for bloque in data["peliculas"]:
	if bloque["clasificacion"] == busqueda:
		print("El título del documental es:",bloque["nombre"])
		encontrado=True
if not encontrado:
	print("Has introducido mal el género")
