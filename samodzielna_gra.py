import main
import przedmioty
import Postacie as p
import funkcje
import mapy

# Funkcja do rozpoczęcia samodzielnej gry
def start_game(postac):
    # Generowanie mapy
    szerokosc_mapy = 40
    wysokosc_mapy = 20
    mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

    # Ustawienie początkowej pozycji postaci
    postac.x = 5
    postac.y = 5

    print("\nRozpoczyna się samodzielna gra...")
    while True:
        # Wyświetlanie mapy i informacji o postaci
        mapy.wyswietl_mape(mapa, postac)
        print(postac)

        # Pobieranie ruchu od gracza
        kierunek = input("\nPodaj kierunek ruchu (góra, dół, lewo, prawo, koniec): ").lower()
        if kierunek == "koniec":
            break

        # Wykonanie ruchu gracza
        funkcje.porusz_sie(postac, mapa, kierunek)