#Permita ingresa n edades. El programa debe decir cuántas personas son mayor de
#edad y cuantas son menores de edad.

c_may = 0

c_men = 0

acu_edades = 0

vuelta = 0

limite = int(input("Cuantas edades quiere ingresar?"))

while(True):
    edad = int(input("Edad: "))

    if(edad >= 18):
        c_may = c_may + 1
        print("Es mayor de edad!")
    else:
        cont_men += 1
        print("Menor de edad!")


    acu_edades = acu_edades + edad

    vuelta = vuelta + 1

    if(vuelta == limite):
        break

print("La suma de edades es: ",acu_edades)
print("Mayores de edad: ", c_may)
print("Menores de edad: ", c_men)