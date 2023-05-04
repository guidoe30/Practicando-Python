### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Guido", "Apellido":"Enriquez", "Edad":22, 1:"Python"}

my_dict = {
    "Nombre": "Guido",
    "Apellido": "Enriquez",
    "Edad": 22,
    "Lenguajes": {"Python", "Swtift", "Kotlin"},
    1:1.83
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

(my_dict["Nombre"]) = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle WidoDev"
print(my_dict)

del my_dict["Calle"] # Eliminar 
print(my_dict)

print("Enriquez" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items()) #Tenemos un listados de cada uno de los items
print(my_dict.keys()) #Nos restorna el listado de los keys
print(my_dict.values()) #nos restorna todos los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, ["Widodev"])
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))  

print(my_new_dict.values())

print(tuple(my_new_dict))
print(set(my_new_dict))