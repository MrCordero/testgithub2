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
    acu_num += num/limite

    #Division

    cont_vueltas = cont_vueltas + 1
    if(cont_vueltas == limite):
        break








print("el promedio total de los numeros es :", acu_num)
