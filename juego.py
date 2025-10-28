import random

puntaje = 0
intentos = 3

print("bienvenido a el juego")

while intentos > 0:
    numero = random.randint(1,10)
    adi = int(input("Cual es el numero entre 1 y 10:"))
    if numero == adi:
        print("lo has adivinado")
        puntaje += 1
    else:
        print("No has adivinado el numero, el numero era:", numero)
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
        print(f"Tu puntaje es: {puntaje} puntos")