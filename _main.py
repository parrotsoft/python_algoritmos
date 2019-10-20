import os
import re
import numpy as np

orden_columnas = 0

def main():
    repite = True;
    while(repite):
        opcion = menu()
        clearConsole()
        if opcion == 1:
            mensaje_bienvenida()
        if opcion == 2:
            mensaje_orden()
        elif opcion == 4:
            repite = False;


def menu():
    print("""--- MAQUINA ENIGMA ---
    1. Mensaje de bienvenida
    2. Orden
    3. Despedida
    4. Salir""")
    return input("--- Seleccione una opcion ---") 
    
def clearConsole():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")  

def num_columnas(cadena):
    cadena = re.sub("\D", "", cadena)
    return (len(cadena)-3)

def num_filas(cadena, columnas):
    return int(round(float(len(cadena))/float(columnas)))

def matriz_to_cadena(matriz):
    cadena = "";
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cadena += matriz[i][j]

    return cadena


def mensaje_bienvenida():
    print("--- MENSAJE DE BIENVENIDA ---")
    cadena = "HI12ET04ILP5LE51HRC3"
    global orden_columnas

    n_column = num_columnas(cadena)
    n_filas = num_filas(cadena, n_column)
    matriz = np.chararray((n_filas, n_column))

    pos = 0
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            if pos < len(cadena):
                matriz[j][i] = cadena[pos]
                pos += 1

    saludo_desencriptado = matriz_to_cadena(matriz)
    orden_columnas = saludo_desencriptado[len(saludo_desencriptado)-n_column:]
    print("El saludo desencriptados : " + saludo_desencriptado)
    print("El orden de las culumnas es : "+orden_columnas)

    

def mensaje_orden():
    print("--- MENSAJE DE ORDEN ---")
    cadena = "BLUAOKABTDTSEBRCDEAERUFEFAEQRENRSGCAEAAENCV"

    n_column = len(orden_columnas)
    n_filas = num_filas(cadena, n_column)
    matriz = np.chararray((n_filas, n_column))
    
    index = 0;
    columna = int(orden_columnas[index]);
    contador_letra = 0

    for x in range(len(cadena)):
        if contador_letra <= 8:
            matriz[contador_letra][columna-1] = cadena[x]
            contador_letra += 1
            if contador_letra == 8:
                contador_letra = 0
        if index < 4:
            index += 1
            columna = int(orden_columnas[index])

    print(matriz)
                
                
    


if __name__=="__main__":
    main()