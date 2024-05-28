import main
from unittest.mock import patch
import os
import shutil

def test_wyslij_sowe():
    liczba_sukcesow = 0
    liczba_prob = 10000
    
    with patch('main.time.sleep', return_value=None):
        for _ in range(liczba_prob):
            if main.wyslij_sowe("Harry", "Wiadomosc"):
                liczba_sukcesow += 1
    
    wspolczynnik_sukcesow = liczba_sukcesow / liczba_prob
    
    # Sprawdzanie, czy sukces pojawia się w okolicach 85%
    assert 0.80 <= wspolczynnik_sukcesow <= 0.90

test_wyslij_sowe()

def test_wybierz_sowe_zwroc_koszt(odbior: bool, odleglosc, typ, specjalna, wynik):
    
    assert(main.wybierz_sowe_zwroc_koszt(odbior, odleglosc, typ, specjalna)) == wynik, "niepoprawny wynik"


test_wybierz_sowe_zwroc_koszt(False, main.Odleglosc.LOKALNA, main.TypPaczki.LIST, main.SpecjalnaPaczka.WYJEC, {"galeon": 0, "sykl": 0, "knut": 6})
test_wybierz_sowe_zwroc_koszt(True, main.Odleglosc.DALEKOBIEZNA, main.TypPaczki.PACZKA, main.SpecjalnaPaczka.NIE_DOTYCZY, {"galeon": 0, "sykl": 2, "knut": 8})
test_wybierz_sowe_zwroc_koszt(False, main.Odleglosc.KRAJOWA, main.TypPaczki.PACZKA, main.SpecjalnaPaczka.LIST_GONCZY, {"galeon": 0, "sykl": 2, "knut": 2})

def test_waluta_dict_na_str():

    # Test 1: Sprawdzenie podstawowego przypadku
    fundusz_1 = {
    "galeon" : 17,
    "sykl" : 2,
    "knut" : 13
}
    assert main.waluta_dict_na_str(fundusz_1) == "17 galeon 2 sykl 13 knut"


    # Test 2: Sprawdzenie przypadku braku środków
    fundusz_2 = {
    "galeon" : 0,
    "sykl" : 0,
    "knut" : 0
}
    assert main.waluta_dict_na_str(fundusz_2) == ""


    # Test 3: Sprawdzenie dla jednej waluty
    fundusz_3 = {"knut": 1}
    assert main.waluta_dict_na_str(fundusz_3) == "1 knut"


    # Test 4: Sprawdzenie dla dużych wartości
    fundusz_4 = {
    "galeon" : 1000000,
    "sykl" : 500000,
    "knut" : 200000
}
    assert main.waluta_dict_na_str(fundusz_4) == "1000000 galeon 500000 sykl 200000 knut"



test_waluta_dict_na_str()

def test_licz_sume():
    fundusz = {
        "galeon" : [1, 3, 5],
        "sykl" : [18, 20, 10],
        "knut" : [30, 40, 7]
    }
    wynik = main.licz_sume(fundusz)
    assert wynik == {
        "galeon" : 12,
        "sykl" : 0,
        "knut" : 14
    }

    fundusz = {
        "galeon" : [],
        "sykl" : [],
        "knut" : []
    }
    wynik = main.licz_sume(fundusz)
    assert wynik == {
        "galeon" : 0,
        "sykl" : 0,
        "knut" : 0
    }

    fundusz = {
        "galeon" : [100, 0, 0],
        "sykl" : [0, 100, 0],
        "knut" : [0, 0, 100]
    }
    wynik = main.licz_sume(fundusz)
    assert wynik == {
        "galeon" : 106,
        "sykl" : 2,
        "knut" : 16
    }

test_licz_sume()

def test_nadaj_sowe():
    # Remove the file if it exists
    if os.path.exists('poczta_nadania_lista.csv'):
        os.remove('poczta_nadania_lista.csv')
    
    args_sets = [{
        'adresat': 'Hermiona Granger',
        'tresc_wiadomosci': 'Ej pożycz mi 20 złotych',
        'potwierdzenie_odbioru': False,
        'odleglosc': main.Odleglosc.KRAJOWA,
        'typ': main.TypPaczki.LIST,
        'specjalna': main.SpecjalnaPaczka.NIE_DOTYCZY
    }, {
        'adresat': 'Harry Potter',
        'tresc_wiadomosci': 'Przestań pożyczać ode mnie pieniądze',
        'potwierdzenie_odbioru': True,
        'odleglosc': main.Odleglosc.DALEKOBIEZNA,
        'typ': main.TypPaczki.LIST,
        'specjalna': main.SpecjalnaPaczka.WYJEC
    }]
    
    for arg_set in args_sets:
        main.nadaj_sowe(**arg_set)
        
    # Now we check for presence of the file
    assert os.path.exists('poczta_nadania_lista.csv')
    
    # Read the file
    with open('poczta_nadania_lista.csv', 'r') as f:
        content = f.read().strip().splitlines()
        
        # Assert second last line
        assert content[-2] == 'Hermiona Granger,Ej pożycz mi 20 złotych,12 knut,NIE'
        
        # Assert last line
        assert content[-1] == 'Harry Potter,Przestań pożyczać ode mnie pieniądze,31 knut,TAK'

test_nadaj_sowe()