ventas_hoy = [
    {"cliente": "Carlos", "monto": 50, "metodo_pago": "efectivo"},
    {"cliente": "Maria", "monto": 120, "metodo_pago": "tarjeta"},
    {"cliente": "Gianluca", "monto": 30, "metodo_pago": "efectivo"},
    {"cliente": "Sofia", "monto": 200, "metodo_pago": "tarjeta"},
    {"cliente": "Jose", "monto": 15, "metodo_pago": "efectivo"}
]

def resumen_ventas(transacciones, metodo_pago_buscado):
    ventas_total = 0
    cantidad_ventas = 0
    for x in transacciones:
        if x["metodo_pago"] == metodo_pago_buscado:
            cantidad_ventas +=  1
            ventas_total += x["monto"]
    return {"total_dinero": ventas_total, "cantidad_ventas": cantidad_ventas}


ventashoy = resumen_ventas(ventas_hoy, "efectivo")
print(ventashoy)