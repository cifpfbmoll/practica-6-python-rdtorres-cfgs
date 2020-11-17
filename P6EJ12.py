# Escribir un programa para jugar a adivinar un número
# el usuario piensa un número y el programa lo ha de adivinar).
# El programa empieza pidiendo entre qué números está el número
# a adivinar y luego intenta adivinar de qué número se trata. El
# usuario va diciendo si el número que ha dicho el programa es menor,
# mayor o igual al que se ha buscado.
import random

min = int(input("Valor mínimo:"))
max = int(input("Valor máximo:"))
while max <= min:
    max = int(input("%d es menor o igual que %d. Vuelve a poner otro número: " % (max, min)))
secret = random.randint(min, max)
print("Piensa un número enteroº entre", min, "y", max, "a ver si lo adivino.")
reply = input("Es %d ?: " % (secret))
while (reply != "igual"):
    while (reply == "mayor"):
        min = secret
        secret = random.randint(min, max)
        reply = input("Es %d ?: " % (secret))
    while (reply == "menor"):
        max = secret
        secret = random.randint(min, max)
        reply = input("Es %d ?: " % (secret))
    while (reply != "mayor") and (reply != "menor") and (reply != "igual"):
        reply = input(" Vuelve a intentar: ")
    if (max - min == 1) or (max == min):
        print("Syntax error :D. Se termina el juego")
        reply = "igual"
print("Nos vemos en la proxima")
