def licz_sume(fundusz):
    geleon = fundusz.get('geleon')
    sykl = fundusz.get('sykl')
    knut = fundusz.get('knut')

    # Obliczanie sumy w knutach
    suma_knutow = geleon * 17 * 21 + sykl * 21 + knut

    # Konwersja na galeony
    ile_galeonow = suma_knutow // (17 * 21)
    suma_knutow %= (17 * 21)
    sredni_nominale = suma_knutow // 21
    suma_knutow %= 21

    # Tworzenie słownika wynikowego
    wynik = {
        'geleon': ile_galeonow,
        'sykl': sredni_nominale,
        'knut': suma_knutow
    }
    return wynik
