import sys

if len(sys.argv) != 3:
    print("Debe agregar dos argumentos numéricos al comando")
else:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if 1 <= filas <= 9 and 1 <= columnas <= 9:
        print("----" * columnas + "-")
        for i in range(filas):
            for j in range(columnas):
                print("| * ", end='')
            print("|") 
            print("----" * columnas + "-")
    else:
        print("Los argumentos deben ser números del 1 al 9.")
