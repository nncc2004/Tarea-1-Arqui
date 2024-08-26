import random as r

'''
    Funciones:
    1. De decimal a binario (lista: binario)
    2. De decimal a Hexadecimal
    3. De decimal a octal (lista: octal)
    4. Generación del "lanzamiento de dados" aleatorio (lista: lanz_dados)
'''

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
    
def hexa(decimal):
    pass

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

valor = lanz_dados(2,100) #cantidad, tipo | (1d6) = 1 dado de 6 caras
bin = binario(valor)
oct = octal(valor)

print("el dado arrojó ", str(valor), " en decimal, que es lo mismo que ", bin, " en decimal y ", oct, " en octal")