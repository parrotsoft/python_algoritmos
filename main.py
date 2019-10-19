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
            suma_exp_incremental()
        elif opcion == 5:
            suma_exp_n()            
        elif opcion == 6:
            repite = False
        else:
            print("Selecciono una opcion errada")

def menu():
    print("""--- MENU DE OPERACIONES ---
    1. Numeros primos
    2. Numeros pares
    3. Serie Fibonacci
    4. Suma Exp incremental
    5. Suma Exp N
    6. Salir""")
    licencia()
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
    print("--- SERIE FIBONACCI ---")
    ene = int(input("Digite el valor de N : "))
    numeros = []
    for i in range (1, ene + 1):
        numeros.append(fib(i))
    print(numeros)

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

def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)

def licencia():
    print("Copyright 2019 - Miguel Lopez Ariza")
    print("")

def suma_exp_incremental():
    print("--- SUMA EXP. INCREMENTAL ---")
    ene = int(input("Digite el valor de N : "))
    print(sumaRecursiva(ene, True))

def suma_exp_n():
    print("--- SUMA EXP. N ---")
    ene = int(input("Digite el valor de N : "))
    print(sumaRecursiva(ene, False))    

def sumaRecursiva(num, auto):
    i = 0
    if num > 0:
        if auto:
            i += 1
            return (num**i) + sumaRecursiva(num -1, auto)
        else:
            return (num**num) + sumaRecursiva(num -1, auto)
    else:
        return num

if __name__=="__main__":
    main()
