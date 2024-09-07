Nombre 1: Lucas Enriquez Rivera
Rol 1: 202373521-3
Paralelos 1: 200
--------------------------
Nombre 2: Nicolás Chehade Casivar
Rol 2: 202373508-6
Paralelos 2: 200

--------------------------
Especificaci´on de los algoritmos y desarrollo realizado:

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

- Para pasar de cualquier base a decimal, hacemos uso de un algortimo en el cual se identifican los diferentes 'caracteres' que cada base posee (Ej: binario 2, octal 8, hexadecimal 16...) y, a partir de estos, sumamos a una variable entera el recorrido que hacemos de izquierda a derecha de la cadena de entrada con el siguiente procedimiento tomando de ejemplo la cadena de entrada en base numérica binaria "110":
	- Identificamos el caracter actual y vemos su 'valor' decimal en una tabla que posee TODAS las unidades de las bases a utilizar en un array: [0, 1, 2, ..., 9, A, B, C, D, E, F].
	"110"
	 ^- Se encuentra en el índice 1, por lo que su valor es 1.
	- Considerando el máximo valor por base, aplicamos una fórmula exponencial que toma de base al respectivo rango de valores posibles por esta.
	FORMULA:
		VALOR_DIGITO * RANGO_VALORES^(POS. DÍGITO - 1)
		- Aplicando la fórmula al ejemplo "110" con el 1er caracter de izq. a der.:
		1 * 2^2 <-- El primer 1 está en el tercer digito de derecha a izquierda.
		^   ^------ Ya sabemos que la base binaria solo posee 2 valores posibles: 0 y 1
		|__________ Dijimos que el 1 en sí posee el valor 1 en la base decimal.

		1 * 2^2 = 4
	- Vamos sumando los valores que nos entrega la formula digito por digito.
		"110" entrega:
		 ^^^-- 0 * 2^0 = 0
		 ||___ 1 * 2^1 = 2
		 |____ 1 * 2^2 = 4
		
		2 + 4 = 6
	- ... Así lo podemos hacer para el resto de las bases.
		