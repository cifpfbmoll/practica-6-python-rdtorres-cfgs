#Escribe un programa que te pida palabras y las guarde en una lista.
#Para terminar de introducir palabras, simplemente pulsa Enter.
#El programa termina escribiendo la lista de palabras.
palabra = str((input("Escribe una palabra: ")))
lista=[]
while palabra!='':
    lista+=[palabra]
    print("Escriba otra palabra: ")
    palabra=str(input())
print(lista)