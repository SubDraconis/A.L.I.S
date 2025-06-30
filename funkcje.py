import przedmioty
import Postacie as p
import ai
import mapy
import random
import json

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
        return None, False
    else:
        print("Nieprawidłowy kierunek!")
        return None, False

    if 0 <= nowe_x < szerokosc_mapy and 0 <= nowe_y < wysokosc_mapy:
        postac.x = nowe_x
        postac.y = nowe_y

        if mapa[nowe_y][nowe_x] == mapy.TERRAIN_ID["Wioska"]:
            postac.ostatnia_wioska = (nowe_x, nowe_y)
            print("Zapamiętano wioskę!")

        wrog = losowanie_wroga(nowe_x, nowe_y, mapa[nowe_y][nowe_x])
        if wrog:
            return wrog, True  # Zwracamy wroga i informację o ataku
        return None, True # Kontynuacja ruchu
    else:
        print("Nie możesz wyjść poza mapę!")
        return None, False

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
def atakuj_przekonaj_ucieknij(postac, wrog):
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
                        postac.x = 0
                        postac.y = 0
                        print(f"{postac.imie} odradza się w punkcie startowym ({postac.x}, {postac.y})!")

                    postac.lvl = max(1, postac.lvl // 2)
                    postac.xp = 0
                    postac.hp = 100
                    print(f"Poziom postaci został obniżony do {postac.lvl}, a HP przywrócone do 100.")
                    return "przegrana"
        
        
        
        elif co_chce_zrobic == "uciekaj":
            szansa_postaci = random.randint(1, 20) + postac.zrecznosc
            szansa_wroga = random.randint(1, 20) + wrog.zrecznosc
            if szansa_postaci > szansa_wroga:
                print(f"{postac.imie} ucieka!")
                return "ucieczka"
            else:
                postac.hp -= wrog.zrecznosc
                print(f"{postac.imie} nie udało się uciec! HP postaci: {postac.hp}")
        
        
        
        elif co_chce_zrobic == "przekonaj":
            print(f"{postac.imie} próbuje przekonać {wrog.imie}!")
            if postac.charyzma > wrog.inteligencja:
                szansa_postaci = random.randint(1, 20) + postac.charyzma
                print(f"Szansa przekonania {postac.imie}: {szansa_postaci}")
                szansa_wroga = random.randint(1, 20) + wrog.inteligencja
                print(f"Szansa przekonania {wrog.imie}: {szansa_wroga}")
                if szansa_postaci > szansa_wroga:
                    print(f"{postac.imie} przekonał {wrog.imie} do odejścia!")
                    postac.xp += wrog.lvl * 5
                    print(f"{postac.imie} zdobył {wrog.lvl * 5} XP ! Łącznie: {postac.xp}")
                    return "przekonanie"
                else:
                    if szansa_postaci < szansa_wroga:
                        if wrog.inteligencja >= 10:    
                            if postac.sila > wrog.sila:
                                wybor = input(f"{wrog.imie} Daje ci szansę na ucieczkę. Czy chcesz uciec? (tak/nie): ").strip().lower()
                                if wybor == "tak":
                                    print(f"{postac.imie} ucieka przed {wrog.imie}!")
                                    return "ucieczka"
        else:
            print("Nieprawidłowa akcja! Wybierz atakuj, ucieknij lub przekonaj.")

def ai_atakuj_przekonaj_ucieknij(postac, wrog):
    if not wrog:
        print("Nie ma wroga do ataku!")
        return True

    # AI podejmuje decyzję o ataku, przekonaniu lub ucieczce
    akcja = random.choice(["atakuj", "przekonaj", "ucieknij"])

    if akcja == "atakuj":
        print(f"{postac.imie} atakuje {wrog.imie}!")
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
                    postac.x = 0
                    postac.y = 0
                    print(f"{postac.imie} odradza się w punkcie startowym ({postac.x}, {postac.y})!")

                postac.lvl = max(1, postac.lvl // 2)
                postac.hp = 100
                print(f"Poziom postaci został obniżony do {postac.lvl}, a HP przywrócone do 100.")
                return "przegrana"
            return "walka_trwa"  # Walka trwa, ale nikt nie wygrał
    elif akcja == "uciekaj":
        print(f"{postac.imie} ucieka!")
        return "ucieczka"
    elif akcja == "przekonaj":
        print(f"{postac.imie} próbuje przekonać {wrog.imie}!")
        if postac.charyzma > wrog.inteligencja:
            szansa_postaci = random.randint(1, 20) + postac.charyzma
            print(f"Szansa przekonania {postac.imie}: {szansa_postaci}")
            szansa_wroga = random.randint(1, 20) + wrog.inteligencja
            print(f"Szansa przekonania {wrog.imie}: {szansa_wroga}")
            if szansa_postaci > szansa_wroga:
                print(f"{postac.imie} przekonał {wrog.imie} do odejścia!")
                return "przekonanie"
            else:
                if szansa_postaci < szansa_wroga:
                    if wrog.inteligencja >= 10:
                        if postac.sila > wrog.sila:
                            wybor = input(f"{wrog.imie} Daje ci szansę na ucieczkę. Czy chcesz uciec? (tak/nie): ").strip().lower()
                            if wybor == "tak":
                                print(f"{postac.imie} ucieka przed {wrog.imie}!")
                                return "ucieczka"
                            else:
                                postac.hp -= wrog.sila
                                print(f"{postac.imie} został zaatakowany przez {wrog.imie}! HP postaci: {postac.hp}")
        else:
            print("Nie udało się przekonać wroga!")
            return False

# Funkcja do obliczania wymaganej ilości XP do awansu na kolejny poziom    
def wymagane_xp(lvl):
    return 50 * (lvl ** 2) - 50 * lvl

# Funkcja do pokazania ekwpunku postaci
def pokazanie_ekwipunek(postac): #poprawiona nazwa
    if not postac.ekwipunek:
        print("Ekwipunek jest pusty.")
    else:
        print("Twój ekwipunek:")
        for przedmiot in postac.ekwipunek:
            przedmiot.wyswietl_info()

def ubierz_przedmiot(postac, przedmiot): #poprawiona nazwa
    if przedmiot in postac.ekwipunek:
        if przedmiot.typ == "bron": #poprawiona nazwa
            postac.ekwipunek.remove(przedmiot)
            postac.ekwipunek.append(postac.bron)
            postac.bron = przedmiot
            print(f"{postac.imie} ubrał {przedmiot.nazwa} jako broń.")
        elif przedmiot.typ == "napiersnik": #poprawiona nazwa
            postac.ekwipunek.remove(przedmiot)
            postac.ekwipunek.append(postac.napiersnik)
            postac.napiersnik = przedmiot
            print(f"{postac.imie} ubrał {przedmiot.nazwa} jako napiersnik.")
        elif przedmiot.typ == "hełm": #poprawiona nazwa
            postac.ekwipunek.remove(przedmiot)
            postac.ekwipunek.append(postac.hełm)
            postac.hełm = przedmiot
            print(f"{postac.imie} ubrał {przedmiot.nazwa} jako hełm.")
        elif przedmiot.typ == "spodnie": #poprawiona nazwa
            postac.ekwipunek.remove(przedmiot)
            postac.ekwipunek.append(postac.spodnie)
            postac.spodnie = przedmiot
            print(f"{postac.imie} ubrał {przedmiot.nazwa} jako spodnie.")
        elif przedmiot.typ == "buty": #poprawiona nazwa
            postac.ekwipunek.remove(przedmiot)
            postac.ekwipunek.append(postac.buty)
            postac.buty = przedmiot
            print(f"{postac.imie} ubrał {przedmiot.nazwa} jako buty.")
        else:
            print("Nie można ubrać tego przedmiotu.")
    else:
        print("Przedmiot nie znajduje się w ekwipunku.")

def zarzadzaj_ekwipunkiem(postac):
    print("\nEkwipunek:")
    for i, przedmiot in enumerate(postac.ekwipunek):
        print(f"{i+1}. {przedmiot}")

    akcja = input("\nCo chcesz zrobić? (załóż/zdejmij/nic): ").lower()

    if akcja == "załóż":
        try:
            indeks = int(input("Podaj numer przedmiotu do założenia: ")) - 1
            if 0 <= indeks < len(postac.ekwipunek):
                przedmiot = postac.ekwipunek[indeks]
                postac.zaloz_przedmiot(przedmiot)
            else:
                print("Nieprawidłowy numer przedmiotu.")
        except ValueError:
            print("To nie jest liczba!")
    elif akcja == "zdejmij":
        typ_przedmiotu = input("Podaj typ przedmiotu do zdjęcia (Broń, Hełm, Napierśnik, Spodnie, Buty): ").capitalize()
        postac.zdejmij_przedmiot(typ_przedmiotu)
    elif akcja == "nic":
        return
    else:
        print("Nieprawidłowa akcja.")

def ai_zarzadzaj_ekwipunkiem(postac):
    if not postac.ekwipunek:
        return

    akcja = random.choice(["załóż", "zdejmij", "nic"])

    if akcja == "załóż":
        przedmiot = random.choice(postac.ekwipunek)
        postac.zaloz_przedmiot(przedmiot)
    elif akcja == "zdejmij":
        typy_do_zdjecia = []
        if postac.bron: typy_do_zdjecia.append("Broń")
        if postac.hełm: typy_do_zdjecia.append("Hełm")
        if postac.napiersnik: typy_do_zdjecia.append("Napierśnik")
        if postac.spodnie: typy_do_zdjecia.append("Spodnie")
        if postac.buty: typy_do_zdjecia.append("Buty")

        if typy_do_zdjecia:
            typ_przedmiotu = random.choice(typy_do_zdjecia)
            postac.zdejmij_przedmiot(typ_przedmiotu)
    elif akcja == "nic":
        return

def quest(lokalizacja):
    if lokalizacja == "Wioska":
        print("Podchodzi do ciebie burmiszcz i mówi:")
        quest_wybrany = random.choice(list(przedmioty.questy.values()))
        odpowiedz = input(f"czy przyjmujesz to zadanie: {quest_wybrany['tekst']} a nagroda to {quest_wybrany['nagroda']}").lower()
        if odpowiedz == "tak":
            przedmioty.przyjete_questy.append(quest_wybrany)
            return True
        else:
            print("Nie przyjąłeś propozycji")
            return False

# Funkcja do zapisywania stanu gry
def zapisz_gre(postac, mapa, filename="save.json"):
    dane = {
        "postac": {
            "imie": postac.imie,
            "typ": postac.typ,
            "sila": postac.sila,
            "zrecznosc": postac.zrecznosc,
            "inteligencja": postac.inteligencja,
            "charyzma": postac.charyzma,
            "lvl": postac.lvl,
            "xp": postac.xp,
            "hp": postac.hp,
            "x": postac.x,
            "y": postac.y,
            "ekwipunek": postac.ekwipunek,
            "ostatnia_wioska": postac.ostatnia_wioska
        },
        "mapa": mapa
    }
    with open(filename, "w") as f:
        json.dump(dane, f)
    print("Gra została zapisana.")

def wczytaj_gre(filename="save.json"):
    with open(filename, "r") as f:
        dane = json.load(f)
    return dane

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

