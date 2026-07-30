weight = float(input("Weight of the item in kg: "))
price = float(input("Price of the item: "))

if weight <2:
    delivery = int(0)
elif weight <10:
    delivery = int(15)
else:
    delivery = int(30)

if price >200:
    descuento = int(10)
else:
    descuento = int(0)

total = price + delivery - descuento

if total < price:
    total = price
    
print(f"Delivery cost is {delivery:.2f}$")
print(f"Your total is {total:.2f}$")
