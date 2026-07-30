import requests

saldo = 0

while True:
    try:
        orden = input('Escribe "compra" para comprar BTC o "saldo" para ver tu saldo: ').strip()
        orden_corregida = orden.lower()
        if orden_corregida == "compra":
            try:
                monto = float(input("Cuanto BTC quieres: "))
                if monto > 0:
                    saldo += monto
                else:
                    print("La cantidad debe ser mayor a cero.")
            except ValueError:
                print("Error, Debes introducir un número válido.")
        elif orden_corregida == "saldo":
            print(f"Saldo actual: {saldo} BTC")
        else:
            print("Operación no existente.")
    except EOFError:
        print("\n--- CERRANDO SESIÓN ---")
        try:
            request = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            request_json = request.json()
            precio_btc = float(request_json["price"])
            saldo_en_dolares = precio_btc * saldo
            print(f"Tu saldo es de {saldo} BTC, igual a ${saldo_en_dolares:,.2f}")
        except requests.RequestException:
            print(f"Tu saldo es de {saldo} BTC, pero no pudimos conectar con Binance para calcular el valor en USD.")
        break