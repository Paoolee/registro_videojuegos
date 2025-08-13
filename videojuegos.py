videosjuegos = []

plataformas = ("PC", "PS5","xbox series X","Nintendo Switch")

while True:
    print("\n-- MENÚ DE VIDEOJUEGOS---")
    print("1. Registrar videojuego")
    print("2. Ver videojuego")
    print("3. Modificar videojuego")
    print("3.Eliminar videojuego")
    print("4.Salir ")

    opcion = input("Seleccione una opción (1-5):")

    if opcion =="1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
     pass
    elif opcion == "4":
       pass
    elif opcion == "5":
       print("Saliendo del programa.")
       break
    else:
       print("Opción invalida")

       if opcion == "1":
          codigo = int(input("Ingrese el código del videojuego:"))
          nombre = int(input("Ingrese el nombe del videojuego"))
          genero = input("Ingrese el genero del videojuego:") 

          print("\nplataformas disponiles")
          print("1.PC")
          print("2. PSS") 
          print("3. xbox series X") 
          print("4.Nintendo Switch")

          plataformas_codigo = int(input("Seleccione el núnero de la plataforma:"))
          plataforma = plataforma[plataformas_codigo -1]
          videosjuegos = {
             "codigo": codigo,
             "nombre": nombre,
             "genero": genero,
             "plataforma": plataforma
          }

          videosjuegos.append(videosjuegos)
          print("Videojuego registrado correcatmente")

       elif opcion == "2":
          if len(videosjuegos) == 0:
             print("No hay videojuegos registrados.")
          else:
             print("\n--- LISTA DE VIDEOJUEGOS---")
             for v in videosjuegos:
                print(f"codigo: {v["codigo"]}, nombre:{v["nombre"]}, Género:{v["genero"]},plataforma:{v["plataforma"]}")
       elif opcion == "3":
          codigo = int(input("Ingrese el codigo del videojuego a modificar:"))
          encontrado = False
          for v in videosjuegos:
             if v ["codigo"]== codigo:
                v ["nombre"]= input("nuevo nombre:")
                v ["genero"]= input("uevo genero:")

                print("\nplataformas disponibles:")
                print("1.PC")
                print("2.PSS")
                print("3.xbox series X")
                print("4.nintendo switch")
                plataformas_codigo = int(input("Seleccione el número de la nueva plataforma:"))
                v ["plataforma"] = plataformas[plataformas_codigo -1]

                print("Videosjuego modificado correctamente.")
                encontrado = True
                break
             if not encontrado:
                print("Videojuego no enconytrado.")
        elif opcion == "4":
          codigo = int(input("Ingrese el codigo del videojuego a eliminar:"))
          eliminado = False
          for v in videosjuegos:
             if v ["codigo"]== codigo:
                videosjuegos.remove(v)
                print("videojueg eliminado correctamente.")
                eliminado = True
                break
             if not eliminado:
                print("videojuego no encontrado")
                
                

                

             

          

            
                
    
