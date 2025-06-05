from przedmioty import wyswietl_info_przedmiotu, przedmioty_info

class Postac:
    def __init__(self, imie, typ, sila, zrecznosc, inteligencja, charyzma, lvl=1, gatunek=None):
        self.imie = imie
        self.typ = typ
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []
        self.lvl = lvl
        self.gatunek = gatunek

    def __str__(self):
        base_info = f"{self.typ}: {self.imie}, Poziom: {self.lvl}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}"
        if self.gatunek:
            base_info += f", Gatunek: {self.gatunek}"
        return base_info

# Słownik mapujący nazwy postaci na typy
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
        Postac(imie, "Wróg", sila, zrecznosc, inteligencja, charyzma, lvl, gatunek)
}

# Domyślne wartości dla klas (bez zmian)
class_defaults = {
    "paladyn": {
        "sila": 16,
        "zrecznosc": 12,
        "inteligencja": 10,
        "charyzma": 14,
        "ekwipunek": ["Miecz", "Tarcza", "Zbroja płytowa", "Symbol święty"]
    },
    "wojownik": {
        "sila": 18,
        "zrecznosc": 14,
        "inteligencja": 8,
        "charyzma": 10,
        "ekwipunek": ["Topór bojowy", "Zbroja łańcuchowa", "Tarcza"]
    },
    "mag": {
        "sila": 8,
        "zrecznosc": 12,
        "inteligencja": 18,
        "charyzma": 14,
        "ekwipunek": ["Różdżka", "Księga zaklęć", "Szaty maga"]
    },
    "mieszany": {
        "sila": 14,
        "zrecznosc": 14,
        "inteligencja": 14,
        "charyzma": 12,
        "ekwipunek": ["Miecz krótki", "Lekka zbroja", "Księga zaklęć"]
    }
}