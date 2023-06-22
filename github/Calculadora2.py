#calculadora 2
#inicializo la lista
def calculadora2():
    lista_simbolos = ["+", "-", "/", "*",""]
    error = "f"
    #escalonadamente, se revisa que cada variable ingresada sea correcta
    var1n = input("Ingrese el numerador de su numero\n")
    var1d = input("Ingrese el denominador de su numero\n")
    try:
        var1n=int(var1n)
        var1d=int(var1d)
    except:
        print("error")
        error = "t"
    if var1d==0:
        print ("error")
        error = "t"
    if error != "t":
        simbolo=input("Ingrese la operacion a realizar\n")
        if simbolo not in lista_simbolos or simbolo == "":
            print ("error")
        else:
            var2n=input("Ingrese el numerador de su numero\n")
            var2d=input("Ingrese el denominador de su numero\n")
            try:
                var2n=int(var2n)
                var2d=int(var2d)
            except:
                print("error")
                error = "t"
            if simbolo == "/" and var2n==0:
                print("No se puede dividir por 0\nerror")
                error = "t"
            if var2d==0:
                print ("error")
                error = "t"
            if error == "f":
                #se realizan las cuentas
                if simbolo == "+" :
                    var1n=int(var1n)
                    var1d=int(var1d)
                    var2n=int(var2n)
                    var2d=int(var2d)
                    resultado_n = (var1n * var2d) + (var2n * var1d)
                    resultado_d = var1d * var2d
                if simbolo == "-" :
                    var1n=int(var1n)
                    var1d=int(var1d)
                    var2n=int(var2n)
                    var2d=int(var2d)
                    resultado_n = (var1n * var2d) - (var2n * var1d)
                    resultado_d = var1d * var2d
                if simbolo == "/" :
                    var1n=int(var1n)
                    var1d=int(var1d)
                    var2n=int(var2n)
                    var2d=int(var2d)
                    resultado_n = var1n * var2d
                    resultado_d = var1d * var2n
                if simbolo == "*" :
                    var1n=int(var1n)
                    var1d=int(var1d)
                    var2n=int(var2n)
                    var2d=int(var2d)
                    resultado_n = var1n * var2n
                    resultado_d = var1d * var2d
                simbolo2 = input("Ingrese ¨=¨ para saber el resultado u otro simbolo para continuar operando\n")
                if simbolo2 != "=" :
                    while simbolo2 != "=" and error == "f":
                        #se entra en un loop para segur ingresando numeros hasta que se ingrese un "=" o se encuentre algun error
                        if simbolo2 not in lista_simbolos or simbolo2 == "":
                            print ("error")
                            error = "t"
                        else:
                            var3n = input("Ingrese el numerador de su numero\n")
                            var3d = input("Ingrese el denominador de su numero\n")
                            try:
                                var3n=int(var3n)
                                var3d=int(var3d)
                            except:
                                print("error")
                                error = "t"
                            if simbolo2 == "/" and var3n==0:
                                print("No se puede dividir por 0\nerror")
                                error = "t"
                            if var3d==0:
                                print ("error")
                                error = "t"
                                #se hacen las cuentas
                                if simbolo2 == "+" :
                                    var3n=int(var3n)
                                    var3d=int(var3d)
                                    resultado_n = (resultado_n * var3d) + (resultado_d * var3n)
                                    resultado_d = resultado_d * var3d
                                if simbolo2 == "-" :
                                    var3n=int(var3n)
                                    var3d=int(var3d)
                                    resultado_n = (resultado_n * var3d) - (resultado_d * var3n)
                                    resultado_d = resultado_d * var3d
                                if simbolo2 == "/" :
                                    var3n=int(var3n)
                                    var3d=int(var3d)
                                    resultado_n = resultado_n * var3d
                                    resultado_d = resultado_d * var3n
                                if simbolo2 == "*" :
                                    var3n=int(var3n)
                                    var3d=int(var3d)
                                    resultado_n = resultado_n * var3n
                                    resultado_d = resultado_d * var3d
                        if error=="f":
                            simbolo2=input("Ingrese ¨=¨ para saber el resultado u otro simbolo para continuar operando\n")
                    #si no hubo errores se imprime el resutado 
                if error == "f":
                    print("El numerador es: ", resultado_n)
                    print("El denominador es: ", resultado_d)
                    print(resultado_n, "/", resultado_d)