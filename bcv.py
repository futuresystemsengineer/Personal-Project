import requests

orden = requests.get("https://ve.dolarapi.com/v1/dolares/paralelo")
precio = orden.json()

print(precio["promedio"])