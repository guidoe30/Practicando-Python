### Strings ###
my_strings = "Mi String"
my_other_strings = "Mi otro String"

print(len(my_strings))
print(len(my_other_strings))

print(my_strings + " " + my_other_strings)

my_new_line_strings = "Este es un string\ncon salto de linea"
print(my_new_line_strings)

my_tab_strings = "\tEste es un string con tabulación"
print(my_tab_strings)

my_space_strings = "Este es un string \nescapado"
print(my_space_strings)


# Formateo

name, surname, age  = "Guido", "Enriquez", 22

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(surname, name, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #esta es la forma mas rapida 

# Desempaquetado de caracteres 
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

#Funciones

print(language.capitalize()) #primera letra mayuscula
print(language.upper()) #Todas las letras mayuscula
print(language.count("t")) #Cuanta los caracteres
print(language.isnumeric())
print("1".isnumeric())
print(language.lower()) #Todas las letras minusculas 
print(language.upper().isupper()) 
print(language.startswith("py")) #Si empieza con X caracter 
print(language.startswith("Py"))
print("Py" == "py") # No es lo mismo