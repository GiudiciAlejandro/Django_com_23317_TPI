""". Escribir una función que calcule el mínimo común múltiplo entre dos números"""
# Formula de mcm(a, b) = (a * b) / mcd(a, b)

from ej_1 import mcd

def mcm(a, b):
    min_com_mul = (a * b) / mcd(a, b)
    return min_com_mul