Nombre 1: Lucas Enriquez Rivera
Rol 1: 202373521-3
Paralelos 1: 200
--------------------------
Nombre 2: Nicolás Chehade Casivar
Rol 2: 202373508-6
Paralelos 2: 200

--------------------------
Especificaci´on de los algoritmos y desarrollo realizado:
El programa se separa en 5 fuciones, 3 de conversión de base y  2 que son el funcionamiento per se de la tarea.

- Para pasar de decimal a binario, se usa la función "binario(decimal)", que está pensada para recibir un 
numero decimal como parámetro. El algoritmo se basa en dividir el numero por 2 e ir guardando el resto
de la división entera, que resultará en el numero en base binaria (pero invertido, luego se da vuelta).
Este proceso se repite mientras el numero siga siendo mayor que 0.

- Para pasar de decimal a octal, se usa la función "octal(decimal)" cuyo funcionamiento es idéntico a la 
función "binario(decimal)", únicamente con la excepción de que la división entera es en 8 y no en 2. El resto del 
proceso es el mismo.

- Para pasar de decimal a hexadecimal se usa la función "hexa(decimal)", cuyo funcionamiento es similar
a las dos funciones anteriores. Las únicas diferencias es que la división es por 16 y no 8 o 2 como antes,
y el resto se cambia por la letra correspondiente, en caso de ser necesario como se muestra a continuación:
	- Si el resto es 15 se reemplaza con una F
	- Si el resto es 14 se reemplaza con una E
	- Si el resto es 13 se reemplaza con una D
	- Si el resto es 12 se reemplaza con una C
	- Si el resto es 11 se reemplaza con una B
	- Si el resto es 10 se reemplaza con una A
Los restos que vayan entre 0 y 9 quedan intactos.

- La función "lanz_dados(cantidad, tipo)" recibe como parametros dos enteros, que representan la cantiadad
de dados lanzados y el tipo de dado (n° de caras) respectivamente. La función se encarga de hacer lanzamientos
aleatorios y reotrnar la suma de estos, todo basado en los parametros recibidos. 

- La función "preguntar_y_separar()" es la encargada de unir todas las piezas anteriores. Inicialmente
le pide al usuario que ingrese detalles sobre el lanzamiento (cantidad y tipo en el formato cdt), y con lo que 
llama a la función lanz_dados para obtener la suma del lanzamiento. Posteriormente, según el tipo de dado 
especficiado llama a la función correspondiente para hacer el cambio de base y mostrarlo luego por pantalla.
Por último, le pide al usuario que ingrese la conversión a decimal del numero mostrado, quien recibe un mensaje de
aceptación o error según su respuesta. 
--------------------------
Supuestos utilizados:
1. El usuario ingresa un solo lanzamiento por ejecución del programa
2. El formato del lanzamiento es CdT, donde C es cantidad y T es el tipo de dato.
	Por ejemplo: 2d6 significa que se lanzan dos dados de 6 caras, por lo que el resultado está
	en el rando entre 2 y 12. 
