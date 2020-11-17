#Escribe un programa que te pida números y los guarde en una lista.
#Para terminar de introducir número, simplemente escribe “Salir”.
#El programa termina escribiendo la lista de números.
num = str(input("Escribe un número: "))
lista = []
while num != "Salir":
    lista += [num]
    num = str(input("Escriba otro número: "))
print(lista)
