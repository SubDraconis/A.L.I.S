#--- Importowanie ---
from przedmioty import wyswietl_info_przedmiotu
import Postacie as p
import gra_ai
import drugi_gracz
import samodzielna_gra
import mapy
import random

#--- Główna część programu ---

# Wyświetlanie dostępnych klas postaci
print("Dostępne klasy postaci:")
for klasa, defaults in p.class_defaults.items():
        for atrybut, wartosc in defaults.items():
            if atrybut == "ekwipunek":
                print(f"\nEkwipunek startowy:")
                for przedmiot in wartosc:
                    wyswietl_info_przedmiotu(przedmiot)
            else:
                print(f"- {atrybut}: {wartosc}")

# Wybór postaci przez gracza
while True:
    wybor = input("\nWybierz postać (Paladyn, Wojownik, Mag, Mieszany): ").strip().capitalize()
    if wybor in ["Paladyn", "Wojownik", "Mag", "Mieszany"]:
        break
    else:
        print("Podaj poprawną nazwę postaci!")

Wybrana_klasa = p.postacie_map.get(wybor)

if Wybrana_klasa:
    defaults = p.class_defaults[wybor]
    
    wybor_imienia = input("Podaj imię postaci: ").strip()
    if not wybor_imienia:
        wybor_imienia = "Bezimny"
    
    postac = Wybrana_klasa(
        imie=wybor_imienia,
        sila=defaults["sila"],
        zrecznosc=defaults["zrecznosc"],
        inteligencja=defaults["inteligencja"],
        charyzma=defaults["charyzma"]
    )
    
    postac.ekwipunek = defaults["ekwipunek"].copy()
    
    print("\nStworzono postać:")
    print(postac)
    print("\nSzczegółowe informacje o ekwipunku:")
    for przedmiot in postac.ekwipunek:
        wyswietl_info_przedmiotu(przedmiot)
else:
    print("Nieprawidłowy wybór postaci!")

# Generowanie mapy
szerokosc_mapy = 40
wysokosc_mapy = 20
mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

# Znajdź losową wioskę
wioski = mapy.znajdz_wioski(mapa)
if wioski:
    start_x, start_y = random.choice(wioski)
    postac.x = start_x
    postac.y = start_y
    postac.ostatnia_wioska = (start_x, start_y)
else:
    # fallback jeśli nie ma wioski
    postac.x = 0
    postac.y = 0
    postac.ostatnia_wioska = (0, 0)

# Wybór trybu gry
while True:
    try:
        tryb_gry = int(input("Wybierz tryb gry (1 - Z AI, 2 - Z drugim graczem, 3 - Sam): "))
        if tryb_gry in [1, 2, 3]:
            break
        else:
            print("Podaj liczbę 1, 2 lub 3.")
    except ValueError:
        print("Podaj poprawną liczbę!")

if tryb_gry == 1:
    gra_ai.start_game(postac, mapa)
elif tryb_gry == 2:
    drugi_gracz.start_game(postac, mapa)
elif tryb_gry == 3:
    samodzielna_gra.start_game(postac, mapa)



