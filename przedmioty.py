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
    else:
        print(f"Przedmiot '{nazwa_przedmiotu}' nie istnieje w ekwipunku.")