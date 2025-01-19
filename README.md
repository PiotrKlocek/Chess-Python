**Python-Chess**

Gra w szachy napisana w Pythonie z wykorzystaniem bibliotek pygame i tkinter. Aplikacja obsługuje podstawowe zasady gry w szachy, takie jak ruchy figur, bicie, sprawdzanie szacha, mata oraz promocję pionków.

**Funkcje**:
* Pełna graficzna plansza do szachów z pionkami.
* Obsługa zasad gry, w tym:
  * Legalne ruchy dla każdej figury.
  * Wykrywanie szacha i mata.
  * Zamiana pionka na hetmana, gdy ten dojdzie do końca szachownicy
* System tur graczy (naprzemiennie białe i czarne).
* Powiadomienia o końcu gry za pomocą okien dialogowych tkinter.

**Instalacja**:
1. Sklonuj to repozytorium:
   
   git clone https://github.com/Pioter1290/Chess-Python.git
   
   cd Chess-Python

2. Zainstaluj bibliotekę pygame:
 
   pip install pygame

3. Upewnij się, że masz następującą strukturę katalogów dla obrazków:
   main/
   
└── images/

    ├── black_king.png
    ├── white_king.png
    ├── black_queen.png
    ├── white_queen.png
    ├── black_rook.png
    ├── white_rook.png
    ├── black_knight.png
    ├── white_knight.png
    ├── black_bishop.png
    ├── white_bishop.png
    ├── black_pawn.png
    └── white_pawn.png


**Uruchamianie**

1.Uruchom grę:
   
  python main.py
   
2.Użyj myszki, aby wybrać figurę, a następnie kliknij na pole, na które chcesz ją przesunąć. Dozwolone są tylko legalne ruchy.

3.Gra przełącza się między turami białych i czarnych. Powiadomienia o macie wyświetlają się w oknie dialogowym tkinter.

**Klasy:**

* **Pawn:**
  
Reprezentuje pionka. Obsługuje logikę ruchów specyficzną dla tej figury.

* **Queen:**
  
Reprezentuje hetmana. Obsługuje ruchy w rzędach, kolumnach i na przekątnych.

* **King:**
  
Reprezentuje króla. Zawiera logikę ruchów oraz wykrywania szacha.

* **Rook:**
  
Reprezentuje wieżę. Obsługuje ruchy w poziomie i pionie.

* **Knight:**
  
Reprezentuje skoczka. Porusza się w kształcie litery "L".

* **Bishop:**
  
Reprezentuje gońca. Porusza się po przekątnych.

**Logika Gry**

* **Szach:** Gra sprawdza, czy król znajduje się w zagrożeniu po każdym ruchu.
* **Mat:** Gra wykrywa sytuację, w której gracz będący w szachu nie ma żadnych legalnych ruchów.
* **Zamiana pionka:** Pionek, który dotrze do końca planszy, automatycznie zamienia się w hetmana.

  

**Struktura Plików**
- main.py: Główny plik zawierający pętlę gry i logikę renderowania GUI.
- pawn.py, queen.py, king.py, rook.py, knight.py, bishop.py: Pliki definiujące figury szachowe oraz ich logikę ruchów.
- main/images/: Katalog zawierający obrazki figur szachowych.


Gif pokazujący działanie aplikacji:

  
![ezgif-4-64a782a2a8](https://github.com/user-attachments/assets/211f56f4-bafe-4036-9d9f-99db00e56884)
