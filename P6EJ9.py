#Escribe un programa que te pida nombres de personas y sus números de teléfono.
#Para terminar debe pulsar “S” cuando te pida el nombre.
#El programa termina escribiendo nombres y números de teléfono.
#Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura
#[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
list_contactos = []
nombre = str
while nombre != "S":
    nombre = input("Dime el nombre: ")
    if nombre != "S":
        numero = input("Dame un numero: ")
        list_contactos.append([nombre, numero])
print("Los nombres y numeros de la agenda son los siguientes: ")
for i in range(len(list_contactos)):
    print("nombre: ", list_contactos[i][0], " numero: ", list_contactos[i][1])
