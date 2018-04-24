#Permita ingresar un grupo de notas (el usuario escoge). Al final sacar el promedio
#general del curso.

cont_notas = 0

acum_notas = 0

cont_vueltas = 0

limite = int(input("¿Cuantas notas quiere ingresar? : "))

while(True):
    notas = float(input("Indique la nota:"))
    acum_notas += notas/limite
    cont_vueltas +=1

    if(cont_vueltas == limite ):
        break


print("El promedio final del curso es ", acum_notas)
