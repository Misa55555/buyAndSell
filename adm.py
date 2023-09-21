from base_datos import lista_producto,ultimo_id

def llamarMenu():
    from menuAdm import menuAdm
    menuAdm()


def crearProducto(): ##PARA ADMIN 4
    while True:
        try:
            nombre = input("Nombre del producto: ")
            stock = int(input("Stcok del producto: "))
            precio = int(input("Precio del producto: "))
            if stock < 0 or precio <= 0:
                print("No puedes poner valores negativos")
                continue
            global ultimo_id
            ultimo_id +=1
            producto = {
                "Nombre:":nombre,
                "stock":stock,
                "precio":precio,
                "id":ultimo_id
            }
            lista_producto.append(producto)
            consultarStock()
            llamarMenu()
            break
        except ValueError:
            print("Debes de colocar los valores correctos")
            continue
       
    
def consultarStockForMenu():
    while True:
        for i in lista_producto:
            print(i)
        break
    llamarMenu()

def consultarStock(): ##PARA ADMIN(opcion 1)
    while True:
        for i in lista_producto:
            print(i)
        break
    

def modiStock(): ##opcion 2
    while True:
        try:
            print("---Estos son los productos que hay en Stock---")
            consultarStock()
            respuesta_admin2 = int(input("ID del producto que quieres modificar: "))
            productoEncontrado = None
            for p in lista_producto:
                if p["id"] == respuesta_admin2:
                    productoEncontrado = p
                    print(productoEncontrado)
                    break
            else:
                print("Error, producto no encontrado")
                continue

        except ValueError:
            print("Error, debes de colocar ID numerico")
            continue

        try:
            while True:
                respuesta_admin3 = int(input("----cuanto de stock le quieres agregar----: "))
                if respuesta_admin3 * -1 > p["stock"] and respuesta_admin3 < 0:
                    print("No puedes quitar mas de lo que tienes ❌")
                    continue
                else:
                    p["stock"] = p["stock"] + respuesta_admin3
                    print(productoEncontrado)
                    llamarMenu()
                    break
            break
        except ValueError:
            print("Error, Vuelve a intentarlo")
            continue

def modiPrecio(): ##opcion 3
    while True:
        try:
            print("---Estos son los productos que hay en Stock---")
            consultarStock()
            respuesta_admin2 = int(input("ID del producto que quieres modificar el precio: "))
            productoEncontrado = None
            for p in lista_producto:
                if p["id"] == respuesta_admin2:
                    productoEncontrado = p
                    print(productoEncontrado)
                    break
            else:
                print("Error, producto no encontrado")
                continue

        except ValueError:
            print("Error, debes de colocar ID numerico")
            continue

        try:
            while True:
                respuesta_admin3 = int(input("----cuanto de precio le quieres colocar----: "))
                if respuesta_admin3 < 0:
                    print("No puedes poner un valor negativo")
                    continue
                else:
                    p["precio"] = respuesta_admin3
                    print(productoEncontrado)
                    llamarMenu()
                break
            break
        except ValueError:
            print("Error, Vuelve a intentarlo")
            continue


##########################################################



