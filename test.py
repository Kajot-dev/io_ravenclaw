import main

def test_wybierz_sowe_zwroc_koszt(odbior: bool, odleglosc, typ, specjalna, wynik):
    
    assert(main.wybierz_sowe_zwroc_koszt(odbior, odleglosc, typ, specjalna)) == wynik, "niepoprawny wynik"


test_wybierz_sowe_zwroc_koszt(False, main.Odleglosc.LOKALNA, main.TypPaczki.LIST, main.SpecjalnaPaczka.WYJEC, {"galeon": 0, "sykl": 0, "knut": 6})
test_wybierz_sowe_zwroc_koszt(True, main.Odleglosc.DALEKOBIEZNA, main.TypPaczki.PACZKA, main.SpecjalnaPaczka.NIE_DOTYCZY, {"galeon": 0, "sykl": 2, "knut": 8})
test_wybierz_sowe_zwroc_koszt(False, main.Odleglosc.KRAJOWA, main.TypPaczki.PACZKA, main.SpecjalnaPaczka.LIST_GONCZY, {"galeon": 0, "sykl": 2, "knut": 2})