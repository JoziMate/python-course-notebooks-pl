# Architektura i decyzje projektowe

Ten dokument wyjaśnia, dlaczego system sprawdzania zadań został zbudowany w taki, a nie inny sposób.

## Inspiracja
Główną inspiracją dla frameworka `checker.py` była biblioteka `learntools` używana w kursach na platformie Kaggle Learn. Chcieliśmy przenieść to doświadczenie (natychmiastowa informacja zwrotna, podpowiedzi wewnątrz notebooka) na grunt polskiego kursu Pythona.

## Decyzje projektowe

### 1. Polskie nazwy w API
Zdecydowaliśmy się na użycie polskich nazw metod i klas (`Zadanie.sprawdz()`, `ZestawZadan.postep()`), mimo że standardem w programowaniu jest język angielski.
- **Dlaczego?** Kurs jest skierowany do osób początkujących z Polski. Chcemy zminimalizować barierę wejścia i uczynić interakcję z kodem jak najbardziej naturalną.
- **Koszt:** Framework jest przez to mniej uniwersalny i nie nadaje się jako biblioteka open-source o zasięgu międzynarodowym. Jest to jednak akceptowalne, ponieważ to narzędzie wewnętrzne kursu.

### 2. Definicje zadań w folderze `cwiczenia/`
Zadania nie są definiowane bezpośrednio w kodzie notebooka, lecz w osobnych plikach `.py`.
- **Dlaczego?** Notebook pozostaje czysty i skupia się na teorii. Uczeń nie widzi logiki sprawdzającej ani rozwiązań (ukrytych w parametrze `kod_rozwiazania`) poprzez proste przesunięcie wzroku w górę do poprzedniej komórki. Ponadto ułatwia to współdzielenie logiki między różnymi wersjami notebooków.

### 3. Pobieranie plików przez `!wget`
W Google Colab nie używamy `git clone` całego repozytorium na starcie.
- **Dlaczego?** `git clone` pobrałby wszystkie materiały, w tym rozwiązania do wszystkich przyszłych modułów. Pobieranie tylko potrzebnych plików (`checker.py` + konkretny plik ćwiczeń) jest szybsze i utrzymuje skupienie ucznia na aktualnym temacie.

### 4. Wykorzystanie `sys._getframe()`
Framework automatycznie odnajduje zmienne w notebooku ucznia.
- **Dlaczego?** Chcieliśmy uniknąć składni typu `z1.sprawdz(globals())`. Dla osoby początkującej `globals()` jest pojęciem abstrakcyjnym i magicznym. Dzięki `_getframe()` API ogranicza się do prostego `z1.sprawdz()`.

## Struktura folderów

```text
.
├── checker.py              # Rdzeń frameworka (współdzielony)
├── cwiczenia/              # Definicje zadań (pliki .py)
│   ├── cwiczenie01_zmienne.py
│   └── ...
├── moduly/                 # Materiały dla ucznia (notebooki)
│   ├── 01_podstawy/
│   │   └── 01_zmienne_i_typy.ipynb
│   └── ...
├── docs/                   # Dokumentacja Diátaxis
├── _szablony/              # Szablony do tworzenia nowych treści
└── README.md
```
