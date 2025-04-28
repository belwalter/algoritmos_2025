
class Person:
    
    def __init__(self, nom, ape, dni):
        self.nom = nom
        self.ape = ape
        self.dni = dni
    
    def __str__(self):
        return f"{self.ape}, {self.nom} - {self.dni}"


class List(list):
    pass


def show(list: list):
    for i in list:
        print(i)

def delete_value(list, key):
    pass

def insert_value(list, value):
    pass

def sort(list):
    pass

# list_number = List()

people = [
    Person(nom='Juana', ape='Gonzalez', dni=45),
    Person(nom='Mariano', ape='Perez', dni=32),
    Person(nom='Mariano', ape='Perez', dni=51),
    Person(nom='Carlos', ape='Romero', dni=14),
    Person(nom='Ana', ape='Cordoba', dni=29),
]

list_people = List()

for person in people:
    list_people.append(person)

# list_number.append(2)
# list_number.append(1)
# list_number.append(20)

# list_number.insert(1, 11)

def order_by_name(item):
    return item.nom

def order_by_ape(item):
    return item.ape

def order_by_dni(item):
    return item.dni

def order_by_ape_nom(item):
    return item.ape+item.nom

list_people.sort(key=order_by_ape_nom)

# deleted_value = list_people.pop(2)
# deleted_value = list_people.remove(people[2])

# print(f'deleted value: {deleted_value}')

# print(type(list_number))
# print()

list_people[2].nom = 'Luke'
show(list_people)
