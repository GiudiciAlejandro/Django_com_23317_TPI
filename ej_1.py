"""scribir una función que calcule el máximo común divisor entre dos números."""

def mcd(a, b):
    intermedio = 0
    while b != 0:
        intermedio = b
        b = a % b
        a = intermedio
    return a