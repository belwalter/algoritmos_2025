from list_ import List

class Person:
    
    def __init__(self, nom, ape, dni):
        self.nom = nom
        self.ape = ape
        self.dni = dni
    
    def __str__(self):
        return f"{self.ape}, {self.nom} - {self.dni}"

def order_by_name(item):
    return item.nom

def order_by_surname(item):
    return item.ape

def order_by_id(item):
    return item.dni    

people = [
    Person(nom='Juana', ape='Gonzalez', dni=45),
    Person(nom='Mariano', ape='Perez', dni=32),
    Person(nom='Mariano', ape='Perez', dni=51),
    Person(nom='Carlos', ape='Romero', dni=14),
    Person(nom='Ana', ape='Cordoba', dni=29),
]

list_people = List()
list_people.add_criterion('nombre', order_by_name)
list_people.add_criterion('dni', order_by_id)
list_people.add_criterion('apellido', order_by_surname)

for person in people:
    list_people.append(person)

# print(list_people.search(51, 'dni'))
# print(list_people.delete_value('Gonzalez'))
list_people.sort_by_criterion('dni')

print()
list_people.show()
