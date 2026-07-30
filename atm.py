saldo = 1000
while True:
    retiro = float(input("Cuanto dinero deseas retirar o presiona 0 para salir: "))
    if retiro == 0:
        print("Adios")
        break
    elif retiro> saldo:
        print("Fondos insuficientes, no puedes retirar mas de tu saldo actual")
    elif retiro <= saldo:
        saldo= float(saldo - retiro)
        print(f"Retiro exitoso, saldo restante de {saldo:.2f}$")
    if saldo==0:
        print("Te has quedado sin dinero, el sistema se cerrara automaticamente")
        break