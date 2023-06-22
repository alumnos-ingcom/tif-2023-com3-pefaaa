#Menu principal
import Calculadora1 as c1
import Calculadora2 as c2
import Calculadora3 as c3
opcion = input("Ingrese 1 para calculadora clasica, 2 para calcuadora clasica de fracciones, 3 para calculadora transformadora y 4 para finalizar\n")
#no pasa hasta que se ingrese alguna calculadora(1,2,3) o "4" para salir
while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
    opcion=input("Ingrese opcion 1, 2, 3 o 4 para comenzar\n")
#se entra en el bucle de elejir una calculadora hasta que ingrese el numero 4
while opcion != "4":
    if opcion == "1":
        c1.calculadora1()
    if opcion == "2":
        c2.calculadora2()
    if opcion == "3":
        c3.calculadora3()
    opcion = input("Ingrese 1 para calculadora clasica, 2 para calcuadora clasica de fracciones, 3 para calculadora transformadora y 4 para finalizar\n")