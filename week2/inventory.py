productos = [
    {"nombre": "Teclado", "categoria": "tecnologia", "precio": 50},
    {"nombre": "Silla", "categoria": "muebles", "precio": 120},
    {"nombre": "Mouse", "categoria": "tecnologia", "precio": 25},
    {"nombre": "Monitor", "categoria": "tecnologia", "precio": 200},
    {"nombre": "Escritorio", "categoria": "muebles", "precio": 150}
]
def filtrar_productos(inventario, categoria_buscada, precio_maximo):
        lista_productos_posibles = []
        for x in inventario:
            if x["categoria"] == categoria_buscada and x["precio"] <= precio_maximo:
                lista_productos_posibles.append(x["nombre"])
        return lista_productos_posibles
