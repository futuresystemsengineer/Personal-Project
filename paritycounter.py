numero_inicio = int(input("Introduce un numero de inicio: "))
numero_final = int(input("Introduce un numero final: "))
contador_numeros_pares= 0
contador_numeros_impares=0
for i in range(numero_inicio, numero_final +1):
    if i %2 ==0:
        contador_numeros_pares +=1
    else:
        contador_numeros_impares +=1

print(f"Hubo {contador_numeros_pares} numeros pares y {contador_numeros_impares} numeros impares")
