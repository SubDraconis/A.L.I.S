import random

# Definicje terenu
TERRAIN_ID = {
    "Trawa": 0,
    "Las": 1,
    "Woda": 2,
    "Góry": 3,
    "Wioska": 4,
    "Rzeka": 5
}

# Symbole terenu
TERRAIN_SYMBOLS = {
    TERRAIN_ID["Trawa"]: " ",
    TERRAIN_ID["Las"]: "🌲",
    TERRAIN_ID["Woda"]: "🌊",
    TERRAIN_ID["Góry"]: "⛰️",
    TERRAIN_ID["Wioska"]: "🏠",
    TERRAIN_ID["Rzeka"]: "〰️"
}

TERRAIN_NAME = {v: k for k, v in TERRAIN_ID.items()}

def nazwa_terenu(pole):
    return TERRAIN_NAME.get(pole, "Nieznany teren")

# Funkcja do generowania mapy
def generuj_mape(szerokosc, wysokosc):
    mapa = []
    for y in range(wysokosc):
        wiersz = []
        for x in range(szerokosc):
            # Losowanie terenu
            losowy_teren = random.choices(
                [TERRAIN_ID["Trawa"], TERRAIN_ID["Las"], TERRAIN_ID["Woda"], TERRAIN_ID["Góry"], TERRAIN_ID["Rzeka"]],
                weights=[0.6, 0.2, 0.05, 0.05, 0.1]
            )[0]
            wiersz.append(losowy_teren)

        mapa.append(wiersz)

    # Dodawanie wiosek
    liczba_wiosek = random.randint(1, 3)
    for _ in range(liczba_wiosek):
        x = random.randint(0, szerokosc - 1)
        y = random.randint(0, wysokosc - 1)
        mapa[y][x] = TERRAIN_ID["Wioska"]

    return mapa

# Funkcja do wyświetlania mapy
def wyswietl_mape(mapa, postac=None, ai_postac=None):
    for y, wiersz in enumerate(mapa):
        for x, teren in enumerate(wiersz):
            # Wyświetlanie postaci na mapie
            if postac and postac.x == x and postac.y == y:
                print("P", end="")
            elif ai_postac and ai_postac.x == x and ai_postac.y == y:
                print("A", end="")
            else:
                print(TERRAIN_SYMBOLS[teren], end="")
        print()

def znajdz_wioski(mapa):
    wioski = []
    for y, wiersz in enumerate(mapa):
        for x, teren in enumerate(wiersz):
            if teren == TERRAIN_ID["Wioska"]:
                wioski.append((x, y))
    return wioski

def czy_w_wiosce(postac, mapa):
    return mapa[postac.y][postac.x] == TERRAIN_ID["Wioska"]

szerokosc_mapy = 40
wysokosc_mapy = 20
mapa = generuj_mape(szerokosc_mapy, wysokosc_mapy)
wyswietl_mape(mapa)