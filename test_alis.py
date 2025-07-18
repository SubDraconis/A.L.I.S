import unittest
import mapy
import Postacie as p
import funkcje
import os

class TestMapy(unittest.TestCase):
    def test_generuj_mape_ma_wioske(self):
        mapa = mapy.generuj_mape(10, 10)
        wioski = mapy.znajdz_wioski(mapa)
        self.assertGreaterEqual(len(wioski), 1, "Mapa powinna zawierać przynajmniej jedną wioskę")

    def test_czy_w_wiosce_true(self):
        mapa = [[mapy.TERRAIN_ID["Wioska"]]]
        postac = p.Postac("Test", "Paladyn", 10, 10, 10, 10)
        postac.x, postac.y = 0, 0
        self.assertTrue(mapy.czy_w_wiosce(postac, mapa))

    def test_czy_w_wiosce_false(self):
        mapa = [[mapy.TERRAIN_ID["Trawa"]]]
        postac = p.Postac("Test", "Paladyn", 10, 10, 10, 10)
        postac.x, postac.y = 0, 0
        self.assertFalse(mapy.czy_w_wiosce(postac, mapa))

class TestFunkcje(unittest.TestCase):
    def setUp(self):
        self.mapa = [[mapy.TERRAIN_ID["Trawa"] for _ in range(3)] for _ in range(3)]
        self.postac = p.Postac("Test", "Paladyn", 10, 10, 10, 10)
        self.postac.x, self.postac.y = 1, 1

    def test_porusz_sie_gora(self):
        _, ok = funkcje.porusz_sie(self.postac, self.mapa, "góra")
        self.assertTrue(ok)
        self.assertEqual((self.postac.x, self.postac.y), (1, 0))

    def test_porusz_sie_poza_mape(self):
        self.postac.x, self.postac.y = 0, 0
        _, ok = funkcje.porusz_sie(self.postac, self.mapa, "góra")
        self.assertFalse(ok)

    def test_porusz_sie_wioska_zapamietuje(self):
        self.mapa[0][1] = mapy.TERRAIN_ID["Wioska"]
        self.postac.x, self.postac.y = 1, 1
        funkcje.porusz_sie(self.postac, self.mapa, "góra")
        self.assertEqual(self.postac.ostatnia_wioska, (1, 0))

    def test_zapisz_i_wczytaj_gre(self):
        # Przygotuj dane
        self.postac.x = 2
        self.postac.y = 2
        self.postac.ekwipunek = ["Miecz", "Tarcza"]
        self.mapa[2][2] = mapy.TERRAIN_ID["Wioska"]
        filename = "test_save.json"
        # Zapisz grę
        funkcje.zapisz_gre(self.postac, self.mapa, filename)
        self.assertTrue(os.path.exists(filename))
        # Wczytaj grę
        dane = funkcje.wczytaj_gre(filename)
        self.assertEqual(dane["postac"]["x"], 2)
        self.assertEqual(dane["postac"]["y"], 2)
        self.assertIn("Miecz", dane["postac"]["ekwipunek"])
        self.assertEqual(dane["mapa"][2][2], mapy.TERRAIN_ID["Wioska"])
        # Usuń plik testowy
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()