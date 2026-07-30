precios = {"General": 5, "Niño": 3, "Estudiante": 4}
venta = {"General": 0, "Niño": 0, "Estudiante": 0}
total = 0
while True:
    try:
        tipo = input("Tipo: ")
        tipo_corregido = tipo.title()
        if tipo_corregido in precios:
            venta[tipo_corregido]  += 1
            total += precios[tipo_corregido]
        else:
            print("El tipo de entrada no existe.")
    except EOFError:
        break

print("Resumen de ventas:")
for x in sorted(venta):
    if venta[x] >0:
        print(f"- {x} {venta[x]} unidades")

print(f"Total recaudado: {total} dolares")