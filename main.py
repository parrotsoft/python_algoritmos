import os


def main():
    repite = True;
    while(repite):
        opcion = menu()
        clearConsole()
        if opcion == 1:
            num_primos()
        elif opcion == 2:
            num_primos()
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
    print("Numeros Primos")

def num_pares():
    print("Numero Pares")

def serie_fibonacci():
    print("Serie Fibonacci")

def clearConsole():
    clear = lambda: os.system('cls')
    clear()

if __name__=="__main__":
    main()
