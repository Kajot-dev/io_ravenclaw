import time
import random

def wyslij_sowe(adresat, tresc):
    print(f"Wysłanie sowy do {adresat} z treścią: {tresc}")
    time.sleep(1)
    
    if random.random() <= 0.85:
        print("Sowa dostarczona")
        return True
    else:
        print("Dostarczenie sowy niemożliwe")
        return False
    
def wybierz_sowe_zwroc_koszt(odbior, odleglosc, typ, specjalna):
    koszt = {"galeon": 0, "sykl": 0, "knut": 0}
    koszt['knut'] += 7 if odbior else 0
    koszt['knut'] += 4 if specjalna == "wyjec" else 1 if specjalna == 'list gonczy' else 0

    # [knut, sykl]
    odleglosc_koszt = {
        "lokalna": {"list": [2, 0], "paczka": [7, 0]},
        "krajowa": {"list": [12, 0], "paczka": [2, 1]},
        "dalekobiezna": {"list": [20, 0], "paczka": [1, 2]}
    }

    koszt['knut'] += odleglosc_koszt[odleglosc][typ][0]
    koszt['sykl'] += odleglosc_koszt[odleglosc][typ][1]

    return koszt

def waluta_dict_na_str(fundusz: dict[str, int]) -> str:
    # nie zmieniamy kolejności walut w słowniku
    buffer = []
    for waluta, ilosc in fundusz.items():
        
        if ilosc == 0:
            continue
        
        last_digit = ilosc

        while last_digit >= 10:
            last_digit = last_digit % 10
            
        if last_digit > 1 and last_digit < 5:
            match waluta[-1]:
                case "l":
                    waluta += "e"
                case _:
                    waluta += "y"

        elif last_digit >= 5:
            match waluta[-1]:
                case "l":
                    waluta += "i"
                case _:
                    waluta += "ów"
            
        buffer.append(f"{ilosc} {waluta}")
        
    return " ".join(buffer)



