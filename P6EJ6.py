#Escribe un programa que pida primero dos números (máximo y mínimo)y que después te pida números intermedios.
#Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
#El programa termina escribiendo la lista de números.

minimo = int(input("Escribe un número: "))
maximo = int(input(f'Escribe un número mayor a {minimo}: '))
list = []
while minimo >= maximo:
    numero = int(input(f"{maximo} no es mayor que {minimo}."))

numero = int(input(f"Escriba un numero entre {minimo} y {maximo}: "))
while minimo <= numero <= maximo:
    list.append(numero)
    numero = int(input(f"Escriba un numero entre {minimo} y {maximo}: "))
print("Los numeros que has escrito son: ", end="")
for i in range (len(list)):
    if i == len(list)+1:
        print(list[i])
    else:
        print(list[i], end=", ")