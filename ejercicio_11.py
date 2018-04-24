#Permita ingresar edades. El programa debe estar pidiendo edades hasta que ingrese la
#edad -100. Decir cuántas personas son de la tercera edad (mayor a 50) y cuantas
#edades se ingresaron

cont_edad = 0

cont_vueltas = 0

cont_mayedad = 0


while(True):

    edad = int(input("Ingrese edades : "))
    if(edad >= 50):
        cont_mayedad = cont_mayedad + 1
        print("Pertenece a la Tercera edad. ")
        cont_vueltas = cont_vueltas + 1

    if(edad == -100):
        break







print("La cantidad de edades ingresadas es de : ", cont_vueltas)
print("La cantidad de personas que pertenecen a la Tercera edad es de :", cont_mayedad)