#Desarrolla de nuevo el ejercicio de la práctica
#anterior de los números primos, con while.
#Reflexiona y escribe en el propio programa en forma de comentario,
#qué opción es mejor y por qué.
num = int(input("Escriba un número mayor que 0: "))

if num <= 0:
    print("El número debe ser mayor a cero.")
else:
    divisor = 0
    i = 2
#Usando el bucle while vamos a tardar muchísimo menor por el hecho de que el
# mismo va ha buscar las soluciones hasta que vea que ya ha cumplido la
# condición si lo hace, para el bucle y muestra el resultado.
    while i < num:
        if num % i == 0:
            divisor += 1
        i += 1
    if divisor == 0 and num > 1:
        print("El número es primo.")
    else:
        print("El número no es primo.")



