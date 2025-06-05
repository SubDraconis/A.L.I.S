import random

TERRAIN_ID = {
    "Trawa": 0,
    "Las": 1,
    "Rzeka": 2,
    "Góry": 3,
    "Wioska": 4,
    "Kościół": 5,
    "Bank": 6,
    "Rząd": 7,
    "Domek": 8
}

def generuj_mape(szerokosc, wysokosc, gestosc_lasu=0.2, gestosc_rzeki=0.1, liczba_wiosek=3):
    mapa = [[TERRAIN_ID["Trawa"] for _ in range(szerokosc)] for _ in range(wysokosc)]

    for y in range(wysokosc):
        for x in range(szerokosc):
            if random.random() < gestosc_lasu:
                mapa[y][x] = TERRAIN_ID["Las"]

    for y in range(wysokosc):
        for x in range(szerokosc):
            if random.random() < gestosc_rzeki:
                mapa[y][x] = TERRAIN_ID["Rzeka"]

    for _ in range(liczba_wiosek):
        x = random.randint(0, szerokosc - 1)
        y = random.randint(0, wysokosc - 1)

        if x + 1 < szerokosc and y + 1 < wysokosc:
            mapa[y][x] = TERRAIN_ID["Kościół"]
            mapa[y][x + 1] = TERRAIN_ID["Bank"]
            mapa[y + 1][x] = TERRAIN_ID["Rząd"]
            mapa[y + 1][x + 1] = TERRAIN_ID["Domek"]

    return mapa

def wyswietl_mape(mapa, postac=None, ai_postac=None):
    terrain_symbols = {
        TERRAIN_ID["Trawa"]: ".",
        TERRAIN_ID["Las"]: "L",
        TERRAIN_ID["Rzeka"]: "~",
        TERRAIN_ID["Góry"]: "^",
        TERRAIN_ID["Wioska"]: "V",
        TERRAIN_ID["Kościół"]: "K",
        TERRAIN_ID["Bank"]: "B",
        TERRAIN_ID["Rząd"]: "R",
        TERRAIN_ID["Domek"]: "D"
    }
    for y, row in enumerate(mapa):
        line = ""
        for x, tile in enumerate(row):
            if postac and postac.x == x and postac.y == y:
                line += "P"
            elif ai_postac and ai_postac.x == x and ai_postac.y == y:
                line += "A"
            else:
                line += terrain_symbols[tile]
        print(line)

szerokosc_mapy = 40
wysokosc_mapy = 20
mapa = generuj_mape(szerokosc_mapy, wysokosc_mapy)
wyswietl_mape(mapa)