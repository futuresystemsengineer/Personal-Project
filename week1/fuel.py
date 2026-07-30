from fractions import Fraction
while True:
    try:
        x = Fraction(input("How much fuel do you have left: "))
    except ValueError:
        pass
    else:
        porcentaje = float(x * 100)
        if porcentaje <=100:
            print(f"Fuel: {porcentaje:.2f}%")
            break
        else:
            continue