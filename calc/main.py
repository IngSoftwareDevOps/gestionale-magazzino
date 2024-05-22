def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Errore: Divisione per zero!"
    return x / y


def main():
    print("Seleziona l'operazione:")
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    while True:
        choice = input("Inserisci la scelta (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("Per favore inserisci dei numeri validi.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Errore: Divisione per zero!":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Scelta non valida. Per favore scegli di nuovo.")

        next_calculation = input("Vuoi eseguire un altro calcolo? (si/no): ")
        if next_calculation.lower() != 'si':
            break


if __name__ == "__main__":
    main()

