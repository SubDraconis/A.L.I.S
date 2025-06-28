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
def start_game(postac, mapa):
    # AI wybiera postać
    ai_postac = p.AICharacter.ai_wybiera_postac()
    print("\nAI wybrało postać:")
    print(ai_postac)
    print(f"Ekwipunek: {', '.join(ai_postac.ekwipunek)}")

    szerokosc_mapy = len(mapa[0])
    wysokosc_mapy = len(mapa)

    # Ustawienie początkowych pozycji postaci na wioskę z tej mapy!
    wioski = mapy.znajdz_wioski(mapa)
    if wioski:
        start_x, start_y = random.choice(wioski)
        postac.x = start_x
        postac.y = start_y
        postac.ostatnia_wioska = (start_x, start_y)
    else:
        postac.x = 0
        postac.y = 0
        postac.ostatnia_wioska = (0, 0)

    # To samo dla AI
    if wioski:
        ai_x, ai_y = random.choice(wioski)
        ai_postac.x = ai_x
        ai_postac.y = ai_y
        ai_postac.ostatnia_wioska = (ai_x, ai_y)
    else:
        ai_postac.x = 0
        ai_postac.y = 0
        ai_postac.ostatnia_wioska = (0, 0)

    print("\nRozpoczyna się gra...")
    while True:
        # Wyświetlanie mapy i informacji o postaciach
        mapy.wyswietl_mape(mapa, postac, ai_postac)
        print(postac)
        print(ai_postac)

        # Pobieranie ruchu od gracza
        kierunek = input("\nPodaj kierunek ruchu (góra, dół, lewo, prawo, ekwipunek, koniec): ").lower()
        if kierunek == "koniec":
            break
        elif kierunek == "ekwipunek":
            funkcje.zarzadzaj_ekwipunkiem(postac)
            continue

        

        wrog, ruch_wykonany = funkcje.porusz_sie(postac, mapa, kierunek)
        # Wykonanie ruchu gracza
        x, y = postac.x, postac.y
        pole = mapa[y][x]
        nazwa_pola = mapy.nazwa_terenu(pole)
        if nazwa_pola == "Wioska":
           funkcje.quest(nazwa_pola)
        elif wrog:
            print("\nZaatakował cię wróg!")
            print(wrog)
            wynik_walki = funkcje.atakuj_przekonaj_ucieknij(postac, wrog)
            if wynik_walki == "wygrana":
                print(f"{postac.imie} wygrał!")
            elif wynik_walki == "przegrana":
                print(f"{postac.imie} przegrał!")
            elif wynik_walki == "ucieczka":
                print(f"{postac.imie} uciekł!")
            continue  # Przejście do następnej iteracji pętli
        
        

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
        # Wykonanie ruchu AI
        wrog_ai, ruch_wykonany_ai = funkcje.porusz_sie(ai_postac, mapa, ai_kierunek)

        ai_info = ""  # Inicjalizacja pustego stringa
        if wrog_ai:
            ai_info += f"\nAI napotkało wroga: {wrog_ai.imie}"
            # AI wybiera akcję (0 - atak, 1 - przekonaj, 2 - ucieczka)
            ai_action = ai_postac.agent.choose_action(state)
            if ai_action == 0:
                ai_info += "\nAI atakuje!"
                wynik_walki = funkcje.ai_atakuj_przekonaj_ucieknij(ai_postac, wrog_ai)
                if wynik_walki == "wygrana":
                    ai_info += f"\nAI wygrało! Pozostałe HP: {ai_postac.hp}"
                    reward = 10
                elif wynik_walki == "przegrana":
                    ai_info += f"\nAI przegrało! Pozostałe HP: {ai_postac.hp}"
                    reward = -10
                elif wynik_walki == "ucieczka":
                    ai_info += f"\nAI uciekło!"
                    reward = -2
            elif ai_action == 1:
                ai_info += "\nAI próbuje przekonać!"
                wynik_przekonania = funkcje.ai_atakuj_przekonaj_ucieknij(ai_postac, wrog_ai)
                if wynik_przekonania:
                    ai_info += "\nAI przekonało wroga!"
                    reward = 5
                else:
                    ai_info += "\nAI nie przekonało wroga!"
                    reward = -5
            elif ai_action == 2:
                ai_info += "\nAI ucieka!"
                reward = -2
        else:
            ai_info += "\nAI nie napotkało wroga."

        # Wyświetlenie informacji o AI pod mapą
        mapy.wyswietl_mape(mapa, postac, ai_postac)
        print(postac)
        print(ai_postac)
        print(ai_info)

        # Uczenie się AI
        ai_postac.agent.learn(state, action, reward, new_state)
        if postac.lvl <= 0 or ai_postac.lvl <= 0:
            break
        
        
        if postac.xp >= funkcje.wymagane_xp(postac.lvl):
            postac.xp -= funkcje.wymagane_xp(postac.lvl)
            postac.lvl += 1
            print(f"{postac.imie} awansował na poziom {postac.lvl}!")
        if ai_postac.xp >= funkcje.wymagane_xp(ai_postac.lvl):
            ai_postac.xp -= funkcje.wymagane_xp(ai_postac.lvl)
            ai_postac.lvl += 1
            print(f"{ai_postac.imie} awansował na poziom {ai_postac.lvl}!")

        # AI - Zarządzanie ekwipunkiem
        if random.random() < 0.2:  # 20% szans na zarządzanie ekwipunkiem
            funkcje.ai_zarzadzaj_ekwipunkiem(ai_postac)

# Uruchomienie gry
if __name__ == "__main__":
    postac = p.AICharacter.ai_wybiera_postac()
    mapa = mapy.generuj_mape(40, 20)  # Przykładowe wymiary mapy
    start_game(postac, mapa)