"""Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia"""

from ej_3 import dev_dic

def tupla_rep(diccionario):
    maximo = 0
    pal_max = ""
    for pal in diccionario:
        if diccionario[pal] > maximo:
            maximo = diccionario[pal]
            pal_max = pal
    resultado=(pal_max, maximo)
    return tuple(resultado)

print(tupla_rep(dev_dic("ale pepe ale popo ale pepe")))