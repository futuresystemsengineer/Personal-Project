menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_cuenta = 0

while True:
    try:
        order = input("Item: ")
        item_formateado = order.title()

        if item_formateado in menu:
            total_cuenta += menu[item_formateado]
            print(f"Total: ${total_cuenta:.2f}")

    except EOFError:
        print() 
        break