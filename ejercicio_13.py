#Permita ingresar notas. El programa debe estar pidiendo notas hasta que ingrese la
#nota -800. Decir cuántos sietes y cuántos unos hay


cont_notas = 0

cont_unos = 0

cont_sietes = 0

cont_vueltas = 0


while(True):
    notas = float(input("Ingrese las notas"))

    cont_notas = cont_notas + 1

    if(notas == 7 ):
        cont_sietes = cont_sietes + 1
    elif(notas == 1):
        cont_unos = cont_unos + 1


        cont_vueltas = cont_vueltas + 1

    if(notas == -800):
        break
















print("Cantidad de unos es de:" , cont_unos)
print("Cantidad de sietes es de:" , cont_sietes)
print("Total de numeros ingresados : " , cont_vueltas)