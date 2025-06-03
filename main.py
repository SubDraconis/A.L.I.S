import ai

class Postacie:
    def __init__(self):
        self.postacie = []

class Paladyn:
    def __init__(self, imie, sila, zrecznosc, inteligencja, charyzma):
        self.imie = imie
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []

    def __str__(self):
        return f"Paladyn: {self.imie}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}"

class Wojownik:
    def __init__(self, imie, sila, zrecznosc, inteligencja, charyzma):
        self.imie = imie
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []

    def __str__(self):
        return f"Wojownik: {self.imie}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}"

class Mag:
    def __init__(self, imie, sila, zrecznosc, inteligencja, charyzma):
        self.imie = imie
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []

    def __str__(self):
        return f"Mag: {self.imie}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}"

class Mieszany:
    def __init__(self, imie, sila, zrecznosc, inteligencja, charyzma):
        self.imie = imie
        self.sila = sila
        self.zrecznosc = zrecznosc
        self.inteligencja = inteligencja
        self.charyzma = charyzma
        self.ekwipunek = []

    def __str__(self):
        return f"Mieszany: {self.imie}, Siła: {self.sila}, Zręczność: {self.zrecznosc}, Inteligencja: {self.inteligencja}, Charyzma: {self.charyzma}"

# Słownik mapujący nazwy postaci na klasy
postacie_map = {
    "paladyn": Paladyn,
    "wojownik": Wojownik,
    "mag": Mag,
    "mieszany": Mieszany,
}

# Domyślne wartości dla klas
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

print("Dostępne klasy postaci:")
for klasa in postacie_map.keys():
    print(f"\n{klasa.title()}:")
    for atrybut, wartosc in class_defaults[klasa].items():
        if atrybut == "ekwipunek":
            print(f"- {atrybut}: {', '.join(wartosc)}")
        else:
            print(f"- {atrybut}: {wartosc}")

wybor = input("\nWybierz postać (Paladyn, Wojownik, Mag, Mieszany): ").strip().lower()

# Pobranie klasy postaci ze słownika
Wybrana_klasa = postacie_map.get(wybor)

if Wybrana_klasa:
    # Pobierz domyślne wartości dla wybranej klasy
    defaults = class_defaults[wybor]
    
    # Pobierz imię na końcu
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
    print(f"Ekwipunek: {', '.join(postac.ekwipunek)}")
else:
    print("Nieprawidłowy wybór postaci!")

