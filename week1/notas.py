while True:
    primer_corte = int(input("Primer corte: "))
    if 1 <= primer_corte <= 20:
        segundo_corte = int(input("Segundo corte: "))
        if 1 <= segundo_corte <= 20:
            break
        else:
            print("Las notas solo llegan hasta 20")
    else:
        print("Las notas solo llegan hasta 20")

resultado = ((primer_corte * 0.40) + (segundo_corte * 0.60))

print(f"Definitiva: {resultado}")