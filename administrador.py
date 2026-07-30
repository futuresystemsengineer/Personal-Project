almacen = {"Laptop": 5, "Monitor": 10, "Teclado": 8}

print("Introduce los productos en formato 'Producto-Cantidad' (Ctrl+D para terminar):")

while True:
    try:
        entrada = input("Entrada: ").strip()
        if "-" in entrada:
            producto, cantidad = entrada.split("-")
            producto_corregido = producto.title()
            cantidad_corregida = int(cantidad)
            if cantidad_corregida >0:
                if producto_corregido in almacen:
                    almacen[producto_corregido] += cantidad_corregida
                else:
                    almacen[producto_corregido] = cantidad_corregida
            else:
                print("La cantidad debe ser mayor a cero")
    except ValueError:
        print("¡Error! La cantidad debe ser un número entero válido.")
    except EOFError:
        print("\n")
        break

for producto in sorted(almacen):
    print(f"- {producto}: {almacen[producto]} unidades")