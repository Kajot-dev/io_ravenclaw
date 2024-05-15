import main
import os
import shutil

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
        assert content[-2] == 'Hermiona Granger,Ej pożycz mi 20 złotych,12 knutów,NIE'
        
        # Assert last line
        assert content[-1] == 'Harry Potter,Przestań pożyczać ode mnie pieniądze,31 knutów,TAK'

test_nadaj_sowe()