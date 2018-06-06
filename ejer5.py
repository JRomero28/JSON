#Ejercicio libre. Una película según id, director, género o año
import json
from pprint import pprint
with open("peliculas.json") as data_file:
	data=json.load(data_file)

def menu():
	print("PULSA EL NÚMERO PARA LA BUSQUEDA")
	print("1. Por id")
	print("2. Por direcotor")
	print("3. Por género")
	print("4. Por año")
	print("5. Salir")
	print("")

while True:
	menu()
	orden=int(input("¿Cómo quieres buscar la pelicula? "))
	if orden == 1:
		ide=int(input("Número de la id (del 1 al 10): "))
		print(" ")
		for bloque in data["peliculas"]:
			if bloque["id"] == ide:
				print("Título de la pelicula de la id",ide,":",bloque["nombre"])
				print("")

	elif orden == 2:
		director=input("Nombre del director: ")
		print(" ")
		for bloque in data["peliculas"]:
			if bloque["director"] == director:
				print("Título de la pelicula del director",director,":",bloque["nombre"])
				print("")

	elif orden == 3:
		clasificacion=input("Nombre de la clasificacion: ")
		print(" ")
		for bloque in data["peliculas"]:
			if bloque["clasificacion"] == clasificacion:
				print("Título de la pelicula del genero",clasificacion,":",bloque["nombre"])
				print("")

	elif orden == 4:
		año=int(input("Numero del año: "))
		print(" ")
		for bloque in data["peliculas"]:
			if bloque["director"] == director:
				print("Título de la pelicula del director",director,":",bloque["nombre"])
				print("")

	elif orden == 5:
		break

	else:
		print("ERROR: No has introducido el número correcto")
		print("")
