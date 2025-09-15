from tree import BinaryTree

# nombre, altura y peso

# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo
# de baja;


star_wars_tree_name = BinaryTree()
star_wars_tree_id = BinaryTree()

characters = [('Yoda', 1), ('Darth Vader', 2), ('Boba Fett', 3), ('Grogu', 4), ('Mando', 5), ('Han Solo', 6), ('Palpatine', 9), ('Mace Windu', 10)]

from random import randint
for character in characters:
    info = {
        'weight': randint(10, 100),
        'height': randint(40, 190),
    }
    info.update({'id': character[1]})
    star_wars_tree_name.insert(character[0], info)

    info2 = info.copy()
    info2.pop('id')
    info2.update({'name': character[0]})
    star_wars_tree_id.insert(character[1], info2)


star_wars_tree_name.in_order()
print()

# punto b
star_wars_tree_name.insert('R2-D2', {'weight': 100, 'height': 85, 'id': 15})
star_wars_tree_id.insert(15, {'weight': 100, 'height': 85, 'name': 'R2-D2'})
value, other_value = star_wars_tree_name.delete('Palpatine')
star_wars_tree_id.delete(other_value['id'])

pos = star_wars_tree_name.search('R2-D2')
if pos is not None:
    pos.other_values['weight'] = 115
    pos.other_values['height'] = 71

value, other_values = star_wars_tree_name.delete('Mando')
if value is not None:
    new_value = 'Din Djarin'
    star_wars_tree_name.insert(new_value, other_values)
    pos = star_wars_tree_id.search(other_values['id'])
    pos.other_values['name'] = new_value


# print('buscando', star_wars_tree_name.search('Din Djarin').value)

# punto C
pos = star_wars_tree_name.search('Yoda')
if pos is not None:
    print(f'search character {pos.value}, character info {pos.other_values}')
pos = star_wars_tree_name.search('Boba Fett')
if pos is not None:
    print(f'search character {pos.value}, character info {pos.other_values}')

print()

# puntos d
star_wars_tree_name.in_order_height()
print()

# punto e
star_wars_tree_name.in_order_weight()
print()

star_wars_tree_name.in_order()
print()

star_wars_tree_id.in_order()
print()