# Dokumentacja API: checker.py

Ten dokument zawiera techniczny opis klas i metod dostępnych w frameworku `checker.py`, używanym do automatycznego sprawdzania zadań w kursie.

## Klasa `Zadanie`

Klasa reprezentująca pojedyncze zadanie do wykonania przez ucznia.

### Konstruktor

```python
Zadanie(zmienna=None, oczekiwana=None, warunek=None, podpowiedzi=None, kod_rozwiazania=None, opis_rozwiazania=None)
```

**Parametry:**

* `zmienna` (*str*, opcjonalne): Nazwa zmiennej w przestrzeni globalnej notebooka, która ma zostać sprawdzona.
* `oczekiwana` (*any*, opcjonalne): Oczekiwana wartość zmiennej określonej w parametrze `zmienna`.
* `warunek` (*callable*, opcjonalne): Funkcja (zazwyczaj `lambda`), która przyjmuje słownik (przestrzeń nazw) i zwraca `True` jeśli zadanie jest rozwiązane poprawnie. Ma priorytet nad `zmienna`/`oczekiwana`.
* `podpowiedzi` (*list[str]*, opcjonalne): Lista tekstowych podpowiedzi.
* `kod_rozwiazania` (*str*, opcjonalne): Fragment kodu w Pythonie będący wzorcowym rozwiązaniem.
* `opis_rozwiazania` (*str*, opcjonalne): Tekstowy opis rozwiązania (używany, gdy kod nie jest wystarczający lub potrzebny).

### Atrybuty

* `proby` (*int*): Liczba podjętych prób sprawdzenia zadania.
* `rozwiazane` (*bool*): Czy zadanie zostało poprawnie rozwiązane.

### Metody

#### `.sprawdz()`
Pobiera przestrzeń nazw wywołującego, sprawdza czy zadeklarowana zmienna ma oczekiwaną wartość lub czy spełniony jest warunek niestandardowy. Wyświetla wynik (✅ lub ❌) w notebooku.

#### `.podpowiedz()`
Wyświetla kolejną podpowiedź z listy `podpowiedzi`. Po wyświetleniu ostatniej, kolejne wywołania będą powtarzać ostatnią podpowiedź.

#### `.rozwiazanie()`
Wyświetla wzorcowy kod rozwiązania lub opis rozwiązania.

---

## Klasa `ZestawZadan`

Klasa grupująca zadania dla danego modułu i zarządzająca ich wczytywaniem.

### Konstruktor

```python
ZestawZadan(nazwa, zadania)
```

**Parametry:**

* `nazwa` (*str*): Czytelna nazwa modułu (np. "Moduł 1: Zmienne").
* `zadania` (*dict[str, Zadanie]*): Słownik, gdzie kluczem jest nazwa zmiennej (np. "z1"), a wartością obiekt klasy `Zadanie`.

### Metody

#### `.wczytaj()`
Wstrzykuje obiekty zadań (z1, z2, itd.) bezpośrednio do przestrzeni globalnej notebooka, z którego została wywołana, aby uczeń mógł na nich operować.

#### `.postep()`
Wyświetla podsumowanie postępu: liczbę rozwiązanych zadań, procent ukończenia oraz tekstowy pasek postępu.

---

## Ograniczenia znane

1. **Zależność od `sys._getframe()`**: Framework używa niskopoziomowego dostępu do stosu wywołań, aby automatycznie wykrywać zmienne w notebooku bez konieczności przekazywania `globals()`. Może to nie działać w niektórych specyficznych implementacjach Pythona (choć działa stabilnie w CPythonie, Jupyterze i Google Colab).
2. **Głębokość stosu**: Metody zależą od stałej głębokości stosu wywołań. Dodatkowe warstwy abstrakcji (np. wywoływanie `.sprawdz()` wewnątrz innej funkcji) mogą spowodować błąd znalezienia zmiennych.
3. **Brak trwałego zapisu**: Postęp (atrybuty `rozwiazane`) jest przechowywany tylko w pamięci aktualnej sesji. Po zrestartowaniu środowiska (Runtime) w Colab, postęp zostanie zresetowany.
