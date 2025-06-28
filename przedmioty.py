import random

# Słownik z informacjami o przedmiotach
przedmioty_info = {
    "Miecz": {"typ": "Broń", "obrażenia": "1k6"},
    "Tarcza": {"typ": "Tarcza", "pancerz": 2},
    "Hełm płytowy": {"typ": "Hełm", "pancerz": 2},
    "Napierśnik płytowy": {"typ": "Napierśnik", "pancerz": 4},
    "Spodnie płytowe": {"typ": "Spodnie", "pancerz": 3},
    "Buty płytowe": {"typ": "Buty", "pancerz": 1},
    "Symbol święty": {"typ": "Przedmiot", "opis": "Używany przez Paladynów"},
    "Topór bojowy": {"typ": "Broń", "obrażenia": "1k10"},
    "Hełm łańcuchowy": {"typ": "Hełm", "pancerz": 1},
    "Napierśnik łańcuchowy": {"typ": "Napierśnik", "pancerz": 3},
    "Spodnie łańcuchowe": {"typ": "Spodnie", "pancerz": 2},
    "Buty łańcuchowe": {"typ": "Buty", "pancerz": 1},
    "Różdżka": {"typ": "Broń", "obrażenia": "1k4", "magia": True},
    "Księga zaklęć": {"typ": "Przedmiot", "magia": True},
    "Szaty maga": {"typ": "Pancerz", "pancerz": 1, "magia": True},
    "Miecz krótki": {"typ": "Broń", "obrażenia": "1k6"},
    "Hełm skórzany": {"typ": "Hełm", "pancerz": 1},
    "Napierśnik skórzany": {"typ": "Napierśnik", "pancerz": 2},
    "Spodnie skórzane": {"typ": "Spodnie", "pancerz": 1},
    "Buty skórzane": {"typ": "Buty", "pancerz": 1}
}

# Funkcja do wyświetlania informacji o przedmiocie
def wyswietl_info_przedmiotu(nazwa_przedmiotu):
    if nazwa_przedmiotu in przedmioty_info:
        info = przedmioty_info[nazwa_przedmiotu]
        print(f"  {nazwa_przedmiotu}:")
        for atrybut, wartosc in info.items():
            print(f"    - {atrybut}: {wartosc}")
    else:
        print(f"  Nieznany przedmiot: {nazwa_przedmiotu}")

questy = {
    "1": {"tekst": "Moja córka została porwana przez gobliny, uratuj ją", "nagroda": random.randint(100, 1000)},
    "2": {"tekst": f"Znajdź {random.choice(list(przedmioty_info))}", "nagroda": random.randint(100, 500)},
    "3": {"tekst": "Zabij smoka i przynieś jego głowę", "nagroda": random.randint(10000, 100000)}
}
przyjete_questy = []