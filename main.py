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