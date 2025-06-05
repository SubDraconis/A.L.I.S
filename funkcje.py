import przedmioty
import Postacie as p
import ai
import mapy

def porusz_sie(postac, mapa, kierunek):
    szerokosc_mapy = len(mapa[0])
    wysokosc_mapy = len(mapa)

    nowe_x = postac.x
    nowe_y = postac.y

    if kierunek == "góra":
        nowe_y -= 1
    elif kierunek == "dół":
        nowe_y += 1
    elif kierunek == "lewo":
        nowe_x -= 1
    elif kierunek == "prawo":
        nowe_x += 1
    else:
        print("Nieprawidłowy kierunek!")
        return

    if 0 <= nowe_x < szerokosc_mapy and 0 <= nowe_y < wysokosc_mapy:
        if mapa[nowe_y][nowe_x] != mapy.TERRAIN_ID["Góry"]:
            postac.x = nowe_x
            postac.y = nowe_y
        else:
            print("Nie możesz tam iść! To góry!")
    else:
        print("Nie możesz wyjść poza mapę!")

if __name__ == '__main__':
    szerokosc_mapy = 40
    wysokosc_mapy = 20
    mapa = mapy.generuj_mape(szerokosc_mapy, wysokosc_mapy)

    from Postacie import Postac
    postac = Postac("Test", "Testowa", 10, 10, 10, 10)
    postac.x = 5
    postac.y = 5

    mapy.wyswietl_mape(mapa)
    print(postac)

    porusz_sie(postac, mapa, "prawo")
    print(postac)
    mapy.wyswietl_mape(mapa)