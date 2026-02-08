#hola mundo 
#no se conoce como string si no como de clae str de tipo texto 
texto:str="cadena de texto"

entero:int =10 
#no existe el double en python
flotante:float= 1.5
#es necesario empezar con masyuaculas en caso de False o True
booleano:bool=True

print("Hola mundo ")
#impresion de variables 
print(texto,entero)
#impresion con  escape de variables
#el f antes de las comillas es para indicar que vamos a usar variables dentro del string
print(f"este es el valor de una variable {flotante}")
print("este es un texto",booleano)

#funciones adicionales de print 
#.center es para decirle cuantos caracteres quieres tener es decir la palabra que tenemos ocupa 15 caracteres y le pusimos que ocupamos 25 por los tanto 
#habran 10 espacios adicionales que se reparten a la izquierda y derecha
print("menu de usuario".center(50,'-'))
print("texto de prueba",end=".")#el end es para indicar que al final de la impresion se ponga lo que le indiquemos
print("texto prueba2",end="\n\n")

#impresion de tipo de dato 
print(type(texto))
print(type(entero))
print(type(flotante))   
print(type(booleano))

#impresion de direccion de memoria
print(id(texto))
print(id(entero))       
print(id(flotante))
print(id(booleano))

#estructura de control 
if entero >0 and entero <100: 
    if entero <100:
        print("esta dentro del rango")
    else:
        print("esta fuera del rango")
else:
    print("es menor ")
    
#version mejorada 
    
if  0< entero <100: 
        print("esta dentro del rango")
else:
    print("es menor ")
    
    #elif
if 0< entero <=100: 
        print("esta dentro del rango")
elif entero <0:
        print("esta fuera del rango")
else:
    print("es menor ")
    
#ciclos de repeticion
for i in range(10):
    print(i,end=",")
    
#del 5 al 30 
for i in range(5,31):
    print(i,end=",")

#este va a ir de 5 en 5 
#posisiones primero inicio ,segundo final ,tercero ingremento
for i in range(5,31,5):
    print(i,end=",")

for letra in texto:
    print(letra,end="-")