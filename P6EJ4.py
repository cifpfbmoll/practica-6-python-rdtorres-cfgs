#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
#El programa termina escribiendo los dos números tal y como se pide:
num1 = int(input("Escribe un número: "))
num2 = int(input(f'Escribe un número mayor a {num1}: '))
while num2 <= num1:
    num2 = int(input(f'{num2} No es un número mayor a {num1}, escriba otro número : '))
    print()
print(f'Los números que ha escrito son: {num1} y {num2}')
