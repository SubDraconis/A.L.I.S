# drugi_gracz.py
import Postacie as p
import funkcje
import mapy

# Funkcja do rozpoczęcia gry dla dwóch graczy
def start_game(postac1):
    # Gracz 2 wybiera postać
    print("\nGracz 2, wybierz swoją postać:")
    wybor2 = input("Wybierz postać (Paladyn, Wojownik, Mag, Mieszany): ").strip().lower()
    Wybrana_klasa2 = p.postacie_map.get(wybor2)

    if Wybrana_klasa2:
        defaults2 = p.class_defaults[wybor2]
        wybor_imienia2 = input("Podaj imię postaci: ").strip()
        if not wybor_imienia2:
            wybor_imienia2 = "Bezimny2"
        postac2 = Wybrana_klasa2(
            imie=wybor_imienia2,
            sila=defaults2["sila"],
            zrecznosc=defaults2["zrecznosc"],
            inteligencja=defaults2["inteligencja"],
            charyzma=defaults2["charyzma"]
        )
        postac2.ekwipunek = defaults2["ekwipunek"].copy()
        print("\nStworzono postać dla Gracza 2:")
        print(postac2)
    else:
        print("Nieprawidłowy wybór postaci dla Gracza 2!")
        return

    # Generowanie mapy
    szerokosc_mapy = 40
    wysokosc_mapy = 20
    mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

    # Ustawienie początkowych pozycji postaci
    postac1.x = 5
    postac1.y = 5
    postac2.x = 10
    postac2.y = 10

    print("\nRozpoczyna się gra dla dwóch graczy...")
    while True:
        # Wyświetlanie mapy i informacji o postaciach
        mapy.wyswietl_mape(mapa, postac1, postac2)
        print(postac1)
        print(postac2)

        # Ruch gracza 1
        kierunek1 = input("\nGracz 1, podaj kierunek ruchu (góra, dół, lewo, prawo, koniec): ").lower()
        if kierunek1 == "koniec":
            break
        funkcje.porusz_sie(postac1, mapa, kierunek1)

        # Ruch gracza 2
        kierunek2 = input("\nGracz 2, podaj kierunek ruchu (góra, dół, lewo, prawo, koniec): ").lower()
        if kierunek2 == "koniec":
            break
        funkcje.porusz_sie(postac2, mapa, kierunek2)