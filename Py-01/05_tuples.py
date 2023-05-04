### Tuples ### es un conjunto de valores 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.83, "Guido", "Enriquez", "Guido")
my_other_tuple = (35, 60, 30)

print (my_tuple)
print(type(my_tuple))

print (my_tuple[0])
print (my_tuple[-1])
#print (my_tuple[4]) Error fuera de rango
#print (my_tuple[-6]) Erorr

print (my_tuple.count("Guido"))
print(my_tuple.index("Enriquez"))
print (my_tuple.index("Guido"))

#my_tuple[1] = 1.90 Error no podemos asignar como tabla 

my_sum_tumple = my_tuple + my_other_tuple
print(my_sum_tumple)

print(my_sum_tumple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "GuidoDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
#print(my_tuple) NamError: name 'my_tuple' is not defined

