# Jak dodać nowy moduł kursu

Ten przewodnik przeprowadzi Cię przez proces tworzenia i dodawania nowego modułu (notebooka z zadaniami) do repozytorium.

## Krok po kroku

### 1. Kopiowanie szablonów
Skopiuj pliki z folderu `_szablony/` do odpowiednich lokalizacji:
- `_szablony/_szablon_cwiczenia.py` → `cwiczenia/cwiczenieXX_temat.py`
- `_szablony/_szablon_modulu.ipynb` → `moduly/FOLDER_MODULU/XX_nazwa.ipynb`

Pamiętaj o zmianie nazw plików (XX to numer modułu z zerem wiodącym).

### 2. Wypełnianie pliku z zadaniami
Otwórz nowy plik w `cwiczenia/` i:
- Zmień nazwę zestawu w `ZestawZadan`.
- Zdefiniuj zadania `z1`, `z2`, itd.
- Sprawdź poprawność składniową pliku:
  ```bash
  python3 -m ast cwiczenia/cwiczenieXX_temat.py
  ```

### 3. Przygotowanie notebooka
W notebooku (`.ipynb`):
- Wypełnij placeholder-y w nawiasach klamrowych `{...}`.
- Upewnij się, że w komórce konfiguracji (Konfiguracja) URL-e oraz nazwa importu pasują do Twojego nowego pliku z `cwiczenia/`.
- Liczba zadań w notebooku (wywołania `zN.sprawdz()`) MUSI zgadzać się z liczbą zadań zdefiniowanych w pliku `.py`.

### 4. Test lokalny
Zanim wgrasz zmiany, sprawdź czy wszystko działa:
```python
from checker import Zadanie, ZestawZadan
from cwiczenia.cwiczenieXX_temat import zestaw
zestaw.wczytaj()
# Przetestuj ręcznie z1.sprawdz() itd.
```

### 5. Walidacja formatu notebooka
Użyj biblioteki `nbformat`, aby upewnić się, że plik JSON notebooka jest poprawny i posiada unikalne ID komórek:
```python
import nbformat
with open("moduly/...", "r") as f:
    nb = nbformat.read(f, as_version=4)
nbformat.validate(nb)
```

### 6. Commit i test w Colab
1. Wyślij zmiany do repozytorium (`git add`, `commit`, `push`).
2. Otwórz notebook bezpośrednio w Google Colab przez link `Open in Colab`.
3. Uruchom komórki po kolei w **czystej sesji**, aby upewnić się, że `!wget` poprawnie pobiera pliki z `main`.

## Zobacz także
- [Opis techniczny API](../reference/checker-api.md)
- [Architektura systemu](../explanation/architektura.md)
