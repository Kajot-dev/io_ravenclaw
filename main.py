import time
import random
import csv
from enum import Enum

class Odleglosc(Enum):
    LOKALNA = "lokalna"
    KRAJOWA = "krajowa"
    DALEKOBIEZNA = "dalekobieżna"
    
class TypPaczki(Enum):
    LIST = "list"
    PACZKA = "paczka"
    
class SpecjalnaPaczka(Enum):
    WYJEC = "wyjec"
    LIST_GONCZY = "list gonczy"
    NIE_DOTYCZY = "nie dotyczy"

def wyslij_sowe(adresat, tresc):
    print(f"Wysłanie sowy do {adresat} z treścią: {tresc}")
    time.sleep(1)

    if random.random() <= 0.85:
        print("Sowa dostarczona")
        return True
    else:
        print("Dostarczenie sowy niemożliwe")
        return False
    
def wybierz_sowe_zwroc_koszt(odbior: bool, odleglosc: Odleglosc, typ: TypPaczki, specjalna: SpecjalnaPaczka):
    koszt = {"galeon": 0, "sykl": 0, "knut": 0}
    if odbior:
        koszt["knut"] += 7
    
    if specjalna == SpecjalnaPaczka.WYJEC:
        koszt["knut"] += 4
    elif specjalna == SpecjalnaPaczka.LIST_GONCZY:
        koszt["knut"] += 1

    # [knut, sykl]
    odleglosc_koszt = {
        Odleglosc.LOKALNA: {TypPaczki.LIST: [2, 0], TypPaczki.PACZKA: [7, 0]},
        Odleglosc.KRAJOWA: {TypPaczki.LIST: [12, 0], TypPaczki.PACZKA: [2, 1]},
        Odleglosc.DALEKOBIEZNA: {TypPaczki.LIST: [20, 0], TypPaczki.PACZKA: [1, 2]}
    }

    koszt['knut'] += odleglosc_koszt[odleglosc][typ][0]
    koszt['sykl'] += odleglosc_koszt[odleglosc][typ][1]

    return koszt


def licz_sume(fundusz):
    # Pobranie list monet dla każdego rodzaju
    geleon = fundusz.get('geleon', [0, 0, 0])
    sykl = fundusz.get('sykl', [0, 0, 0])
    knut = fundusz.get('knut', [0, 0, 0])

    # Obliczenie sumy wartości monet w knutach
    suma_knutow = sum(geleon) * 17 * 21 + sum(sykl) * 21 + sum(knut)

    # Konwersja na galeony, sykle i knuty
    ile_galeonow = suma_knutow // (17 * 21)
    suma_knutow %= (17 * 21)
    ile_sykli = suma_knutow // 21
    suma_knutow %= 21

    # Tworzenie słownika wynikowego
    wynik = {
        'galeon': ile_galeonow,
        'sykl': ile_sykli,
        'knut': suma_knutow
    }
    return wynik


def waluta_dict_na_str(fundusz: dict[str, int]) -> str:
    # nie zmieniamy kolejności walut w słowniku
    buffer = []
    for waluta, ilosc in fundusz.items():

        if ilosc == 0:
            continue

        last_digit = ilosc

        while last_digit >= 10:
            last_digit = last_digit % 10

        if last_digit > 1 and last_digit < 5:
            match waluta[-1]:
                case "l":
                    waluta += "e"
                case _:
                    waluta += "y"

        elif last_digit >= 5:
            match waluta[-1]:
                case "l":
                    waluta += "i"
                case _:
                    waluta += "ów"

        buffer.append(f"{ilosc} {waluta}")

    return " ".join(buffer)

def waluta_str_na_dict(ciag_znakow):
    # Podział ciągu znaków po spacji
    elementy = ciag_znakow.split()

    # Inicjalizacja słownika
    wynik = {'galeon': 0, 'sykl': 0, 'knut': 0}

    # Przepisanie wartości z ciągu znaków do słownika
    for i in range(0, len(elementy), 2):
        if elementy[i+1].startswith('g'):
            wynik['galeon'] = int(elementy[i])
        elif elementy[i+1].startswith('s'):
            wynik['sykl'] = int(elementy[i])
        elif elementy[i+1].startswith('k'):
            wynik['knut'] = int(elementy[i])

    return wynik

def nadaj_sowe(adresat: str, tresc_wiadomosci: str, potwierdzenie_odbioru: bool, odleglosc: Odleglosc, typ: TypPaczki, specjalna: SpecjalnaPaczka):
    
    koszt = wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt)
    
    potwierdzenie_odbioru_str = "TAK" if potwierdzenie_odbioru else "NIE"
    
    with open("poczta_nadania_lista.csv", "w+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([adresat, tresc_wiadomosci, koszt_str, potwierdzenie_odbioru_str])

