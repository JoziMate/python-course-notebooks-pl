# Jak uruchomić notebook w Google Colab

Ten przewodnik jest przeznaczony dla osób uczących się, które chcą korzystać z interaktywnych materiałów do kursu.

## Instrukcja uruchomienia

1. **Otwarcie notebooka**: Wejdź do folderu `moduly/` i wybierz interesujący Cię temat. Kliknij w przycisk `Open in Colab` widoczny na górze notebooka.
2. **Logowanie**: Musisz być zalogowany(-a) na swoje konto Google, aby móc uruchamiać kod i zapisywać postępy.
3. **Uruchamianie komórek**: Uruchamiaj komórki po kolei, od samej góry. Możesz to zrobić klikając ikonę "Play" lub używając skrótu `Shift + Enter`.
4. **Zapisywanie pracy**: Zmiany w notebooku nie zapisują się automatycznie w naszym repozytorium. Aby zachować swoje rozwiązania, wybierz `Plik` → `Zapisz kopię na Dysku`.

## Praca z zadaniami

Większość modułów zawiera sekcje "Twoja kolej".
- Napisz swoje rozwiązanie w wyznaczonej komórce kodu.
- Uruchom komórkę z rozwiązaniem.
- Uruchom komórkę poniżej zawierającą `z1.sprawdz()` (lub odpowiedni numer zadania).
- Jeśli masz problem, odkomentuj i uruchom `z1.podpowiedz()` lub `z1.rozwiazanie()`.

## Rozwiązywanie typowych problemów

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `ModuleNotFoundError: No module named 'cwiczenie...'` | Nie uruchomiono komórki "Konfiguracja" na górze. | Wróć do sekcji Konfiguracja i uruchom ją. |
| `NameError: name 'z1' is not defined` | Nie wykonano `zestaw.wczytaj()` lub wystąpił błąd pobierania. | Upewnij się, że komórka konfiguracji wykonała się bez błędów. |
| Błędy po dłuższej przerwie | Sesja Colab wygasła i pliki tymczasowe zostały usunięte. | Wybierz `Środowisko wykonawcze` → `Uruchom ponownie i wykonaj wszystko`. |
| `404 Not Found` podczas `!wget` | Plik zadania nie został jeszcze wgrany do repozytorium lub zmieniono jego nazwę. | Sprawdź czy plik istnieje w folderze `cwiczenia/` na GitHubie. |
