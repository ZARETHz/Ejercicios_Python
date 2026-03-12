from Pelicula import Pelicula
from Tabla import Tabla

tablaPeliculas = Tabla("Peliculas")

while True:
    print("\n" + "MI GESTOR DE PELICULAS".center(50,"*"))
    print("1. Agregar pelicula")
    print("2. Mostrar peliculas")
    print("3. Buscar pelicula")
    print("4. Editar pelicula")
    print("5. Eliminar pelicula")
    print("6. Mostrar historial de cambios")
    print("7. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    match opcion:
        
        case "1":
            titulo = input("Titulo: ")
            genero = input("Genero: ")
            descripcion = input("Descripcion: ")
            director = input("Director: ")
            
            pelicula = Pelicula(titulo,genero,descripcion,director)
            tablaPeliculas.insercion(pelicula.info())
        
        case "2":
            tablaPeliculas.mostrarDatos()
        
        case "3":
            campo = input("Campo a buscar (titulo,genero,descripcion,director,id): ")
            valor = input("Valor: ")
            if campo == "id":
                valor = int(valor)
            
            resultado = tablaPeliculas.busquedaCampo(campo,valor)
            if resultado:
                print("Registro encontrado:", resultado)
        
        case "4":
            id= int(input("ID de la pelicula que quieres editar "))
            print("\n1.Editar un solo campo")
            print("2.Editar varios campos")
            
            opcion_editar= input("Seleccione una opcion: ")
            
            match opcion_editar:
                case "1":
                    campo=input("Campo a editar (titulo,genero,descripcion,director): ")
                    valor = input("Nuevo valor: ")
                    tablaPeliculas.editar(id,valor,campo)
                case "2":
                    print("Ingrese los nuevos datos deje vacio si no quiere cambiarlo:   ")
                    nuevo_titulo = input("Nuevo titulo: ")
                    nuevo_genero = input("Nuevo genero: ")
                    nueva_descripcion = input("Nueva descripcion: ")
                    nuevo_director = input("Nuevo director: ")
                    if nuevo_titulo !="":
                        tablaPeliculas.editar(id,nuevo_titulo,"titulo")
                    if nuevo_genero !="":
                        tablaPeliculas.editar(id,nuevo_genero,"genero")
                    if nueva_descripcion !="":
                        tablaPeliculas.editar(id,nueva_descripcion,"descripcion")
                    if nuevo_director !="":
                        tablaPeliculas.editar(id,nuevo_director,"director")
                case _:
                    print("Opcion no valida")   
        
        case "5":
            id = int(input("ID de la pelicula a eliminar: "))
            tablaPeliculas.eliminar(id)
        
        case "6":
            tablaPeliculas.mostrarHistorial()
        
        case "7":
            print("Saliendo del sistema...")
            break
        
        case _:
            print("Opcion no valida")

print(f"Mi gestor de base de datos ".center(50,"*"))
pelicula1 = Pelicula("Spiderman", "Accion", "Pelicula del hombre araña", "Cesar Gonzalez")
pelicula2 = Pelicula("Spiderman 2", "Accion", "Pelicula del hombre araña 2", "Cesar Gonzalez")
pelicula3 = Pelicula("Spiderman 3", "Accion", "Pelicula del hombre araña 3", "Cesar Gonzalez")
pelicula4 = Pelicula("Spiderman 4", "Accion", "Pelicula del hombre araña", "Cesar Gonzalez")


tablaPeliculas = Tabla("Peliculas")
tablaPeliculas.insercion(pelicula1.info())
tablaPeliculas.insercion(pelicula2.info())
tablaPeliculas.insercion(pelicula3.info())
tablaPeliculas.insercion(pelicula4.info())
tablaPeliculas.mostrarTodos()
tablaPeliculas.busquedaCampo("titulo", "Spiderman")
tablaPeliculas.editar(4, "Spiderman 4", "titulo")
tablaPeliculas.busquedaCampo(4,"titulo", "Spiderman 4")
tablaPeliculas.eliminar(3)