#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma
#de los números introducidos coincida con el número inicial.
#El programa termina escribiendo la lista de números.
limite = int(input("Escriba un valor límite: "))
numero = int(input("Escriba un numero: "))
list_num = [numero]
while numero > limite:
    print(f"{numero} supera el limite")
    numero = int(input("Escribe otro valor: "))
    numero = numero
    list_num.append(numero)
while sum(list_num) != limite:
    numero_2 = int(input("Escribe otro valor: "))
    list_num.append(numero_2)
    while sum(list_num) > limite:
        list_num.remove(numero_2)
        print(f'{numero_2} es mayor que {limite}')
        list_num.append(numero_2)
print(f'El limite es {limite}. La lista es: ', end="")
for i in range(len(list_num)):
    if i == len(list_num)+1:
        print(list_num[i])
    else:
        print(list_num[i], end=", ")