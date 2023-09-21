usuario1 = {
    "nombre": "misa",
    "contraseña": 1234
}

admin = {
    "nombre": "admin",
    "contraseña": 567
}

def login():
    contador = 0
    while True or False:
        try:
            usuario = input("Nombre: ")
            contrasena = int(input("Contraseña: "))

            if usuario == usuario1["nombre"] and contrasena == usuario1["contraseña"]:
                print("usuario entro")
                from menu_user import menuUser
                menuUser()
                return "user"
            if usuario == admin["nombre"] and contrasena == admin["contraseña"]:
                print("admin entro")
                from menuAdm import menuAdm
                menuAdm()
                return "admin"
            else:
                contador += 1
                print(f"Contraseña o usuario no valido. intentos: {contador}/3")
                if contador == 3:
                    print("CUENTA BLOQUEADA")
                    break
        except ValueError:
            contador +=1 
            print(f"ERROR DE SINTAXIS {contador}/3")
            if contador == 3:
                    print("CUENTA BLOQUEADA")
                    break
