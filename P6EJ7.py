#Escribe un programa que pida un número (límite) y luego
#te pida números hasta que la suma de los números introducidos supere el límite inicial.
#El programa termina escribiendo la lista de números
limite = int(input("Escriba un valor límite: "))
numero = int(input("Escriba un numero: "))
max = numero
list = []

while max < limite:
    list.append(numero)
    numero = int(input("Escriba otro numero: "))
    max += numero
print()
print(f"La suma {max} de los valores supera el límite")
for i in range(len(list)):
    if i == len(list)+1:
        print(list[i])
    else:
        print(list[i], end=", ")