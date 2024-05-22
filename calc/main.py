n1 = float(input("Inserisci il primo valore: "))
n2 = float(input("Inserisci il secondo valore: "))
scelta = int(input("Che operazione vuoi svolgere? \n1: Somma \n2: Sottrazione \n3: Moltiplicazione \n4: Divisione\n"))


def calcolo(n1, n2, scelta):
    if scelta == 1:
        print(n1, "+", n2, "=", n1 + n2)
    elif scelta == 2:
        print(n1, "-", n2, "=", n1 - n2)
    elif scelta == 3:
        print(n1, "*", n2, "=", n1 * n2)
    elif scelta == 4:
        print(n1, "/", n2, "=", n1 / n2)
    else:
        print("Scelta non valida.")


calcolo(n1, n2, scelta)
