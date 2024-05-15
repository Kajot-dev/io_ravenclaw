import main
from unittest.mock import patch

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
