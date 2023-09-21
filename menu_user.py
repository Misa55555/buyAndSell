from login import login
from comprador import productosCompra,precioCompra,consultarStockForMenuUser
def menuUser():
    menu_user = {
        "-":"-----------------------------",
        1:"Visualizar menu de productos",
        2:"Comprar",#dentro se vizualiza el carrito
        3:"Salir de la aplicacion",
        "--":"------------------------------"
    }
    for c,v in menu_user.items():
        print(c,v)
    respuesta_user = input("Eligue una opcion(1-4): ")
    while True:
        if respuesta_user == "1":
            consultarStockForMenuUser()
            break
        elif respuesta_user == "2":
            print("respuesta 2")
            productosCompra() ##aca va comprar
            break
        elif respuesta_user == "3":
            print("--Saliendo de la aplicacion--")
            pepe = login()
            pepe
            break
        else:
            print("Debes de colocar una opcion del (1-4)")
            menuUser()

