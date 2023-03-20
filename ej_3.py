""" Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
"""

def dev_dic(cadena):
    dicc = {}
    lista = cadena.split(" ")
    for pal in lista:
        dicc[pal] = lista.count(pal)
    return dicc
