from main import * 

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
    wynik = licz_sume(fundusz)
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
    wynik = licz_sume(fundusz)
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
    wynik = licz_sume(fundusz)
    assert wynik == {
        "galeon" : 106,
        "sykl" : 2,
        "knut" : 16
    }

test_licz_sume()


