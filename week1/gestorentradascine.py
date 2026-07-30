asientos_libre = 10
dinero_recaudado = 0
while True:
    edad = int(input(f"Quedan {asientos_libre} asientos libres. Ingresa la edad del cliente (o escriba -1 para cerrar la taquilla): "))
    if edad == -1:
        break
    elif asientos_libre == 0:
        print("Sala llena, no se pueden vender mas entradas")
        break
    elif edad<5:
        entrada = 0
    elif edad <= 17:
        entrada = 5
    elif edad > 17:
        entrada = 10

    if asientos_libre >0:
        asientos_libre -= 1
        dinero_recaudado = dinero_recaudado + entrada
        print(f"Entrada vendida, precio {entrada}$. Asientos restantes: {asientos_libre}.")

asientos_vendidos = 10 - asientos_libre
print(f"Se vendieron {asientos_vendidos} entradas y se gano {dinero_recaudado}$.")