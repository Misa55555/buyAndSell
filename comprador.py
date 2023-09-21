from base_datos import lista_producto,carrito,monto_Carrito #usar para la suma/saber usar GLOBAL

def consultarStockForMenuUser():
    while True:
        for i in lista_producto:
            print(i)
        break
    irMenu()

def vaciarCompra():
    global monto_Carrito
    monto_Carrito = 0
    carrito.clear()
def irMenu():
    from menu_user import menuUser
    menuUser()

def eliminarUltimoCarrito():
    for p in carrito:
        p.popitem()


def pagarCarrito(): #MENU PARA PAGAR 
    global monto_Carrito
    formPagos = {
        "-":"-----------------",
        1:"Efectivo 10% OFF",
        2:"Credito 10% Recargo",
        3:"Debito",
        4: "cancelas compra",
        "_":f"_______________saldo pendiente:     ${monto_Carrito}"
    }
    while True:
        try:
            for c,v in formPagos.items():
                print(c,v)
                    
            opPago = input("Como quieres pagar: ")
            if opPago == "1":   
                monto_Carrito = monto_Carrito * 0.9
                print(f"Monto pagar: {monto_Carrito}")
                resp = input("Quieres pagar? (si o no): ")
                if resp == "si":
                    #debemos de ir al menu de compra de nuevo, pero con carrito vacio
                    print(f"Monto pagado: -{monto_Carrito}")
                    carrito.clear()
                    monto_Carrito = 0
                    eliminarUltimoCarrito()
                    from menu_user import menuUser
                    menuUser()
                    break
                elif resp == "no":
                    continue
                else:
                    print("Debes de poner SI O NO ❌")
                    continue
            elif opPago == "2":
                monto_Carrito = monto_Carrito / 0.9
                print(f"Monto pagar: {monto_Carrito}")
                resp = input("Quieres pagar? (si o no): ")
                if resp == "si":
                    #debemos de ir al menu de compra de nuevo, pero con carrito vacio
                    print(f"Monto pagado: -{monto_Carrito}")
                    eliminarUltimoCarrito()
                    vaciarCompra()
                    irMenu()
                elif resp == "no":
                    continue
                else:
                    print("Debes de poner SI O NO ❌")
                    continue
            elif opPago == "3":
                #debemos de ir al menu de compra de nuevo, pero con carrito vacio
                print(f"Monto pagar: {monto_Carrito}")
                resp = input("Quieres pagar? (si o no): ")
                if resp == "si":
                    print(f"Monto pagado: -{monto_Carrito}")
                    eliminarUltimoCarrito()
                    vaciarCompra()
                    irMenu()
                elif resp == "no":
                    continue
                else:
                    print("Debes de poner SI O NO❌")
                    continue
            elif opPago == "4":
                print("PAGO CANCELADO, VOLVIENDO AL MENU PRINCIPAL.")
                for i in carrito: #esto va para la opcion 4
                    nuevoStock= i["cantidad"] + i["stock"]
                    i["stock"] = nuevoStock
                    print(i)
                eliminarUltimoCarrito()
                vaciarCompra()
                irMenu()
                continue #esta mal 
                #aca lo que tengo que hacer, es eliminar montoCarrito = 0 y eliminar todo lo que este en el carrito
            else:
                print("Debes de colocar una de las opciones (1-4)❌")
                continue
            break
        except ValueError:
            print(SyntaxError)
            continue

def precioCompra():
    global monto_Carrito
    monto_Carrito = 0
    print("---CARRITO---")
    for p in carrito:
        monto_Carrito += p["precio"] * p["cantidad"]
        print(
            f"""
          [Nombre]:     {p["Nombre:"]} 
          [P/Unidad]:   {p["precio"]}
          [cantidad]:   {p["cantidad"]}             
                                    
                    """)
        
    print(f"TOTAL: {monto_Carrito}")
    pagarCarrito()




def productosCompra():
    cargarP = None
    while True:
        for i in lista_producto:
            print(i)
        try:
            compra = int(input("ID del producto quiere comprar? "))
            cantidad = int(input("Cantidad que que quieres del producto?"))
            if compra < 0 or cantidad < 0:
                print("No puedes indicar un numero negativo ❌")
                continue
            for p in lista_producto:
                if p["id"] == compra:
                    cargarP = p
                    p["stock"] = p["stock"] - cantidad
                    print(p["stock"])
                #elif cantidad > p["stock"]:
                    #print("Stock insuficiente ❌")
                    #productosCompra()
            
            if p["stock"] < cantidad:
                print("Stock insuficiente❌")
                continue
            cargarP["cantidad"] = cantidad  ##esto creo que hace que aparezca cantidad en Lista_productos 
            carrito.append(cargarP) 
            ask = input("Quieres seguir añadiendo productos?(si/no)")
            if ask == "si":
                continue
            elif ask == "no":
                print(carrito)
                break
            else:
                print("Error, debes de poner si o no ❌")
        except ValueError:
            print("Debes de colocar Valores validos❌")
            continue
    precioCompra()
