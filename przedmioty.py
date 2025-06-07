# Słownik z informacjami o przedmiotach
przedmioty_info = {
    "Miecz": {"typ": "Broń", "obrażenia": "1k6"},
    "Tarcza": {"typ": "Pancerz", "pancerz": 2},
    "Zbroja płytowa": {"typ": "Pancerz", "pancerz": 6},
    "Symbol święty": {"typ": "Przedmiot", "opis": "Używany przez Paladynów"},
    "Topór bojowy": {"typ": "Broń", "obrażenia": "1k10"},
    "Zbroja łańcuchowa": {"typ": "Pancerz", "pancerz": 4},
    "Różdżka": {"typ": "Broń", "obrażenia": "1k4", "magia": True},
    "Księga zaklęć": {"typ": "Przedmiot", "magia": True},
    "Szaty maga": {"typ": "Pancerz", "pancerz": 1, "magia": True},
    "Miecz krótki": {"typ": "Broń", "obrażenia": "1k6"},
    "Lekka zbroja": {"typ": "Pancerz", "pancerz": 3}
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