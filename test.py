import main

def test_wyslij_sowe():
    liczba_sukcesow = 0
    liczba_prob = 10000
    
    for _ in range(liczba_prob):
        if wyslij_sowe("Harry", "Wiadomosc"):
            liczba_sukcesow += 1
    
    wspolczynnik_sukcesow = liczba_sukcesow / liczba_prob
    
    # Sprawdzanie, czy sukces pojawia się w okolicach 85%
    assert 0.80 <= wspolczynnik_sukcesow <= 0.90

    if __name__ == '__main__':
    test_wyslij_sowe()

