# Gra AI - Prosty symulator gry z AI
#--- Importy ---
import random
import Postacie as p
import funkcje
import mapy
import ai

# Funkcja do obliczania stanu na podstawie współrzędnych
def get_state(x, y, szerokosc_mapy, wysokosc_mapy):
    return y * szerokosc_mapy + x

# Funkcja do określania nagrody na podstawie terenu
def get_reward(mapa, x, y):
    if mapa[y][x] == mapy.TERRAIN_ID["Wioska"]:
        return 10
    else:
        return -1

# Główna funkcja gry
def start_game(postac):
    # AI wybiera postać
    ai_postac = p.AICharacter.ai_wybiera_postac()
    print("\nAI wybrało postać:")
    print(ai_postac)
    print(f"Ekwipunek: {', '.join(ai_postac.ekwipunek)}")

    # Generowanie mapy
    szerokosc_mapy = 40
    wysokosc_mapy = 20
    mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

    # Ustawienie początkowych pozycji postaci
    postac.x = 5
    postac.y = 5
    ai_postac.x = 10
    ai_postac.y = 10

    print("\nRozpoczyna się gra...")
    while True:
        # Wyświetlanie mapy i informacji o postaciach
        mapy.wyswietl_mape(mapa, postac, ai_postac)
        print(postac)
        print(ai_postac)

        # Pobieranie ruchu od gracza
        kierunek = input("\nPodaj kierunek ruchu (góra, dół, lewo, prawo, koniec): ").lower()
        if kierunek == "koniec":
            break

        # Wykonanie ruchu gracza
        funkcje.porusz_sie(postac, mapa, kierunek)

        # Określenie stanu AI
        state = get_state(ai_postac.x, ai_postac.y, szerokosc_mapy, wysokosc_mapy)
        # Wybór akcji przez AI
        action = ai_postac.agent.choose_action(state)

        # Określenie nowego stanu AI
        new_state = get_state(ai_postac.x, ai_postac.y, szerokosc_mapy, wysokosc_mapy)
        # Ustalenie nagrody
        reward = 0
        if action == 0:
            ai_kierunek = "góra"
        elif action == 1:
            ai_kierunek = "dół"
        elif action == 2:
            ai_kierunek = "lewo"
        elif action == 3:
            ai_kierunek = "prawo"
        # Losowanie wroga
        Wroga=funkcje.losowanie_wroga(ai_postac.x, ai_postac.y, mapa)
        if Wroga:
            print(f"\nNapotkałeś wroga: {Wroga.imie}")
            funkcje.atakuj(postac, Wroga)
        # Poruszanie się AI
        funkcje.porusz_sie(ai_postac, mapa, ai_kierunek)
        funkcje.losowanie_wroga(ai_postac.x, ai_postac.y, mapa)
        if Wroga:
            print(f"\nAI napotkało wroga: {Wroga.imie}")
            ai_action = ai_postac.agent.choose_action(state)
            if ai_action == 0:
                print("AI atakuje!")
                wynik_walki = funkcje.atakuj(ai_postac, Wroga)
                if wynik_walki == "wygrana":
                    reward = 10
                elif wynik_walki == "przegrana":
                    reward = -10
                else:
                    reward = 1
            elif ai_action == 1:
                print("AI próbuje przekonać!")
                reward = 5
            elif ai_action == 2:
                print("AI ucieka!")
                reward = -2
        # Uczenie się AI
        ai_postac.agent.learn(state, action, reward, new_state)
        if postac.lvl <= 0 or ai_postac.lvl <= 0:
            break

# Uruchomienie gry
if __name__ == "__main__":
    postac = p.AICharacter.ai_wybiera_postac()
    start_game(postac)