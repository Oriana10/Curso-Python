"""
import sys

numero_cadena = str(int(sys.argv[1]))

print(numero_cadena[2:])


if len(sys.argv) != 1:
    print("Debe agregar un argumentos numéricos al comando")
else:
    numero_cadena = int(sys.argv[1])
    for i in len(string):
        print( numero_cadena[i:] )

  3647
  0007
  0040
  0600
  3000
"""


import sys

if len(sys.argv) != 2:
    print("Uso: python descomposicion.py <numero>")
else:
    numero = int(sys.argv[1])

    numero_str = str(numero)
    longitud = len(numero_str)

    # Iterar desde la unidad hasta el número, multiplicando por potencias de 10
    for i in range(longitud):
        # Calcular la potencia de 10 correspondiente
        potencia_10 = 10 ** (longitud - i - 1)
        
        # Calcular la parte correspondiente del número y formatearla
        parte_numero = numero // potencia_10
        parte_formateada = "{:04}".format(parte_numero * potencia_10)

        # Imprimir la parte formateada
        print(parte_formateada)

        # Actualizar el número restando la parte que ya se procesó
        numero %= potencia_10
