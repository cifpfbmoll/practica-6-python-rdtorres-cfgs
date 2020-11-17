#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista.
#Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.
#El programa termina escribiendo la lista de números:
num1 = int(input("Escribe un número: "))
num2 = int(input(f'Escribe un número mayor a {num1}: '))
list = [num1]
while num1 < num2:
    num1 = num2
    list.append(num1)
    num2 =int(input(f'Escriba un número mayor qué {num2}: '))
print("Los numeros que has escrito son: ", end="")
for i in range (len(list)):
    if i == len(list)+1:
        print(lit[i])
    else:
        print(list[i], end=", ")