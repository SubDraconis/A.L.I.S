#--- Importowanie ---
from przedmioty import wyswietl_info_przedmiotu
import Postacie as p
import gra_ai
import drugi_gracz
import samodzielna_gra

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
wybor = input("\nWybierz postać (Paladyn, Wojownik, Mag, Mieszany): ").strip().lower()

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

# Wybór trybu gry
tryb_gry = input("\n Wybierz tryb gry (1 - Z AI, 2 - Z drugim graczem 3 - Sam ): ")

if tryb_gry == "1":
    gra_ai.start_game(postac)
elif tryb_gry == "2":
    drugi_gracz.start_game(postac)
elif tryb_gry == "3":
    samodzielna_gra.start_game(postac)
else:
    print("Nieprawidłowy wybór trybu gry!")

