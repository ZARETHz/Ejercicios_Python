datos = [1,2,3,4,5]
print(f"Lista original: {datos}")


copia_datos = datos 
print(f"liasta 2: {copia_datos}")
copia_datos.append(6)
print(f"Lista original {datos}")
print(f"Lista 2: {copia_datos}")
#forma adecuada de hacer una copia de una lista con desempaquetamiento 
#forma correcta de copiar una lista es
#aqui vamos a desempaquetar al arreglo original y crear uno nuevo con los mismos elementos
copia_datos = [*datos]
print(*datos)

def impresion_nombres (*nombres): 
   #el print con la f no te permite desenpaquetar 
    print(f"Los nombres son",*nombres)
    #recibe todo de manera de una tipla 
    #la impresion de nombres es una tupla por lo tanto no se pueden modificar los elementos de la tupla pero si se pueden modificar las variables que apuntan a la tupla
impresion_nombres("diego","juan","ana","maria")



def impresion_datos(**data):
    print(f"Lostaos son {data}")
    
impresion_datos(nombre ="diego",tel=5512307753,carrera="sistemas" )
diccionario_datos={"marca":"DELL","modelo":"XPS 15","año":2022}
copia_diccionario ={**diccionario_datos}
impresion_datos(**diccionario_datos)
