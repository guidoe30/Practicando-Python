### Classes ###

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname): 
        self.full_name = f"{name} {surname}"
        
    def walk (self):
      print(f"{self.full_name} esta caminando") 
    
my_person = Person("Guido", "Enriquez") 
print(my_person.full_name)
my_person.walk()

class Car:
    def __init__(self):
        self.color = "Rojo"
        self.marca = "Ferrari"
      

my_auto = Car()
print(f"{my_auto.color} {my_auto.marca}")