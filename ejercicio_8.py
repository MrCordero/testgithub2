#Contador de numeros
cont_num = 0

#Contador de vueltas
cont_vueltas = 0

#Acumulador de numeros
acu_num = 0





while(True):
    num = int(input("Ingrese numero : "))

    #Suma
    acu_num += num
    cont_num=cont_num + 1

    cont_vueltas = cont_vueltas + 1
    prom=acu_num/cont_vueltas
    if(num == -100):
        break








print("La suma de los numeros es :", acu_num)
print("Cantidad de numeros ingresados es ", cont_num)