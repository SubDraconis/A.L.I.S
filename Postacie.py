from przedmioty import wyswietl_info_przedmiotu, przedmioty_info
import random
import ai

# Klasa bazowa dla postaci
class Postac:
    # Inicjalizacja postaci
    def __init__(self, imie, typ, sila, zrecznosc, inteligencja, charyzma, lvl=1, gatunek=None, x=0, y=0, xp=0, hp=100, bron=None, napiersnik=None, hełm=None, spodnie=None, buty=None):
        self.imie = imie
        self.typ = typ
        self.sila = sila + (bron.sila if bron else 0)
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []
        self.bron = bron
        self.napiersnik = napiersnik
        self.hełm = hełm
        self.spodnie = spodnie
        self.buty = buty
        self.lvl = lvl
        self.gatunek = gatunek
        self.x = x
        self.y = y
        self.xp = xp
        self.hp = hp
        self.pancerz = (0 + (napiersnik.pancerz if napiersnik else 0) +
                        (hełm.pancerz if hełm else 0) +
                        (spodnie.pancerz if spodnie else 0) +
                        (buty.pancerz if buty else 0))
        self.ostatnia_wioska = None

    # Reprezentacja tekstowa postaci
    def __str__(self):
        base_info = f"{self.typ}: {self.imie}, Poziom: {self.lvl}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}, Pozycja: ({self.x}, {self.y}), XP: {self.xp}, HP: {self.hp}"
        if self.gatunek:
            base_info += f", Gatunek: {self.gatunek}"
        return base_info

    def zaloz_przedmiot(self, przedmiot_nazwa):
        if przedmiot_nazwa in przedmioty_info:
            przedmiot = przedmioty_info[przedmiot_nazwa]
            typ_przedmiotu = przedmiot["typ"]
            if typ_przedmiotu == "Broń":
                self.bron = przedmiot_nazwa
            elif typ_przedmiotu == "Hełm":
                self.hełm = przedmiot_nazwa
            elif typ_przedmiotu == "Napierśnik":
                self.napiersnik = przedmiot_nazwa
            elif typ_przedmiotu == "Spodnie":
                self.spodnie = przedmiot_nazwa
            elif typ_przedmiotu == "Buty":
                self.buty = przedmiot_nazwa
            else:
                print(f"Nie można założyć przedmiotu typu {typ_przedmiotu}.")
                return
            self.ekwipunek.remove(przedmiot_nazwa)
            print(f"{self.imie} założył {przedmiot_nazwa}.")
            self.aktualizuj_pancerz()
        else:
            print(f"Nieznany przedmiot: {przedmiot_nazwa}")

    def zdejmij_przedmiot(self, typ_przedmiotu):
        if typ_przedmiotu == "Broń":
            if self.bron:
                self.ekwipunek.append(self.bron)
                print(f"{self.imie} zdjął {self.bron}.")
                self.bron = None
            else:
                print(f"{self.imie} nie ma założonej broni.")
                return
        elif typ_przedmiotu == "Hełm":
            if self.hełm:
                self.ekwipunek.append(self.hełm)
                print(f"{self.imie} zdjął {self.hełm}.")
                self.hełm = None
            else:
                print(f"{self.imie} nie ma założonego hełmu.")
                return
        elif typ_przedmiotu == "Napierśnik":
            if self.napiersnik:
                self.ekwipunek.append(self.napiersnik)
                print(f"{self.imie} zdjął {self.napiersnik}.")
                self.napiersnik = None
            else:
                print(f"{self.imie} nie ma założonego napierśnika.")
                return
        elif typ_przedmiotu == "Spodnie":
            if self.spodnie:
                self.ekwipunek.append(self.spodnie)
                print(f"{self.imie} zdjął {self.spodnie}.")
                self.spodnie = None
            else:
                print(f"{self.imie} nie ma założonych spodni.")
                return
        elif typ_przedmiotu == "Buty":
            if self.buty:
                self.ekwipunek.append(self.buty)
                print(f"{self.imie} zdjął {self.buty}.")
                self.buty = None
            else:
                print(f"{self.imie} nie ma założonych butów.")
                return
        else:
            print(f"Nieznany typ przedmiotu: {typ_przedmiotu}")
            return
        self.aktualizuj_pancerz()

    def aktualizuj_pancerz(self):
        pancerz = 0
        if self.napiersnik:
            pancerz += przedmioty_info[self.napiersnik]["pancerz"]
        if self.hełm:
            pancerz += przedmioty_info[self.hełm]["pancerz"]
        if self.spodnie:
            pancerz += przedmioty_info[self.spodnie]["pancerz"]
        if self.buty:
            pancerz += przedmioty_info[self.buty]["pancerz"]
        self.pancerz = pancerz

