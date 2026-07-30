import random

numero = random.randint(1, 10)

while True:
    try:
        intento = int(input("Guess a number between 1 and 10: "))
        if intento == numero:
            print(f"Congratulations, you guessed correctly, the number was {numero}")
            break
        else:
            print("Try again")
    except ValueError:
        print(f"That is not a number")