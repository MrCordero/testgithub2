#Permita ingresar un grupo de notas (el usuario escoge). Al final mostrar la nota más
#alta y la nota más baja



cont_vueltas = 0

limite = int(input("Ingrese el numero de notas :"))

while(True):

    notas = float(input("Indique una nota :"))
    cont_vueltas = cont_vueltas + 1

    if(cont_vueltas == 1):
        nma = notas
        nmb = notas
    else:
        if (notas > nma):
            nma = notas

        if (notas < nmb):
            nmb = notas

    if(cont_vueltas == limite):
       break

print("Nota mas alta :",nma)
print("Nota mas baja :",nmb)