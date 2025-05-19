from list_ import List

# class Person:
    
#     def __init__(self, nom, ape, dni):
#         self.nom = nom
#         self.ape = ape
#         self.dni = dni
    
#     def __str__(self):
#         return f"{self.ape}, {self.nom} - {self.dni}"

# def order_by_name(item):
#     return item.nom

# def order_by_surname(item):
#     return item.ape

# def order_by_id(item):
#     return item.dni    

# people = [
#     Person(nom='Juana', ape='Gonzalez', dni=45),
#     Person(nom='Mariano', ape='Perez', dni=32),
#     Person(nom='Mariano', ape='Perez', dni=51),
#     Person(nom='Carlos', ape='Romero', dni=14),
#     Person(nom='Ana', ape='Cordoba', dni=29),
# ]

# list_people = List()
# list_people.add_criterion('nombre', order_by_name)
# list_people.add_criterion('dni', order_by_id)
# list_people.add_criterion('apellido', order_by_surname)

# for person in people:
#     list_people.append(person)

# # print(list_people.search(51, 'dni'))
# # print(list_people.delete_value('Gonzalez'))
# list_people.sort_by_criterion('dni')

# print()
# list_people.show()

from super_heroes_data import superheroes
class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villian):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villian = is_villian

    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villian}"

def order_by_name(item):
    return item.name

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)


for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villian=superhero["is_villian"],
    )
    list_superhero.append(hero)

#A eliminar a Groot
print(list_superhero.delete_value('Groot', 'name'))
print()
#B mostrar año aparicion wolverine
index = list_superhero.search('Wolverine', 'name')
if index:
    print(list_superhero[index].first_appearance)
else:
    print('el superheroe no esta ne la lista')

print()
#C modificar Dr strage de villano a heroe
index = list_superhero.search('Dr Strange', 'name')
if index:
    print(list_superhero[index].is_villian)
    list_superhero[index].is_villian = False
    print(list_superhero[index].is_villian)
else:
    print('el superheroe no esta ne la lista')

#D
print()
print('superheroes con traje')
for superhero in list_superhero:
    if 'armor' in superhero.short_bio or 'suite' in superhero.short_bio:
        print(superhero)

#H
print()
for superhero in list_superhero:
    if superhero.name.startswith(('Ba', 'Cap', 'Spi', 'Y')):
        print(superhero)

