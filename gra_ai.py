import random
import Postacie as p
import funkcje
import mapy
import ai

class AICharacter:
    def __init__(self, imie, typ, sila, zrecznosc, inteligencja, charyzma, lvl, gatunek, agent):
        self.imie = imie
        self.typ = typ
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []
        self.lvl = lvl
        self.gatunek = gatunek
        self.x = 0
        self.y = 0
        self.agent = agent

    def __str__(self):
        return f"{self.typ}: {self.imie}, Poziom: {self.lvl}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}, Pozycja: ({self.x}, {self.y})"

    @staticmethod
    def ai_wybiera_postac():
        dostepne_postacie = [klasa for klasa in p.postacie_map.keys() if klasa != "npc"]
        wybrana_nazwa_postaci = random.choice(dostepne_postacie)
        defaults = p.class_defaults[wybrana_nazwa_postaci]
        imie = "AI_" + wybrana_nazwa_postaci
        Wybrana_klasa = p.postacie_map[wybrana_nazwa_postaci]
        szerokosc_mapy = 40
        wysokosc_mapy = 20
        agent = ai.QLearningAgent(states=szerokosc_mapy * wysokosc_mapy, actions=4)

        postac = AICharacter(
            imie=imie,
            typ=defaults["typ"],
            sila=defaults["sila"],
            zrecznosc=defaults["zrecznosc"],
            inteligencja=defaults["inteligencja"],
            charyzma=defaults["charyzma"],
            lvl = 1,
            gatunek = None,
            agent = agent
        )
        postac.ekwipunek = defaults["ekwipunek"].copy()
        return postac

def get_state(x, y, szerokosc_mapy, wysokosc_mapy):
    return y * szerokosc_mapy + x

def get_reward(mapa, x, y):
    if mapa[y][x] == mapy.TERRAIN_ID["Wioska"]:
        return 10
    else:
        return -1

def start_game(postac):
    ai_postac = AICharacter.ai_wybiera_postac()
    print("\nAI wybrało postać:")
    print(ai_postac)
    print(f"Ekwipunek: {', '.join(ai_postac.ekwipunek)}")

    szerokosc_mapy = 40
    wysokosc_mapy = 20
    mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

    postac.x = 5
    postac.y = 5
    ai_postac.x = 10
    ai_postac.y = 10

    print("\nRozpoczyna się gra...")
    while True:
        mapy.wyswietl_mape(mapa, postac, ai_postac)
        print(postac)
        print(ai_postac)

        kierunek = input("\nPodaj kierunek ruchu (góra, dół, lewo, prawo, koniec): ").lower()
        if kierunek == "koniec":
            break

        funkcje.porusz_sie(postac, mapa, kierunek)

        state = get_state(ai_postac.x, ai_postac.y, szerokosc_mapy, wysokosc_mapy)
        action = ai_postac.agent.choose_action(state)

        new_state = get_state(ai_postac.x, ai_postac.y, szerokosc_mapy, wysokosc_mapy)
        reward = get_reward(mapa, ai_postac.x, ai_postac.y)

        if action == 0:
            ai_kierunek = "góra"
        elif action == 1:
            ai_kierunek = "dół"
        elif action == 2:
            ai_kierunek = "lewo"
        elif action == 3:
            ai_kierunek = "prawo"
        funkcje.porusz_sie(ai_postac, mapa, ai_kierunek)

        ai_postac.agent.learn(state, action, reward, new_state)

        if postac.lvl <= 0 or ai_postac.lvl <= 0:
            break
