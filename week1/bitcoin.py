import requests
import sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit(1)

try:
    numero = float(sys.argv[1])


    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    datos = response.json()

    precio = float(datos["price"])
    resultado = numero * precio

    print(f"${resultado:,.4f}")

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except requests.RequestException: 
    print("Error connecting to Bitcoin API")
    sys.exit(1)