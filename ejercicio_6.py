#Contador de numeros
cont_num = 0

#Contador de vueltas
cont_vueltas = 0

#Acumulador de numeros
acu_num = 0



limite =int(input("¿Cuantos numeros quiere ingresar?"))

while(True):
    num = int(input("Ingrese numero : "))

    #Suma
    acu_num += num

    cont_vueltas = cont_vueltas + 1
    prom=acu_num/cont_vueltas
    if(cont_vueltas == limite):
        break








print("La suma de los numeros es :", acu_num)
print("Cantidad de numeros ingresados es ", limite)