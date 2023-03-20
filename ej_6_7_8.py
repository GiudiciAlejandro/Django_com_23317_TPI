"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""


class Persona:
    def __init__(self, nombre="",edad=0,dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni 
        
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    def validar_nombre(self):
        if len(self.__nombre) < 2:
            print("Nombre invalido, debe tener más de 2 caracteres")
            self.__dni = ""

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
        self.validar_nombre()

    def validar_dni(self):
        if not type(self._dni) == int:
            print("DNI invalido")
            self._dni = ""

    @dni.setter
    def dni(self, dni):
        self._dni=dni
        self.validar_dni()
      
    def validar_edad(self):
        if self.__edad < 0:
            print("Edad incorrecta")
            self.__edad=0


    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        self.validar_edad()
    
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {str(self.__edad)}")
        print(f"DNI: {self.__dni}")


    def esMayorDeEdad(self):
        return self.edad >= 18


"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos"""



class Cuenta(Persona):
    def __init__(self, nombre, cantidad=0.0):
        super().__init__(self, nombre)
        self.__titular = nombre
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular=titular


    def retirar(self,cantidad):
        if cantidad > 0 :
            self.__cantidad -= cantidad
        else:
            if cantidad <=0:
                print("Debe ingresar un valor positivo de dinero a retirar")
            return
        print(f"Transaccion completada satisfactoriamente, su saldo es de: {self.__cantidad}")
    

    def ingresar(self, cantidad):
        if cantidad > 0 :
            self.__cantidad += cantidad
        else:
            if cantidad <=0:
                print("Debe ingresar un valor positivo de dinero a retirar")
            return
        return print(f"Transaccion completada satisfactoriamente, su saldo es de: {self.__cantidad}")
      
    
    def mostrar(self):
        print("Titular de la cuenta: " , self.__titular)
        print("Saldo: ", self.__cantidad)

pers1=Persona("Ale",30,22061)
titular=pers1.mostrar()
count=Cuenta(titular,1000)
count.mostrar
count.retirar(500)
count.mostrar
    
"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta"""


class CuentaJoven(Cuenta):
    def __init__(self, titular ,  cantidad=0.0 , bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
        
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        if bonificacion > 0:
            self.__bonificacion=bonificacion


    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()


    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        print(f"Titular: {self.titular.mostrar()}")
        print(f"Cantidad: {str(self.cantidad)}")
        print(f"Bonificación: {str(self.bonificacion)} %")
   



