# Wyzwanie: AI Game Companion Bot

Bazując na przedstawionym przez Ciebie opisie, oto doprecyzowane cele, zasady i system punktacji dla tego konkretnego wyzwania projektowego.

---
## Cele Projektu

Twoim **głównym celem** jest stworzenie bota (Discord lub CLI) pełniącego rolę towarzysza w grach RPG, realizującego kluczowe funkcje, które wymieniłeś.

### Cele Podstawowe (MVP):
1.  **Działający Interfejs:** Uruchomienie bota jako narzędzia CLI lub podstawowego bota na Discordzie, który reaguje na komendy.
2.  **Implementacja 2 z 5 głównych funkcji** w ich podstawowej formie, na przykład:
    * Prosty generator losowych zdarzeń (np. oparty na liście predefiniowanych zdarzeń).
    * Zarządzanie ekwipunkiem postaci (komendy do dodawania/usuwania/wyświetlania przedmiotów).
3.  **Trwałe Przechowywanie Danych:** Użycie SQLite lub JSON do zapisu np. ekwipunku.

### Cele Rozszerzone:
1.  **Implementacja wszystkich 5 głównych funkcji** wymienionych w Twoim opisie:
    * Generator losowych questów i zdarzeń fabularnych (z wykorzystaniem algorytmów lub opcjonalnie modelu językowego).
    * Pełne zarządzanie inwentarzem.
    * System walki z prostą logiką (rzut kostką, statystyki).
    * Integracja z Text-to-Speech (TTS) dla przynajmniej niektórych narracji/dialogów.
    * Solidna obsługa przez wybrany interfejs (terminal lub Discord).
2.  **Jakość Generowanych Treści:** Generowane questy i zdarzenia są zróżnicowane i interesujące.
3.  **Logika Systemu Walki:** System walki jest grywalny i zrozumiały.

### Cele Bonusowe (Wykraczające ponad podstawę):
1.  **Zaawansowane Generowanie Fabuły:** Jeśli korzystasz z modelu językowego, stworzenie ciekawych promptów i efektywne wykorzystanie jego możliwości. Jeśli tworzysz własne algorytmy, zadbanie o ich złożoność i kreatywność.
2.  **Głosowe Odgrywanie Scen:** Pełniejsze wykorzystanie TTS do nadania botowi charakteru lub odgrywania różnych postaci.
3.  **Personalizacja Bota:** Możliwość dostosowania np. typów generowanych zdarzeń, zasad gry.
4.  **Dokumentacja i Testy:** Stworzenie dokumentacji (np. `README.md`) i ewentualnie prostych testów dla kluczowych funkcji.

---
## Zasady i Wytyczne

1.  **Technologie Główne:**
    * **Python:** Zgodnie z Twoimi zainteresowaniami.
    * **Interfejs:** `discord.py` (dla bota Discord) lub standardowe biblioteki Pythona dla narzędzia CLI. FastAPI jest wymienione, ale bardziej pasowałoby, gdyby bot miał np. webowy interfejs do konfiguracji lub był częścią większego systemu – dla samego Discord bota czy CLI nie jest konieczne.
    * **Baza Danych:** SQLite lub pliki JSON do przechowywania danych.
    * **TTS:** `pyttsx3` lub inna biblioteka TTS dla Pythona.
2.  **Generowanie Treści:** Możesz użyć własnych algorytmów i list losowych lub opcjonalnie zintegrować się z API OpenAI (pamiętając o zarządzaniu kluczami i kosztach, jeśli dotyczy).
3.  **Modularność:** Staraj się pisać kod w sposób zorganizowany, dzieląc go na logiczne moduły/klasy.
4.  **Kreatywność:** Kluczowym elementem jest stworzenie bota, który jest faktycznie pomocnym i interesującym "towarzyszem" – liczy się pomysłowość w generowanych treściach i interakcjach.
5.  **Zakres:** Skup się na dostarczeniu działających funkcji zgodnie z wybranym poziomem zaawansowania.

---
## System Punktacji (do Samooceny)

1.  **Implementacja Głównych Funkcji (max. 60 punktów):**
    * Generator questów/zdarzeń: do 15 pkt (5 za podstawowy, +5 za algorytmiczny/szablonowy, +5 za integrację z LLM/zaawansowane algorytmy)
    * Zarządzanie inwentarzem: do 10 pkt (5 za podstawowe, +5 za rozbudowane np. z wagą, limitami)
    * System walki: do 15 pkt (5 za rzut kostką, +5 za statystyki i tury, +5 za dodatkowe mechaniki)
    * Integracja TTS: do 10 pkt (5 za podstawowe odtwarzanie, +5 za rozbudowane użycie/jakość)
    * Interfejs (CLI/Discord): do 10 pkt (5 za podstawową obsługę, +5 za intuicyjność i dodatkowe komendy)

2.  **Jakość Techniczna (max. 25 punktów):**
    * Struktura kodu i czytelność: do 10 pkt
    * Poprawność działania i obsługa błędów: do 10 pkt
    * Implementacja przechowywania danych (SQLite/JSON): do 5 pkt

3.  **Kreatywność i Użyteczność (max. 15 punktów):**
    * Jakość i oryginalność generowanych treści: do 7 pkt
    * Ogólne wrażenie "towarzysza AI" i grywalność: do 8 pkt

**Maksymalna liczba punktów: 100**

**Poziomy "ukończenia" wyzwania:**

* **Młody Adept AI (MVP):** 30-50 pkt (działający bot z 2-3 podstawowymi funkcjami)
* **Doświadczony Konstruktor Botów:** 51-75 pkt (większość funkcji zaimplementowana, dobra jakość)
* **Arcymistrz Sztucznej Inteligencji Gier:** 76-100 pkt (wszystkie funkcje działają na wysokim poziomie, projekt jest dopracowany i kreatywny)

---