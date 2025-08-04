
tabla_letras = [None] * 10
tabla_numeros = [None] * 1000

legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

def hash_legion(codigo:str) -> int:
    h = 0
    for caracter in codigo:
        h = h * 33 + ord(caracter)
    return h

def hash_numerica(numero:int) -> int:
    return numero % 1000

from random import randint, choice

for i in range(2000):
    codigo = choice(legiones)
    numero = randint(1000, 9999)
    stromtrooper = f'{codigo}-{numero}'
    index = hash_legion(codigo) % len(tabla_letras)
    if tabla_letras[index] is None:
        tabla_letras[index] = []
    tabla_letras[index].append(stromtrooper)
    index = hash_numerica(numero)
    if tabla_numeros[index] is None:
        tabla_numeros[index] = []
    tabla_numeros[index].append(stromtrooper)




# for troopers in tabla_numeros:
#     if troopers is not None:
#         print(troopers)




# trooper = 'FN-2187'
# index = hash_legion(trooper[:2]) % len(tabla_letras)

# if tabla_letras[index] is not None:
#     print(trooper in tabla_letras[index])
# else:
#     print('no esta')

# numero = 1537
# index = hash_numerica(numero)
# print(tabla_numeros[index])

legion = 'CT'
index = hash_legion(legion) % len(tabla_letras)
print(tabla_letras[index])
