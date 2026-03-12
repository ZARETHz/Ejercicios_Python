class Tabla: 
    def __init__(self,nombre):
        self.__nombre = nombre 
        self.__datos = []
        self.__id = 0
        self.__historial = []
        
    def mostrarDatos(self):
        print(f"Datos tabla{self.__nombre}:{self.__datos}")
        
    def incrementarId(self):
        self.__id +=1
        
    def insercion(self,datos):
        self.incrementarId()
        contenido = {**datos}
        contenido["id"]= self.__id
        self.__datos.append(contenido)
        print(f"Los datos fueron añadidios a la tabla ".center(50,"*"))
        self.__historial.append({"accion":"insertar","datos":contenido})
        
    def busquedaCampo(self,campo,valor,cantidad =0):
        encontrado =False 
        if campo in self.__datos[0].keys():
            
            for registro in self.__datos:
                if registro[campo] ==valor:
                    encontrado=True
                    return (registro)
                    if not cantidad :
                        break
            if not encontrado:
                print(f"No se localizo el registro ")
        else:
                    print(f"El campo {campo} no existe en la tabla ")

    def editar(self,id,valor,campo):
        encontrado = False
        for posicion in range(len(self.__datos)):
            if self.__datos[posicion]["id"] == id:
                valor_anterior = self.__datos[posicion][campo]
                self.__datos[posicion][campo]= valor
                print(f"Registro actualizado correctamente")
                self.__historial.append({
                    "accion":"editar",
                    "id":id,"campo":campo,
                    "valor_anterior":valor_anterior,
                    "valor_nuevo":valor})
                encontrado = True
                break
        if not encontrado: 
            print("Registro  no localizado ")
    
    def eliminar(self,id:int=0):
        for posicion in range (len(self.__datos)):
            if self.__datos[posicion]["id"] == id:
                eliminado = self.__datos[posicion]
                self.__datos.pop(posicion)
                self.__historial.append({
                    "accion":"eliminar",
                    "id":id,
                    "datos_eliminados":eliminado
                }) 
                print("registro eliminado")
                break
                
        #lista_temporal = []
        #for registro in self.__datos: 
          #  if registro["id"] != id:
           #     lista_temporal.append(registro)
       # self.__datos = lista_temporal
    def mostrarHistorial(self):
        print("Historial de acciones:")
        for cambio in self.__historial:
            print(cambio)