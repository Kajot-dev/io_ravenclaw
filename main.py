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

# Przykładowe wejścia i wywołanie funkcji
ciag_znakow = "13 knut"
ciag_znakow_1 = "17 galeon 2 sykl 13 knut"

# Wyświetlenie wyników
print(waluta_str_na_dict(ciag_znakow))
print(waluta_str_na_dict(ciag_znakow_1))