import os


def main():
    repite = True;
    while(repite):
        opcion = menu()
        clearConsole()
        if opcion == 1:
            num_primos()
        elif opcion == 2:
            num_pares()
        elif opcion == 3:
            serie_fibonacci()
        elif opcion == 4:
            repite = False
        else:
            print("Selecciono una opcion errada")

def menu():
    print("""--- MENU DE OPERACIONES ---
    1. Numeros primos
    2. Numeros pares
    3. Serie Fibonacci
    4. Salir""")
    return input("--- Seleccione una opcion ---") 

def num_primos():
    print("--- NUMEROS PRIMOS ---")
    ene = int(input("Digite el valor de N : "))
    numeros = []
    for i in range (1, ene + 1):
        if isPrimo(i) :
            numeros.append(i)
    print(numeros)
    

def num_pares():
    print("--- NUMEROS PARES ---")
    ene = int(input("Digite el valor de N : "))
    numeros = []
    for i in range (1, ene + 1):
        if isPar(i) :
            numeros.append(i)
    print(numeros)

def serie_fibonacci():
    print("Serie Fibonacci")

def clearConsole():
    clear = lambda: os.system('cls')
    clear()

def isPrimo(num):
    if(num == 1):
        return True
    elif ((2** (num - 1)) % num) == 1 or num == 2:
        return True
    else:
        return False


def isPar(num):
    return num % 2 == 0


if __name__=="__main__":
    main()
