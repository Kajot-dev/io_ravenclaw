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



