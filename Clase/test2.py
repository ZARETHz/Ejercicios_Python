#ciclo de repeticion while 
contador =0
while contador <= 5:
    print("buvle infinito")
    contador +=1
    #if contador >= 5:
       # break
       
#lista
lista_frutas:list = []
lista_alterna:list = list()
#impresion de una lista 
print(lista_frutas)
print(lista_alterna)

print(type(lista_frutas))
print(type(lista_alterna))
#funciones de las listas 
lista_frutas.append("manzana")
lista_frutas.append("manngo")
lista_frutas.append("mandarina")
print(len(lista_frutas))#len es para saber la cantidad de elementos que tiene la lista

#insercion de un nuevo elemnto con la fucion insert 
#requiere una posicion de un valor 
lista_frutas.insert(1,"pera")

lista_frutas.pop()#elimina el ultimo elemento de la lista 
#remoover un lemento de una lista con la fucnion remove 
lista_frutas.remove("manzana")

#limpiar una lista con la fucnion clear
lista_frutas.clear()

#del se encarga de eliminar toda la lista de frutas 
#del lista_frutas
print(lista_frutas)

#recorrer una lista 
for i in lista_frutas:
    print(i,end=",")
    
print("\n")

for i in range(len(lista_frutas)):
    print(lista_frutas[i],end=",")
    
print(lista_frutas[0])#acceder a un elemento de la lista por su indice
#cambiar el valor de ina posicion de la lista -
lista_frutas[1] = "naranja"
print(lista_frutas)

#lista
lista_frutas:list=[]   
lista_alterna:list= list()
#impresion de una lista
print(lista_frutas)
print(lista_alterna)  
#impresion de tipo de dato
print(type(lista_frutas))
print(type(lista_alterna))
#funciones de las listas
lista_frutas.append("manzana")   #mide lo elementos al final de la lista
lista_frutas.append("mango")
lista_frutas.append("mandarina")
#cuenta los elementos de una lista con la funcion len()
print(len(lista_frutas))
#inserta un nuevo elemento y si el lugar esta ocupado desplaza el elemento con la funcion insert()
#requiere una posicion y un valor
lista_frutas.insert(1,"pera")
#elimina el ultimo elemento de una lista
#lista_frutas.pop()
#tambien devuelve el valor y elimina
#print(lista_frutas.pop())
#remover un elemento de una lista con la funcion remove()
#lista_frutas.remove("manzana")
#limpiar una lista con la funcion clear()
#lista_frutas.clear()
#elimina una lista
#del lista_frutas
print(lista_frutas)

for i in lista_frutas:
    print(i,end=",")
    
print("")
#recorrer una lista cn for normal
for i in range(len(lista_frutas)):
    print(lista_frutas[i])
    
#impresion de una posicion especifica
print(lista_frutas[0])
#cambiar valor de una posicion
lista_frutas[i]= "naranja"
#print(lista_frutas)
lista_frutas[1]="naranjas"
lista_frutas.append("manzana")
lista_frutas.append("mango")
lista_frutas.append("mandarina")
#elige por rango
print(lista_frutas[-2:]) #si es -va de derecha a izquierda

#tuplas
#2 formas de tupla vacia
tupla_nombres = ("edi","jesuan","lore","michel")
tupla_alterna = tuple()
#imprimir tipo de dato
print(type(tupla_nombres))
#impresion por posicion
print(tupla_nombres[2])
#impresion total por iteracion   tupla=datos que no cambiaran
for nombre in tupla_nombres:
    print(nombre)
#borrar de una tupla
#del tupla_nombres
print(tupla_nombres)

lista_nombres = []
for i in tupla_nombres:
    lista_nombres.append(i)
    
print(tupla_nombres)
lista_nombres.append("jorge")
lista_nombres.append("karla")
print(lista_nombres)
tupla_nombres = tuple(lista_nombres)
print(tupla_nombres)


#coleccion set
colleccion={'tierra','marte','jupiter','saturno','pluton'}
colleccion_alterna = set()
#impresion de tipo de dato
print(type(colleccion))
print(type(colleccion_alterna))
#impresion de todos los elementos
print(colleccion)
#añadir un nuevo elemento a una coleccion
#no se pueden repetir elementos
colleccion.add('mercurio')
#update sirve para añadir elementos a partir de otra estructura de datos
colleccion.update(lista_frutas)
colleccion.update(tupla_nombres)
#descartar un elemento de una collecion,si no existe el elemento mandara un error
colleccion.remove('pluton')
#descartar un elemento,si no existe no manda error
colleccion.discard('pluton')
#limpiar toda la coleccion
colleccion.clear()
print(colleccion)

#diccionarios
diccionario = {"nombre":"diego","carrera":"sis"}
diccionario_alterno = dict()

#impersion del tipo de dato
print(type(diccionario))
print(type(diccionario_alterno))
#mostrar un elemento especifico
print(diccionario['carrera'])
print(diccionario.get('nombre'))
#editar una key del diccionario
diccionario["nombre"]="Diego"
#añadir nuevos elementos
diccionario['semestre']=8

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for key,valor in diccionario.items():
    print(f"la key es: {key}, el valor es: {valor}")
#imprion general
print(diccionario)