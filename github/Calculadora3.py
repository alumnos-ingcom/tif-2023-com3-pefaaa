#calculadora 3
def calculadora3():
    #inicializo listas y variables
    resto_juntado = []
    contador = 0
    no_permitido = ["+","-","*","/","."]
    resultado = 16
    #hago que si o si ingrese la opcion 1, 2 o 3
    opcion = str(input("Ingrese 1 para pasar a binario, 2 para octal o 3 para hexadecimal\n"))
    while opcion != "1" and opcion != "2" and opcion !="3":
        opcion = input("Ingreso incorrecto, ingrese nuevamente")
    #ingresa el numero a transformar y verifica que este bien
    variable = input("Ingrese el numero a transformar\n")
    for i in variable:
        if i in no_permitido:
            opcion="error"
            print ("error")
    #calculadora para pasar a numero binario
    if opcion == "1" :
        variable = int(variable)
        while resultado > 1:
            resultado = variable // 2
            resto = variable % 2
            resto_juntado.append(resto)
            contador = contador + 1
            variable = resultado
    #calculadora para pasar a numero octal
    if opcion == "2" :
        variable = int(variable)
        while resultado > 7:
            resultado = variable // 8
            resto = variable % 8
            resto_juntado.append(resto)
            contador = contador + 1
            variable = resultado
    #calculadora para pasar a numero hexadecimal
    if opcion == "3":
        variable = int(variable)
        while resultado > 15:
            resultado = variable // 16
            resto = variable % 16
            if resto == 10:
                resto = "A"
            if resto == 11:
                resto = "B"
            if resto == 12:
                resto = "C"
            if resto == 13:
                resto = "D"
            if resto == 14:
                resto = "E"
            if resto == 15:
                resto = "F"
            resto_juntado.append(resto)
            contador = contador + 1
            variable = resultado

    #si se pasa a numero hexadecimal el primer numero del numero transformado
    #queda como 10,11,12,13,14 o 15 y tiene que ser A,B,C,D,E o F
    if resultado == 10:
        resultado = "A"
    if resultado == 11:
        resultado = "B"
    if resultado == 12:
        resultado = "C"
    if resultado == 13:
        resultado = "D"
    if resultado == 14:
        resultado = "E"
    if resultado == 15:
        resultado = "F"
    #exepto que halla algun error, se da vuelta la lista y se la pasa
    # a string para ingresar el reultado final de forma correcta
    if opcion != "error":
        resultado_final= str(resultado)
        while contador > 0:
            i=resto_juntado.pop(contador-1)
            i=str(i)
            resultado_final=resultado_final+i
            contador= contador -1
        print(resultado_final)