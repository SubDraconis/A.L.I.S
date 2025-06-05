import Postacie as p
from przedmioty import wyswietl_info_przedmiotu

# Wyświetlanie dostępnych klas postaci
print("Dostępne klasy postaci:")
for klasa, defaults in p.class_defaults.items():
    print(f"\n{klasa.title()}:")
    for atrybut, wartosc in defaults.items():
        if atrybut == "ekwipunek":
            print(f"\nEkwipunek startowy:")
            for przedmiot in wartosc:
                wyswietl_info_przedmiotu(przedmiot)
        else:
            print(f"- {atrybut}: {wartosc}")

# Wybór postaci
wybor = input("\nWybierz postać (Paladyn, Wojownik, Mag, Mieszany): ").strip().lower()

# Pobranie klasy postaci ze słownika
Wybrana_klasa = p.postacie_map.get(wybor)

if Wybrana_klasa:
    # Pobierz domyślne wartości dla wybranej klasy
    defaults = p.class_defaults[wybor]
    
    # Pobierz imię
    wybor_imienia = input("Podaj imię postaci: ").strip()
    
    # Stwórz postać z domyślnymi wartościami
    postac = Wybrana_klasa(
        imie=wybor_imienia,
        sila=defaults["sila"],
        zrecznosc=defaults["zrecznosc"],
        inteligencja=defaults["inteligencja"],
        charyzma=defaults["charyzma"]
    )
    
    # Dodaj ekwipunek
    postac.ekwipunek = defaults["ekwipunek"].copy()
    
    # Wyświetl stworzoną postać
    print("\nStworzono postać:")
    print(postac)
    print("\nSzczegółowe informacje o ekwipunku:")
    for przedmiot in postac.ekwipunek:
        wyswietl_info_przedmiotu(przedmiot)
else:
    print("Nieprawidłowy wybór postaci!")

# Wybór trybu gry
tryb_gry = input("\n Wybierz tryb gry (1 - Z AI, 2 - Z drugim graczem 3 - Sam ): ")

Gra_on = True

while Gra_on:
    if tryb_gry == "1":
        import gra_ai
        gra_ai.start_game(postac)
    elif tryb_gry == "2":
        import drugi_gracz
        drugi_gracz.start_game(postac)
    elif tryb_gry == "3":
        import samodzielna_gra
        samodzielna_gra.start_game(postac)
    else:
        print("Nieprawidłowy wybór trybu gry!")
    
    kontynuacja = input("\nCzy chcesz kontynuować grę? (tak/nie): ").strip().lower()
    if kontynuacja != "tak":
        Gra_on = False
        print("Dziękujemy za grę!")