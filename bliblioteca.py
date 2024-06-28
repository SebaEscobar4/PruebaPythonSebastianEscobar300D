import os
import time
import json
datos=[]
edit_cliente = []

def registro():
    nombre= input("ingrese su nombre: ")
    email = input("ingrese su email: ")
    fecha = input("ingrese la fecha de hoy: ")
    datos = [nombre,email,fecha]

 
    return 

def editar ():
    editarNombre: input("ingrese su nuevo nombre: ")
    editarEmail : input("ingrese su nuevo email: ")
    editarfecha: input("ingrese la nueva fecha de hoy: ")

    edit_cliente = [editarNombre,editarEmail,editarfecha ]

    return

print("#"*10,"Bienvenido a libro mundo", "#"*10)
while True:
    print("*"*10,"Mundo Libro","*"*10 )
    print( "[1]- Mantenedor de usuarios \n [2]- Reportes \n [3]- Salir" )
    opcionp = input("ingresa una opcion(1-3)... :")

    if opcionp == "1":
        print("Bienvenido al mantenedor de usuarios")
        print("1. agregar usuario \n 2. Editar usuario \n 3. Buscar usuario \n 4. Volver")
        editaro= input("ingrese una opcion(1-2):")
        if editaro == "1":
            while True :
                print("Bienvenido nuevo usuario!!!")
                agregar_usuario = registro()
                print("Desea agregar un nuevo usuario? \n 1.SI \n 2.NO ")
                opcion = input("ingresa una opcion... :").lower()
                if opcion == "si":
                    print("Redirigiendo...")
                else:
                    print("Gracias por regristrarte!!!!")
                    break
        elif editaro == "2":
            while True :
                print("Editar Usuario")
                agregar_usuario = editar()
                print("Desea editar otro usuario? \n 1.SI \n 2.NO ")
                opcion = input("ingresa una opcion... :").lower()
                if opcion == "si":
                    print("Redirigiendo...")
                else:
                    print("Gracias por venir!!!!")
                    break
        elif editaro == "3":
            print("Eliminar Usuario")
            agregar_usuario.pop()
            print("el Ultmo usuruario creado a sido eliminado")

        elif editaro == "4":
            print("Volviendo al menu....")
        else:
            ("ingresa una opcion valida:")
            
    elif opcionp == "2":
        print("bienvenido a los reportes")
        for usuario in agregar_usuario:
            print(usuario)

    elif opcionp== "3" :
        print("Saliendo...")
        break
    else:
        print("ingresa una opcion valida....")






