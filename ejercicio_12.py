#Permita ingresar notas. El programa debe estar pidiendo notas hasta que ingrese la
#nota -1. Decir cuántas notas azules hay, cuantas rojas.

cont_notas = 0

cont_rojos = 0

cont_azules = 0

cont_vueltas = 0


while(True):
    notas = float(input("Ingrese las notas"))

    cont_notas = cont_notas + 1

    if(notas >= 4 ):
        cont_azules = cont_azules + 1
    else:
        cont_rojos = cont_rojos + 1


        cont_vueltas = cont_vueltas + 1

        if(notas == -1):
            break



















print("Cantidad de rojos es de:" , cont_rojos)
print("Cantidad de azules es de:" , cont_azules)
print("Total de numeros ingresados : " , cont_vueltas)