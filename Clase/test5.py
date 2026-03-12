class Persona:
    #este es el metodo consturctor 
    #este se encarga de que tengamos todas nuestras propiedades principales para poder utilizarlas en nuestrpos otros metodo 
    #es decir es nuestro metodo principal que se considerarria como un metodo main 
    def __init__(self,nombre= "desocnocido ",apellido= "desconocido",edad= 20,correo="desconocido"):
        self.__nombre = nombre 
        self.__apellido= apellido
        self.__edad = edad 
        self.__correo = correo
        self.__id = 0
        self.__addId()
    #todas son propiedades privadas 
#si lleva dos giones bajos es porque es privao y si lleva una es porque no se pretende que no se va a modificar en apsoluto el programador 

    def __addId(self):
        self.__id +=1
    
    def mostrarDatos(self):   
        print(f"ID:{self.__id},nombre:{self.__nombre},apellido{self.__apellido},edad{self.__edad},correo{self.__correo}")  
    
    @property 
    #va a permiti que se comporte como un metodo get 
    #metodo para devolver el valor de la propiedad nombre 
    def nombre(self):
        return self.__nombre
    
    
    #va a permitir que se comporte como un metodo set
    #metodo para actualizar el valor de la propiedad nombre 
    #indicamos que acuara como un metodo set por lo tanto tambien se 
    #especificara el nombre de la propiedad seguido de un punto y la palabra  setter
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre 
    
    
persona1 = Persona("juanita","perez",20,"juannita@gmail.com")
    #print(persona1.nombre)
    #persona1.nombre = "carmen"
    #print(persona1.nombre)
persona1.mostrarDatos()
print(persona1.nombre)
persona1.nombre= "carmelita"
persona1.mostrarDatos()

