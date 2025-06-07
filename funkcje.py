import przedmioty
import Postacie as p
import ai
import mapy
import random

# Funkcja do poruszania się postaci
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
    elif kierunek == "zostań":
        print("Postać zostaje w miejscu.")
        return
    else:
        print("Nieprawidłowy kierunek!")
        return

    if 0 <= nowe_x < szerokosc_mapy and 0 <= nowe_y < wysokosc_mapy:
        postac.x = nowe_x
        postac.y = nowe_y

        if mapa[nowe_y][nowe_x] == mapy.TERRAIN_ID["Wioska"]:
            postac.ostatnia_wioska = (nowe_x, nowe_y)
            print("Zapamiętano wioskę!")

        wrog = losowanie_wroga(nowe_x, nowe_y, mapa[nowe_y][nowe_x])
        if wrog:
            print("Zaatakował cię wróg!")
            print(wrog)
    else:
        print("Nie możesz wyjść poza mapę!")

# Funkcja do losowania wroga
def losowanie_wroga(x, y, pole):
    if pole == mapy.TERRAIN_ID["Wioska"]:
        return None
    elif pole == mapy.TERRAIN_ID["Las"] or pole == mapy.TERRAIN_ID["Trawa"]:
        if random.random() < 0.5:
            losowanie = random.random()
            akumulowane_prawdopodobienstwo = 0
            wybrany_wrog = None

            for gatunek, statystyki in p.wrogowie.items():
                akumulowane_prawdopodobienstwo += statystyki["prawdopodobienstwo"]
                if losowanie < akumulowane_prawdopodobienstwo:
                    wybrany_wrog = gatunek
                    break

            if wybrany_wrog:
                imie_wroga = wybrany_wrog
                wrog = p.postacie_map["wrog"](
                    imie=imie_wroga,
                    sila=random.randint(p.wrogowie[wybrany_wrog]["sila"][0], p.wrogowie[wybrany_wrog]["sila"][1]),
                    zrecznosc=random.randint(p.wrogowie[wybrany_wrog]["zrecznosc"][0], p.wrogowie[wybrany_wrog]["zrecznosc"][1]),
                    inteligencja=random.randint(p.wrogowie[wybrany_wrog]["inteligencja"][0], p.wrogowie[wybrany_wrog]["inteligencja"][1]),
                    charyzma=random.randint(p.wrogowie[wybrany_wrog]["charyzma"][0], p.wrogowie[wybrany_wrog]["charyzma"][1]),
                    gatunek=wybrany_wrog
                )
                return wrog
            else:
                return None
        else:
            return None
    elif pole == mapy.TERRAIN_ID["Rzeka"]:
        if random.random() < 0.3:
            imie_wroga = "Wodny Potwór"
            wrog = p.postacie_map["wrog"](
                imie=imie_wroga,
                sila=random.randint(5, 7),
                zrecznosc=random.randint(6, 8),
                inteligencja=random.randint(2, 4),
                charyzma=random.randint(1, 3),
                gatunek="Wodny Potwór"
            )
            return wrog
        else:
            return None
    elif pole == mapy.TERRAIN_ID["Góry"]:
        if random.random() < 0.01:
            imie_wroga = "Górski Smok"
            wrog = p.postacie_map["Smok"](
                imie=imie_wroga,
                sila=random.randint(100, 120),
                zrecznosc=random.randint(5, 7),
                inteligencja=random.randint(300, 500),
                charyzma=random.randint(20, 40),
                gatunek="Górski Smok"
            )
            return wrog
        else:
            return None
    else:
        return None

# Funkcja do walki
def atakuj(postac, wrog):
    if not wrog:
        print("Nie ma wroga do ataku!")
        return True

    while True:
        print(f"{postac.imie} atakuje {wrog.imie}!")
        co_chce_zrobic = input("Co chesz zrobić (atakuj, przekonaj, ucieknij)? ").strip().lower()
        if co_chce_zrobic == "atakuj":
            los_postaci = random.randint(0, 20) + postac.sila
            print(f"Siła ataku {postac.imie}: {los_postaci}")
            los_wroga = random.randint(0, 20) + wrog.sila
            print(f"Siła obrony {wrog.imie}: {los_wroga}")
            if los_postaci > los_wroga:
                wrog.hp -= los_postaci + postac.sila - wrog.pancerz
                print(f"{postac.imie} zadał obrażenia {wrog.imie}! HP wroga: {wrog.hp}")
                if wrog.hp <= 0:
                    print(f"{wrog.imie} został pokonany!")
                    postac.xp += wrog.lvl * 10
                    print(f"{postac.imie} zdobył {wrog.lvl * 10} XP ! Łącznie: {postac.xp}")
                    return "wygrana"
            else:
                postac.hp -= los_wroga + wrog.sila - postac.pancerz
                print(f"{wrog.imie} zadał obrażenia {postac.imie}! HP postaci: {postac.hp}")
                if postac.hp <= 0:
                    print(f"{postac.imie} został pokonany!")
                    if postac.ostatnia_wioska:
                        postac.x, postac.y = postac.ostatnia_wioska
                        print(f"{postac.imie} odradza się w wiosce ({postac.x}, {postac.y})!")
                    else:
                        postac.x = 5
                        postac.y = 5
                        print(f"{postac.imie} odradza się w punkcie startowym ({postac.x}, {postac.y})!")

                    postac.lvl = max(1, postac.lvl // 2)
                    postac.hp = 100
                    print(f"Poziom postaci został obniżony do {postac.lvl}, a HP przywrócone do 100.")
                    return "przegrana"
        elif co_chce_zrobic == "uciekaj":
            print(f"{postac.imie} ucieka!")
            return "ucieczka"
        elif co_chce_zrobic == "przekonaj":
            print(f"{postac.imie} próbuje przekonać {wrog.imie}!")
            return "przekonanie"
        else:
            print("Nieprawidłowa akcja! Wybierz atakuj, ucieknij lub przekonaj.")

# Testowanie funkcji
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

