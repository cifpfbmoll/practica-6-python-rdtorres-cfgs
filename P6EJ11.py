# Escribir un programa para jugar a adivinar un número
# (el ordenador "piensa" el número y el usuario lo ha de adivinar).
# El programa empieza pidiendo entre qué números está el número a adivinar,
# se "inventa" un número al azar y luego el usuario va probando valores.
# El programa va decidiendo si son demasiado grandes o pequeños. pista:
import random
min = int(input("Valor mínimo:"))
max = int(input("Valor máximo:"))
trys = 0
secret = random.randint(min, max)
print('Adivina un número entero entre ', min, 'y', max)
num = int(input("Escribe un número: "))
while (num != secret):
    while (num < secret):
        num = int(input("Muy pequeño. Vuelve a probar: "))
        trys += 1
    while (num > secret):
        num = int(input("Muy grande. Vuelve a probar: "))
        trys += 1
print("Enhorabuena. Has hecho ", trys, "intentos.")
