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

