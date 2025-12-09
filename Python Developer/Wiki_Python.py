#---------------------------------------------------------------------------------------
Przykładowe typy zmiennych:

Liczby całkowite (int)
wiek = 25
temperatura = -3

Liczby zmiennoprzecinkowe (float)
waga = 72.5
cena = 19.99

Tekst - String (str)
imie = "Ola"
powitanie = 'Cześć!'

Wartości logiczne (bool)
czy_student = True
czy_pada = False
#---------------------------------------------------------------------------------------
Listy (list) (zbiór wielu wartości, które można dowolnie rozszerzać lub zmniejszać)
liczby = [1, 2, 3, 4]
imiona = ["Ala", "Bartek", "Celina"]

Krotki (tuple) - nie możemy ich modyfikować
koordynaty = (108, 320)

Słowniki (dict) == (para to - klucz: wartość)
osoba = {"imie": "Ola", "wiek": 25}

Zbiory (set) - możemy dodawać lub wyjmować ze zbiorów, przy czym nie mogą się powtarzać obiekty.
liczby = {1, 2, 3, 4}

| Typ danych  | Składnia           | Kolejność                    | Zmiana wartości | Duplikaty                   | Przykład                           |
| ----------- | ------------------ | ---------------------------- | --------------- | --------------------------- | ---------------------------------- |
| **Lista**   | `[]`               | ✅ Tak                        | ✅ Tak           | ✅ Tak                       | `owoce = ["jabłko", "banan"]`      |
| **Krotka**  | `()`               | ✅ Tak                        | ❌ Nie           | ✅ Tak                       | `kolory = ("czerwony", "zielony")` |
| **Słownik** | `{klucz: wartość}` | ❌ (od Pythona 3.7 zachowana) | ✅ Tak           | ❌ Klucze muszą być unikalne | `osoba = {"imię": "Amelka"}`       |
| **Zbiór**   | `{}`               | ❌ Nie                        | ✅ Tak           | ❌ Nie                       | `liczby = {1, 2, 3}`               |

#---------------------------------------------------------------------------------------

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [11, 12, 13, 14, 15, 16,17, 18, 19]

a.append('Jaga')                    #wstawia liczbę lub tekst na końcu listy
a.insert(5, 99)      #wstawia w konkretnie wskazanym miejscu liczbę lub tekst
a.extend('ZMARTWYCHWSTANIE')        #wstawia tekst lub liczbę (tylko jako string) i po przecinku rozbija każdą cyfrę lub literę na końcu listy.
a.pop (10)                          #usuwa poszczególne pozycje, przy czym licząc od 0, 1, itd.
b.remove(19)                        #usuwa dowolnie wskazaną pozycję

print (a)
print (b)
#---------------------------------------------------------------------------------------

| Metoda         | Zachodzące wzorce | Łatwość | Najlepsze do               |
| -------------- | ----------------- | ------- | -------------------------- |
| `.count()`     | ❌                 | ✅✅✅     | szybkie, proste liczenie   |
| `find()`       | ✅                 | ✅✅      | ręczna kontrola pozycji    |
| `re.findall()` | ✅                 | ✅✅      | złożone wzorce, regex      |
| `Counter()`    | ❌                 | ✅✅      | liczenie liter, fragmentów |
| `split()`      | ❌                 | ✅       | proste dzielenie tekstu    |

#-----------------------------------------------------------------------------------------
| Funkcja                           | Działanie                                           |
| --------------------------------- | --------------------------------------------------- |
| `sum(iterable)`                   | Suma wszystkich elementów np. listy                 |
| `len(iterable)`                   | Długość (ilość elementów)                           |
| `min(iterable)` / `max(iterable)` | Najmniejsza / największa wartość                    |
| `abs(x)`                          | Wartość bezwzględna                                 |
| `round(x, n)`                     | Zaokrągla do `n` miejsc po przecinku                |
| `any(iterable)`                   | `True`, jeśli **choć jeden** element jest prawdziwy |
| `all(iterable)`                   | `True`, jeśli **wszystkie** elementy są prawdziwe   |

#-----------------------------------------------------------------------------------------
| Funkcja                  | Działanie                                   |
| ------------------------ | ------------------------------------------- |
| `sorted(iterable)`       | Zwraca posortowaną listę                    |
| `reversed(iterable)`     | Odwraca kolejność                           |
| `enumerate(iterable)`    | Numeruje elementy                           |
| `zip(a, b)`              | Łączy dwa zbiory w pary                     |
| `map(func, iterable)`    | Wykonuje funkcję `func` na każdym elemencie |
| `filter(func, iterable)` | Zwraca tylko elementy spełniające warunek   |

