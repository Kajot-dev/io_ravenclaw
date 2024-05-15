from main import licz_sume

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


