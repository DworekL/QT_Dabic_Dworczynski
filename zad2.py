import Produkt


def wyswietlProdukty():
    print("------------LISTA WSZYSTKICH PRODUKTÓW------------")
    for character in range(len(listaProduktow)):
        print(f'{character + 1}. {listaProduktow[character]}')


def dodajProdukt():
    try:
        print("Dodawanie produktu...")
        nazwa = input("Podaj nazwę: ")
        cena = float(input("Podaj cenę: "))
        kategoria = input("Podaj kategorię: ")
        data = input("Podaj datę waznosci: ")
    except ValueError:
        print("Podano błędne dane")

    prod = Produkt.Produkt(nazwa=nazwa, cena=cena, kategoria=kategoria, data_waznosci=data)
    listaProduktow.append(prod)

def dodajRabat():
    wyswietlProdukty()

    try:
        numer_produktu = int(input("Podaj numer produktu dla którego chcesz dodać rabat: "))
    except ValueError:
        print("Należy podać liczbę całkowitą")

    try:
        rabat = float(input("Podaj rabat w postaci ułamka (np. 30% = 0.3): "))
    except ValueError:
        print("Należy podać ułamek")

    if numer_produktu > len(listaProduktow) or numer_produktu < 1:
        print("Podano błędny numer produktu")
    else:
        listaProduktow[numer_produktu - 1].dodajRabat(rabat)

def zmienCene():
    wyswietlProdukty()

    try:
        numer_produktu = int(input("Podaj numer produktu dla którego chcesz zmienić cenę: "))
    except ValueError:
        print("Należy podać liczbę całkowitą")

    try:
        cena = float(input("Podaj nową cenę: "))
    except ValueError:
        print("Błędna cena")

    if numer_produktu > len(listaProduktow) or numer_produktu < 1:
        print("Podano błędny numer produktu")
    else:
        listaProduktow[numer_produktu - 1].zmienCene(cena)



if __name__ == '__main__':

    prod1 = Produkt.Produkt(nazwa='Czekolada', cena=5.00, kategoria='Słodycze', data_waznosci='25.05.2021')
    prod2 = Produkt.Produkt(nazwa='Ciastka', cena=7.00, kategoria='Słodycze', data_waznosci='27.09.2021')
    prod3 = Produkt.Produkt(nazwa='Chipsy', cena=3.99, kategoria='Przekąski', data_waznosci='06.05.2022')
    prod4 = Produkt.Produkt(nazwa='Coca-Cola', cena=6.50, kategoria='Napoje', data_waznosci='24.12.2022')
    prod5 = Produkt.Produkt(nazwa='Szampon', cena=11.99, kategoria='Kosmetyki', data_waznosci='25.05.2023')

    listaProduktow = []

    listaProduktow.append(prod1)
    listaProduktow.append(prod2)
    listaProduktow.append(prod3)
    listaProduktow.append(prod4)
    listaProduktow.append(prod5)

    boolek = True
    while boolek:

        print("--------------------------------------------------")
        print("1.Dodaj produkt")
        print("2.Dodaj rabat")
        print("3.Wyświetl produkty")
        print("4.Zmien cene")
        print("5.Wyjście")

        odp = int(input("Wybierz opcje: "))

        if odp == 1:
            dodajProdukt()
        elif odp == 2:
            dodajRabat()
        elif odp == 3:
            wyswietlProdukty()
        elif odp == 4:
            zmienCene()
        elif odp == 5:
            boolek = False
            print("Opuszczanie skryptu...")
        else:
            print("Podano błędny numer")

