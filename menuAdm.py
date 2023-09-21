from adm import crearProducto,modiStock,modiPrecio,consultarStockForMenu
from login import login
def menuAdm():
    menu_admin = {
        "-":"-----------------------------",
        1:"visualizar productos y stock",
        2:"modificar stock a los productos",
        3:"modificar precio a los productos",
        4:"Crear nuevos productos",
        5:"Salir de la aplicacion",
        "--":"------------------------------"
    }
    for c,v in menu_admin.items():
        print(c,v)
    respuesta_admin = input("Eligue una opcion(1-4): ")
    while True:
        try:
            if respuesta_admin == "1":
                consultarStockForMenu()
                break
            elif respuesta_admin == "2":
                print("respuesta 2")
                modiStock()
                break
            elif respuesta_admin == "3":
                print("Respuesta 3")
                modiPrecio()
                break
            elif respuesta_admin == "4":
                crearProducto()
                print("Respuesta 4")
                break
            elif respuesta_admin == "5":
                print("--Saliendo de la aplicacion--")
                pepe = login()
                pepe
                break
            else:
                print("Error debes de colocar una opcion (1-4)")#es que no puedo hacer que retorne neuvamente al menuAdm
                menuAdm()
        except ValueError:
            print("Error debes de colocar una opcion (1-4)")
            continue



