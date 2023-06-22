#calculadora 1
#inicializo la lista
def calculadora1():
    lista_simbolos = ["+", "-", "/", "*",""]

    var1 = input("Ingrese un numero\n")
    #escalonadamente, se revisa que cada variable ingresada sea correcta
    try:
        var1=float(var1)
    except:
        print("error")
    else:
        simbolo=input("Ingrese la operacion a realizar\n")
        if simbolo not in lista_simbolos or simbolo == "":
            print ("error")
        else:
            var2=input("Ingrese un numero\n")
            if simbolo == "/" and var2=="0":
                print("No es posible dividir entre 0\nerror")
            else:
                try:
                    var2=float(var2)
                except:
                    print("error")
                else:
                    #se realizan las cuentas
                    if simbolo == "+" :
                        var1=float(var1)
                        var2=float(var2)
                        resultado = var1 + var2
                    if simbolo == "-" :
                        var1=float(var1)
                        var2=float(var2)
                        resultado = var1 - var2
                    if simbolo == "/" :
                        var1=float(var1)
                        var2=float(var2)
                        resultado = var1 / var2
                    if simbolo == "*" :
                        var1=float(var1)
                        var2=float(var2)
                        resultado = var1 * var2
                    simbolo2 = input("Ingrese ¨=¨ para saber el resultado u otro simbolo para continuar operando\n")
                    if simbolo2 != "=" :
                        while simbolo2 != "=" and simbolo2!="error":
                            #se entra en un loop para segur ingresando numeros hasta que se ingrese un "=" o se encuentre algun error
                            if simbolo2 not in lista_simbolos or simbolo2 == "":
                                print ("error")
                                simbolo2 = "error"
                            else:
                                var3=input("Ingrese otro numero\n")
                                if simbolo2 == "/" and var3=="0":
                                    print("No es posible dividir entre 0\nerror")
                                    simbolo2="error"
                                else:
                                    try:
                                        var3=float(var3)
                                    except:
                                        print("error")
                                        simbolo2 = "error"
                                    #se hacen las cuentas
                                    if simbolo2 == "+" :
                                        var3=float(var3)
                                        resultado = resultado + var3
                                    if simbolo2 == "-" :
                                        var3=float(var3)
                                        resultado = resultado - var3
                                    if simbolo2 == "/" :
                                        var3=float(var3)
                                        resultado = resultado / var3
                                    if simbolo2 == "*" :
                                        var3=float(var3)
                                        resultado = resultado * var3
                            if simbolo2!="error":
                                simbolo2=input("Ingrese ¨=¨ para saber el resultado u otro simbolo para continuar operando\n")
                    #si no hubo ningun error se imprime el resultado
                    if simbolo2!="error":
                        print(resultado)