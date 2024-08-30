import random as r

#Dado un numero en decimal, retorna un numero en binario (tipo string!!)
def binario(decimal):
    numero = []
    binario = ''
    while decimal > 0:
        sobra = decimal % 2
        decimal //= 2
        numero.append(str(sobra))
    i = 1
    while i<=len(numero):
        binario += numero[-i]
        i+= 1
        
    return binario
    
#Dado un numero en decimal, retorna un numero en hexadecimal (tipo string!!)
def hexa(decimal):
    numero = []
    hexa = ''
    while decimal > 0:
        sobra = decimal % 16
        decimal //= 16
        numero.append(str(sobra))
    i = 1

    while i<=len(numero):
        if numero[-i] == "15":
            numero[-i] = 'F'
        elif numero[-i] == "14":
            numero[-i] = 'E'
        elif numero[-i] == "13":
            numero[-i] = 'D'
        elif numero[-i] == "12":
            numero[-i] = 'C'
        elif numero[-i] == "11":
            numero[-i] = 'B'
        elif numero[-i] == "10":
            numero[-i] = 'A'
        hexa += numero[-i]
        i+= 1
        
    return hexa

#Dado un numero en decimal, retorna un numero en octal (tipo string!!)
def octal(decimal):
    numero = []
    octal = ''
    while decimal > 0:
        sobra = decimal % 8
        decimal //= 8
        numero.append(str(sobra))
    i = 1
    while i<=len(numero):
        octal += numero[-i]
        i+= 1
        
    return octal

#Dado un tipo de dado y la cantidad de lanzamientos, retorna la suma del lanzamiento
def lanz_dados(cantidad, tipo):
    i = 0
    suma = 0
    while(i<cantidad):
        numero = r.randint(1, tipo)
        suma += numero
        i+=1
    return suma

def preguntar_y_separar():
    dado = input("Dados Obtenidos: ")
    dado = dado.split("d")
    cantidad = dado[0]
    tipo = dado[1]
    valor = lanz_dados(int(cantidad), int(tipo)) 
    if tipo == "6":
        cambio  = binario(valor)
    elif tipo == "20":
        cambio =  octal(valor)
    elif tipo == "100":
        cambio = hexa(valor)
    else:
        print("Tipo de dado no compatible")
        return
    print("Numero obtenido: ", cambio)


    intento = int(input("Ingrese su respuesta: "))
    if intento == valor:
        print("Correcto")
    else:
        print("Incorrecto")

preguntar_y_separar()