class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongOption(Error):
    """Za duzy rabat"""
    pass


class Produkt:
    # Zmienne
    nazwa = ""
    cena = 0.0
    kategoria = ""
    data_waznosci = ""

    def __init__(self, nazwa=None, cena=None, kategoria=None, data_waznosci=None):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria
        self.data_waznosci = data_waznosci

    def __str__(self):
        return f'Nazwa: {self.nazwa}  |  Cena: {self.cena}  |  Kategoria: {self.kategoria}  |  Data ważności: {self.data_waznosci}'

    def zmienCene(self, cena):
        print(f'Stara cena: {self.cena}')
        self.cena = cena
        print(f'Nowa cena: {self.cena}')

    def dodajRabat(self, rabat):
        try:
            if rabat > 0.99:
                raise WrongOption
            else:
                rabacik = 1 - rabat
                self.cena = self.cena * rabacik;
        except WrongOption:
            print("Podana wartość rabatu jest zbyt duża")
