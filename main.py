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

przedmioty = []

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

# Słownik przedmiotów i ich statystyk
przedmioty_info = {
    "Miecz": {
        "typ": "broń",
        "obrażenia": 8,
        "waga": 3,
        "wartość": 15,
        "wymagana_siła": 10
    },
    "Tarcza": {
        "typ": "obrona",
        "obrona": 2,
        "waga": 6,
        "wartość": 10,
        "wymagana_siła": 8
    },
    "Zbroja płytowa": {
        "typ": "pancerz",
        "obrona": 8,
        "waga": 20,
        "wartość": 50,
        "wymagana_siła": 15
    },
    "Symbol święty": {
        "typ": "święty",
        "moc_zaklęć": 2,
        "waga": 1,
        "wartość": 25,
        "wymagana_wiara": 10
    },
    "Topór bojowy": {
        "typ": "broń",
        "obrażenia": 10,
        "waga": 4,
        "wartość": 20,
        "wymagana_siła": 12
    },
    "Zbroja łańcuchowa": {
        "typ": "pancerz",
        "obrona": 5,
        "waga": 15,
        "wartość": 30,
        "wymagana_siła": 12
    },
    "Różdżka": {
        "typ": "broń magiczna",
        "obrażenia_magiczne": 6,
        "waga": 1,
        "wartość": 30,
        "wymagana_inteligencja": 12
    },
    "Księga zaklęć": {
        "typ": "magiczny",
        "moc_zaklęć": 4,
        "waga": 2,
        "wartość": 40,
        "wymagana_inteligencja": 14
    },
    "Szaty maga": {
        "typ": "pancerz magiczny",
        "obrona": 3,
        "obrona_magiczna": 5,
        "waga": 4,
        "wartość": 35,
        "wymagana_inteligencja": 10
    },
    "Miecz krótki": {
        "typ": "broń",
        "obrażenia": 6,
        "waga": 2,
        "wartość": 10,
        "wymagana_siła": 8
    },
    "Lekka zbroja": {
        "typ": "pancerz",
        "obrona": 4,
        "waga": 10,
        "wartość": 20,
        "wymagana_siła": 10
    }
}

# Modyfikacja wyświetlania informacji o ekwipunku
def wyswietl_info_przedmiotu(nazwa_przedmiotu):
    info = przedmioty_info.get(nazwa_przedmiotu, {})
    if info:
        print(f"\n{nazwa_przedmiotu}:")
        for atrybut, wartosc in info.items():
            print(f"- {atrybut}: {wartosc}")

# Modyfikacja kodu wyświetlającego informacje o postaci
print("Dostępne klasy postaci:")
for klasa in postacie_map.keys():
    print(f"\n{klasa.title()}:")
    for atrybut, wartosc in class_defaults[klasa].items():
        if atrybut == "ekwipunek":
            print(f"\nEkwipunek startowy:")
            for przedmiot in wartosc:
                wyswietl_info_przedmiotu(przedmiot)
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
    print("\nSzczegółowe informacje o ekwipunku:")
    for przedmiot in postac.ekwipunek:
        wyswietl_info_przedmiotu(przedmiot)
else:
    print("Nieprawidłowy wybór postaci!")

