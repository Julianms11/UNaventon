import string
import random

def generar_codigo():
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        codigo = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    return codigo

codigo_generado = generar_codigo()
