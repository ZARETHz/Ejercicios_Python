#definir o declarar una funcion
def test():
    print("inpresion desde fucnion")

#invocacion de una funcion 
test()

#las variables puedenser mutables 
def test2(nombre = "desconocido",carrera="sin carrera"):
    print(f"hola {nombre} tu carrera es {carrera}" )

test2(carrera="sistemas")    

#funcion que retorna un valor 
def test3(valor1,valor2):
    return int(valor1)+int(valor2)
#parceaseoo 
print(f"El resultado es {test3(24,10)}")

#capturar datos por terminal 
numero= input("Ingresa un numero")
print(type(numero))
numero = int (numero)
print(type(numero))
print(f"impresion de numero {numero}")