# Klasa dla postaci sterowanych przez AI
class AICharacter(Postac):
    # Inicjalizacja postaci AI
    def __init__(self, imie, typ, sila, zrecznosc, inteligencja, charyzma, lvl, gatunek, agent, x=0, y=0, xp=0, hp=100, pancerz=0):
        super().__init__(imie, typ, sila, zrecznosc, inteligencja, charyzma, lvl, gatunek, x, y, xp, hp, pancerz)
        self.agent = agent

    # Reprezentacja tekstowa postaci AI
    def __str__(self):
        return super().__str__() + f", AI Agent: {type(self.agent).__name__}"

    # Metoda statyczna do tworzenia postaci AI
    @staticmethod
    def ai_wybiera_postac():
        dostepne_postacie = [klasa for klasa in postacie_map.keys() if klasa not in ["npc", "wrog", "Smok"]]
        wybrana_nazwa_postaci = random.choice(dostepne_postacie)
        defaults = class_defaults[wybrana_nazwa_postaci]
        imie = "AI_" + wybrana_nazwa_postaci
        Wybrana_klasa = postacie_map[wybrana_nazwa_postaci]
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

# Mapa dostępnych postaci
postacie_map = {
    "paladyn": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1: 
        Postac(imie, "Paladyn", sila, zrecznosc, inteligencja, charyzma, lvl),
    "wojownik": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1: 
        Postac(imie, "Wojownik", sila, zrecznosc, inteligencja, charyzma, lvl),
    "mag": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1: 
        Postac(imie, "Mag", sila, zrecznosc, inteligencja, charyzma, lvl),
    "mieszany": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1: 
        Postac(imie, "Mieszany", sila, zrecznosc, inteligencja, charyzma, lvl),
    "npc": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1: 
        Postac(imie, "NPC", sila, zrecznosc, inteligencja, charyzma, lvl),
    "wrog": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1, gatunek="Nieznany": 
        Postac(imie, "Wróg", sila, zrecznosc, inteligencja, charyzma, lvl, gatunek),
    "Smok": lambda imie, sila, zrecznosc, inteligencja, charyzma, lvl=1, gatunek="Nieznany":
        Postac(imie, "Smok", sila, zrecznosc, inteligencja, charyzma, lvl, gatunek)
}

# Domyślne wartości dla klas postaci
class_defaults = {
    "paladyn": {
        "typ": "Paladyn",
        "sila": 16,
        "zrecznosc": 12,
        "inteligencja": 10,
        "charyzma": 14,
        "ekwipunek": ["Miecz", "Tarcza", "Zbroja płytowa", "Symbol święty"]
    },
    "wojownik": {
        "typ": "Wojownik",
        "sila": 18,
        "zrecznosc": 14,
        "inteligencja": 8,
        "charyzma": 10,
        "ekwipunek": ["Topór bojowy", "Zbroja łańcuchowa", "Tarcza"]
    },
    "mag": {
        "typ": "Mag",
        "sila": 8,
        "zrecznosc": 12,
        "inteligencja": 18,
        "charyzma": 14,
        "ekwipunek": ["Różdżka", "Księga zaklęć", "Szaty maga"]
    },
    "mieszany": {
        "typ": "Mieszany",
        "sila": 14,
        "zrecznosc": 14,
        "inteligencja": 14,
        "charyzma": 12,
        "ekwipunek": ["Miecz krótki", "Lekka zbroja", "Księga zaklęć"]
    },
    "npc": {
        "typ": "NPC",
        "sila": 10,
        "zrecznosc": 10,
        "inteligencja": 10,
        "charyzma": 10,
        "ekwipunek": []
    }
}

# Definicje wrogów
wrogowie = {
    "Goblin": {"prawdopodobienstwo": 0.5, "sila": (6, 8), "zrecznosc": (8, 10), "inteligencja": (1, 3), "charyzma": (1, 3)},
    "Szkielet": {"prawdopodobienstwo": 0.3, "sila": (7, 9), "zrecznosc": (8, 10), "inteligencja": (4, 6), "charyzma": (3, 5)},
    "Ork": {"prawdopodobienstwo": 0.2, "sila": (9, 11), "zrecznosc": (9, 11), "inteligencja": (7, 9), "charyzma": (6, 8)},
    "Troll": {"prawdopodobienstwo": 0.1, "sila": (12, 14), "zrecznosc": (6, 8), "inteligencja": (3, 5), "charyzma": (2, 4)},
    "Wilkołak": {"prawdopodobienstwo": 0.05, "sila": (15, 17), "zrecznosc": (12, 14), "inteligencja": (5, 7), "charyzma": (4, 6)}
}


