productos =[
    {
        "nombre":"misa",
        "edad":123,
        "stock":10,
    },
    {
        "nombre":"pepe",
        "edad":343,
        "stock":15,
    },
    {
        "nombre":"macaco",
        "edad":2323,
        "stock":24,
    },
]

carrito =[
    {
        "nombre":"misa",
        "edad":123,
        "stock":40,
        "cantidad":8
    },
    {
        "nombre":"pepe",
        "edad":343,
        "stock":30,
        "cantidad":7
    },
]
for i in carrito:
    nuevoStock= i["cantidad"] + i["stock"]
    #nuevoStock = es igual a 37
    print(nuevoStock)
    i["stock"] = nuevoStock
    print(i)