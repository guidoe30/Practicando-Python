### Loops ### Bucles ###

#While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #Es opcional
    print("Mi condición es mayor o igual que 10")
    
print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break    
    print(my_condition)
    
print("La ejecucion continua")

#For

my_list = [35, 24, 62, 52, 30, 30, 17]


for element in my_list:
    print(element)
    
my_tuple = (22, 1.83, "Guido", "Enriquez", "Guido")
for element in my_tuple:
    print(element)
    
my_set = {"Guido", "Enriquez", 22} 
for element in my_set:
    print(element)

my_dict = {"Nombre":"Guido", "Apellido":"Enriquez", "Edad":22, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecucion continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")