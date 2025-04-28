from queue_ import Queue
from random import randint


queue_letters = Queue()

for i in range(15):
    queue_letters.arrive(chr(randint(65, 90)))


queue_letters.show()
print()
for i in range(queue_letters.size()):
    if queue_letters.on_front() in ["A", "E", "I", "O", "U"]:
        queue_letters.attention()
    else:
        queue_letters.move_to_end()
print()
queue_letters.show()

# queue_numbers = Queue()

# queue_positive = Queue()
# queue_negative = Queue()

# for i in range(15):
#     number = randint(-100, 100)
#     queue_numbers.arrive(number)

# queue_numbers.show()

# max_value, min_value = queue_numbers.on_front(), queue_numbers.on_front()

# negative_numbers = 0
# while queue_numbers.size() > 0:
#     number = queue_numbers.attention()
#     if number < 0:
#         negative_numbers +=1
    
#     if number < min_value:
#         min_value = number
    
#     if number > max_value:
#         max_value = number

# print(f'cantidad de negativos {negative_numbers}')
# print(f'el rango es {max_value - min_value}')


# while queue_numbers.size() > 0:
#     number = queue_numbers.attention()
#     if number > 0:
#         queue_positive.arrive(number)
#     elif number < 0:
#         queue_negative.arrive(number)

# print()
# queue_positive.show()
# print()
# queue_negative.show()