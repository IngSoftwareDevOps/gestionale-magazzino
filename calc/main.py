#!/usr/bin/env python

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: divisione per zero"


def main():
    print("Benvenuto nella calcolatrice!")
    print("Operazioni disponibili:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    while True:
        choice = input("Seleziona un'operazione (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("Errore: devi inserire un numero valido.")
                continue

            if choice == '1':
                print(f"Risultato: {add(num1, num2)}")
            elif choice == '2':
                print(f"Risultato: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Risultato: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Risultato: {divide(num1, num2)}")
        else:
            print("Scelta non valida. Riprova.")

        continua = input("Vuoi continuare? (s/n): ")
        if continua.lower() != 's':
            break


if __name__ == "__main__":
    main()
