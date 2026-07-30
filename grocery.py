lista = {}
while True:
    try:
        item = input("")
        item_mayuscula = item.upper()
        if item_mayuscula in lista:
            lista[item_mayuscula]+= 1
        else:
            lista[item_mayuscula] = 1
    except EOFError:
        print()
        break

for item_mayuscula in sorted(lista):
    print(lista[item_mayuscula], item_mayuscula)