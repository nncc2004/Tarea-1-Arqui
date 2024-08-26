import random as r
'''
    Funciones:
    1. De decimal a binario
    2. De decimal a Hexadecimal
    3. De decimal a octal
    4. Generación del "lanzamiento de dados" aleatorio
'''


#Dado un tipo de dado y la cantidad de lanzamientos, retorna la suma del lanzamiento
def lanz_dados(cantidad, tipo):
    i = 0
    suma = 0
    while(i<cantidad):
        numero = r.randint(1, tipo)
        suma += numero
        i+=1
    return suma


valor = lanz_dados(2,6) #cantidad, tipo | (1d6) = 1 dado de 6 caras
print(valor)