#-----------------------------------------------------------------------------------------
| Funkcja                  | Co robi                      | Po co `key`                                                |
| ------------------------ | ---------------------------- | ---------------------------------------------------------- |
| `sorted(lista, key=...)` | Sortuje elementy             | np. `key=str.lower` – sortowanie ignorujące wielkość liter |
| `max(iterable, key=...)` | Szuka największego elementu  | np. `key=q.count` – „najczęściej występujący element”      |
| `min(iterable, key=...)` | Szuka najmniejszego elementu | np. `key=len` – „najkrótszy element”                       |
| `list.sort(key=...)`     | Sortuje listę w miejscu      | Działa tak samo jak `sorted()`                             |

#-----------------------------------------------------------------------------------------
| Funkcja                 | Działanie                        |
| ----------------------- | -------------------------------- |
| `print()`               | Wyświetla wynik                  |
| `input()`               | Pobiera dane od użytkownika      |
| `open()`                | Otwiera plik                     |
| `type()`                | Sprawdza typ zmiennej            |
| `isinstance(obj, type)` | Sprawdza, czy obiekt ma dany typ |

#-----------------------------------------------------------------------------------------
#Obliczamy resztę z dzielenia:
a = 6
b = 3
print (a % b) #0

c = 5
d = 2
print (c % d) #1

#Wskazujemy na typy liczb int (4) czy float (4.0).

print (type (a + b)) #int
print (type (a - b)) #int
print (type (a * b)) #int
print (type (a / b)) #float

#---------------------------------------------------------------------------------------

Przykładowe warunki (instrukcje):

if (jeśli): Python sprawdza pierwszy warunek. Jeśli warunek jest prawdziwy (True), wykonuje blok kodu znajdujący się pod if.

elif (w przeciwnym razie, jeśli): Jeśli warunek if był fałszywy, Python sprawdza pierwszy warunek elif. Jeśli jest on prawdziwy, wykonuje jego blok kodu i pomija resztę.

else (w przeciwnym razie): Jeśli żaden z poprzednich warunków if lub elif nie był prawdziwy, wykonywany jest blok kodu znajdujący się pod else.
#----------------------------------------------------------------------------------------

używaj print() – gdy chcesz zobaczyć wynik,

używaj return – gdy chcesz dalej pracować z wynikiem (np. użyć go w obliczeniach).

#----------------------------------------------------------------------------------------------

def przywitaj():
    print("Cześć!")
przywitaj()


def ...: → tworzy funkcję (definicja)
przywitaj() → uruchamia funkcję (wywołanie)

#Dlaczego w ogóle tworzymy funkcje? Bo funkcje pozwalają:

#Unikać powtórzeń — zamiast pisać 10 razy ten sam kod, piszesz go raz i wywołujesz wielokrotnie.
#Porządkować kod — dzielisz program na logiczne części.
#Łatwiej wprowadzać zmiany — poprawiasz coś raz, a działa wszędzie.
#Wykorzystywać dane — możesz przekazywać różne argumenty (np. różne ceny).

def nazwa_funkcji(argumenty):
    # ciało funkcji
    instrukcje
    return wynik
#----------------------------------------------------------------------------------------------
#Przykład z Argumentem (imie)
def przywitaj(imie):
    print(f"Cześć, {imie}!")

przywitaj('Karol')
przywitaj('Kate')
#Argumenty dodajesz wtedy, gdy chcesz, by funkcja działała na różnych danych!

#Przykład Bez Argumentu ()
def powitanie():
    print("Cześć wszystkim!")

powitanie()
#Gdy funkcja robi zawsze to samo, argumenty nie są potrzebne!

#----------------------------------------------------------------------------------------------
 assert służy do sprawdzenia, czy coś jest prawdą (czyli czy jakiś warunek zwraca True).
 Jeśli warunek jest prawdziwy, program działa dalej.
 Jeśli nie jest prawdziwy, Python zatrzymuje program i zgłasza błąd AssertionError.


def test_add():
    assert add(3, 5) == 15
    assert add(-1, 1) == -1
    assert add(0, 0) == 0
    assert add(5, 5) == 25

#----------------------------------------------------------------------------------------------
@Dekorator w Pythonie to funkcja, która modyfikuje działanie innej funkcji —
bez konieczności zmieniania jej kodu. Dekorator „owija” funkcję, dodając jej nowe możliwości.
Używa się go ze specjalnym symbolem @ umieszczonym nad definicją funkcji.

def log_decorator(func):
    def wrapper():
        print("➡️ Funkcja się zaraz wykona...")
        func()
        print("✅ Funkcja zakończyła działanie.")
    return wrapper

@log_decorator
def say_hello():
    print("Cześć!")

say_hello()

Co się dzieje:
@log_decorator to dekorator, który „opakowuje” funkcję say_hello.
Kiedy wywołujesz say_hello(), naprawdę wykonuje się wrapper() z dekoratora.
Dzięki temu można dodać nową funkcjonalność (np. logowanie) bez zmiany oryginalnej funkcji.


