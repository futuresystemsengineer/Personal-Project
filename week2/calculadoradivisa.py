import requests
import json

while True:
    try:
        monto = float(input("Monto: $"))
        consulta_precio = requests.get("https://ve.dolarapi.com/v1/dolares/oficial")
        precio_json = consulta_precio.json()
        precio = precio_json["promedio"]
        precio_redondeado = round(precio, 2)
        monto_en_bs = monto * precio_redondeado
        print(f"{monto_en_bs:.2f} Bs.")
        break
    except ValueError:
        print("Solo se aceptan numeros.")
    except requests.RequestException:
        print("No ha sido posible consultar el precio.")