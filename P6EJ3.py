#Escribe un programa que pida notas y los guarde en una lista.
#Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
#El programa termina escribiendo la lista de notas.
num = float(input("Escriba una nota: "))
lista = []
while 10 >= num >= 0:
    lista += [num]
    num = float(input("Escriba otra nota: "))
print(lista)