| Termin                | Znaczenie                                                       |
| --------------------- | --------------------------------------------------------------- |
| **Dekorator**         | Funkcja, która modyfikuje działanie innej funkcji               |
| **`@pytest.fixture`** | Dekorator z `pytest`, który tworzy funkcję pomocniczą (fixture) |
| **Cel dekoratorów**   | Dodanie logiki przed/po wywołaniu funkcji, bez zmiany jej kodu  |

#----------------------------------------------------------------------------------------------
*args → pozwala przekazać dowolną liczbę argumentów pozycyjnych (czyli takich bez nazw).

def suma(*args):
    print(args)
    return sum(args)

print(suma(1, 2, 3, 4, 5, 6))
print(suma(10, 20))

**kwargs → pozwala przekazać dowolną liczbę argumentów nazwanych (czyli takich z nazwami, np. x=5).

kwargs = {'name': 'Ala', 'age': 25, 'city': 'Warszawa'}

for (key, value) in kwargs.items():
    print(f"{key} = {value}")

#----------------------------------------------------------------------------------------------

🧩 Co to jest Selenium
Selenium to biblioteka (framework) do automatyzacji przeglądarki internetowej.
Pozwala Twojemu programowi sterować przeglądarką tak, jak człowiek — klikać przyciski, wypełniać formularze, przewijać strony, pobierać dane itd.


----------------------------------------------------------------------------------------------------------------------------------------
| Metoda                                               | Opis                | Przykład                                                 |
| ---------------------------------------------------- | ------------------- | -------------------------------------------------------- |
| `find_element(By.ID, "id")`                          | znajdź po ID        | `driver.find_element(By.ID, "username")`                 |
| `find_element(By.NAME, "name")`                      | po atrybucie `name` | `driver.find_element(By.NAME, "q")`                      |
| `find_element(By.CLASS_NAME, "class")`               | po klasie CSS       | `driver.find_element(By.CLASS_NAME, "btn")`              |
| `find_element(By.TAG_NAME, "tag")`                   | po znaczniku HTML   | `driver.find_element(By.TAG_NAME, "h1")`                 |
| `find_element(By.LINK_TEXT, "tekst linku")`          | po treści linku     | `driver.find_element(By.LINK_TEXT, "Login")`             |
| `find_element(By.XPATH, "//input[@type='text']")`    | po ścieżce XPath    | `driver.find_element(By.XPATH, "//button[text()='OK']")` |
| `find_element(By.CSS_SELECTOR, "div.class > input")` | po selektorze CSS   | `driver.find_element(By.CSS_SELECTOR, "#id > input")`    |
-----------------------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------
| Działanie                  | Kod                              |
| -------------------------- | -------------------------------- |
| Kliknięcie                 | `element.click()`                |
| Wpisanie tekstu            | `element.send_keys("tekst")`     |
| Wciśnięcie klawisza Enter  | `element.send_keys(Keys.RETURN)` |
| Pobranie tekstu z elementu | `element.text`                   |
| Pobranie wartości atrybutu | `element.get_attribute("href")`  |
-----------------------------------------------------------------



----------------------------------------------------------------------------------------------------------------------------------
| driver.back()         wróć do poprzedniej strony | driver.save_screenshot                              zrzut.png                |
| driver.forward()      przejdź do następnej       | driver.switch_to.window(driver.window_handles[1])   przełącz na drugą kartę  |
| driver.refresh()      odśwież                    | driver.close()                                      zamknij aktualną kartę   |
| driver.get("URL")     otwórz nową stronę         | driver.quit()                                       zamknij całą przeglądarkę|
-----------------------------------------------------------------------------------------------------------------------------------


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Uruchomienie Chrome
driver = webdriver.Chrome()

# Otwórz stronę
driver.get("https://www.yahoo.com")
time.sleep (10)

agree_button = driver.find_element(By.NAME, "agree")
agree_button.click()
time.sleep(60)

# print(alert.text)
# alert.accept()   # OK
# alert.dismiss()  # Anuluj

search_box = driver.find_element(By.ID, "ybar-sbq")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

time.sleep(600)
print(driver.title)
driver.quit()

#----------------------------------------------------------------------------------------------
Fixture w pytest → to funkcja, która:
-> przygotowuje coś dla testu (dane, obiekt, konfigurację, stan aplikacji)
-> jest automatycznie przekazywana do testu jako argument

Jednym zdaniem:
Fixture = „automatyczny dostawca rzeczy potrzebnych do testów”

Czas życia testu:
@pytest.fixture(scope="session")

| Scope    | Znaczenie                          | Użycie |
| -------- | ---------------------------------- | ------ |
| function | Nowa dla każdego testu (domyślnie) |        |
| class    | Jedna dla całej klasy              |        |
| module   | Jedna dla całego pliku             |        |
| session  | Jedna dla całej sesji pytest       |        |

