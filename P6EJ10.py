#Escribe un programa que te pida los nombres y notas dealumnos.
#Si escribes una nota fuera del intervalo de 0 a 10,el programa entenderá que no quieres
# introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá
#que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene
# esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc],
#[nom3, nota1, nota2, etc], etc]
list1 = []
list2 = []
nombre = input("Dime el nombre del alumno: ")
while nombre != "":
    list2.append(nombre)
    notas = float(input("Escribe la nota: "))
    while 10 >= float(notas) >= 0:
        list2.append(notas)
        notas = float(input("Escriba otra nota: "))
    list1.append(list2)
    list2 = []
    nombre = input("Dime otro nombre: ")
print("Las notas de los alumnos son: ")
for i in range(len(list1)):
    print(list1[i][0],":",end=" ")
    #print(list1[i][1],end=" ")
    for j in range(1,len(list1[i])):
        print(" - ",list1[i][j],end=" ")
    print("")