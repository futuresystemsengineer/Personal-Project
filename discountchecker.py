compra = float(input("How much was your total? "))

if compra >=100:
    porcentaje = 0.20
elif compra >=50:
    porcentaje= 0.10
else:
    porcentaje= 0.00

descuento = compra * porcentaje
total_compra = compra - descuento

print(f"El descuento aplicado fue de {porcentaje * 100:.0f}% (${descuento:.2f})")
print(f"El total fue {total_compra:.2f}$")