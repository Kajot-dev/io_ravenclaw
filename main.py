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

