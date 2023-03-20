"""Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva"""

def get_int():
    entrada = input("Ingrese un valor")
    try:
        entrada_int = int(entrada)
    except ValueError:
        print("Debe ingresar un valor numérico entero")
        get_int()
    print(f"El numero es entero es: {entrada_int}")


def get_int2():
    while True:
        entrada = input("Ingrese un valor")
        try:
            entrada_int = int(entrada)
            break
        except ValueError:
            print("Debe ingresar un valor numérico entero")
    print(f"El numero es entero es: {entrada_int}")



