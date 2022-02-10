"""
En este archivo se pueden ver las principales variables primitivas que
existen en python
"""

"""
Numeros enteros (int)

Los numeros enteros son números positivos o negativos no fraccionado (Sin decimales)

Este tipo de variable admite hasta 8 bits.
Numero minimo y maximo de este tipo de variable: -32768 a 32767

Ejemplos:
"""

A = 1
B = 10
C = -5

print("Numeros enteros (int):", A, B, C,"\n")

"""
Numeros de punto flotante (float)

Los numeros de punto flotante son numeros positivos o negativos fraccionados 
(Con decimales(incluyento .0))

Este tipo de variable admite hasta 32 Bits.
Numero minimo y maximo de este tipo de variable: 3.4E-38 a 3.4E38.

Ejemplos:
"""

A = 1.5
B = 3.14159365358 # pi
C = -7.48

print("Numeros de punto flotante (float):", A,B,C,"\n")

"""
Caracteres (Char)

Las variables de tipo char admite solo 1 caracter alfanumerico

Este tipo de variable admite solo 1 bit

Advertencia: para que python interprete que es una variable de tipo char tiene
que se asignada usando comillas ("")

Ejemplos:
"""

A = "E"
B = "G"
C = "z"

print("Variables Char:", A,B,C, "\n")

"""
Variables String

Las variables de tipo cadena de caracteres o String admiten una sucesion de
caracteres alfanumericos.

Ejemplos:
"""

A = "Esto es un String"
print("Variables String:", A,"\n")

"""
Variables Booleanas (bool)

La variable booleana es una variable logica, esto quiere decir que solo admite
valores de True(Verdadero) o False(Falso). 

Ejemplos:
"""

A = True
B = False

print("Variables Booleanas:", A,B)