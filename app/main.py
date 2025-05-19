import random

def jugar():
    numero_secreto = random.randint(1, 10)
    intentos = 3

    print("🎮 ¡Bienvenido al juego de Adivina el Número!")
    print("Tienes 3 intentos para adivinar un número del 1 al 10.")

    while intentos > 0:
        try:
            adivina = int(input("Ingresa tu número: "))
        except ValueError:
            print("❌ Solo se permiten números.")
            continue

        if adivina == numero_secreto:
            print("🎉 ¡Felicidades! ¡Adivinaste el número! Caz nunca cambies sos el mejor")
            return
        else:
            intentos -= 1
            print(f"❌ paila Incorrecto. Te quedan {intentos} intento(s).")

    print(f"😢 Se acabaron los intentos. El número era Caz gracias por todo {numero_secreto}.")

if __name__ == "__main__":
    jugar()