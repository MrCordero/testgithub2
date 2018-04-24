#Permita ingresar una cierta cantidad de notas (n). Al momento de ingresar todas las
#notas mostrar el promedio de rojos y el promedio de azules.


acu_azules=0
acu_rojos=0

cont_vueltas=0

limite=int(input(" cuantas notas desea ingresar"))

while(True):

    nota=float(input("ingrese notas "))


    if(nota < 4):
        acu_rojos+=1
    elif(nota >=4):
        acu_azules+=1

    prom_rojos = acu_rojos / limite
    prom_azules = acu_azules / limite

    cont_vueltas += 1



    if(cont_vueltas == limite):
        break



print("el promedio de rojos es de :",prom_rojos,"%")
print("el promedio de azules es de :",prom_azules,"%")










