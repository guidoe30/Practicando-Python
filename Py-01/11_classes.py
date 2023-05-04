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