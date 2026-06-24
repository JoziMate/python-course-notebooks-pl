"""
_szablon_cwiczenia.py
INSTRUKCJA UŻYCIA:
1. Skopiuj ten plik do folderu cwiczenia/ i zmień nazwę na cwiczenieXX_{temat}.py
   (np. cwiczenie02_petle.py).
2. Zmień nazwę zestawu ("Moduł {XX}: {Temat}").
3. Dodaj/usuń klucze "z1", "z2", ... odpowiadające liczbie zadań w notebooku.
4. Wypełnij każde Zadanie: ustaw zmienna+oczekiwana LUB warunek, podpowiedzi i kod_rozwiazania.
5. W notebooku zaktualizuj komórkę konfiguracyjną (wget + import).

Ten plik NIE jest pokazywany widzowi w notebooku — leży w repo
w folderze cwiczenia/, notebook tylko go importuje.
"""

from checker import Zadanie, ZestawZadan

zestaw = ZestawZadan("Moduł {XX}: {Temat}", {
    "z1": Zadanie(
        zmienna="{nazwa_zmiennej}",
        oczekiwana={oczekiwana_wartosc},
        podpowiedzi=[
            "{Podpowiedź 1 dla zadania 1.}",
            "{Podpowiedź 2 dla zadania 1.}",
        ],
        kod_rozwiazania="{nazwa_zmiennej} = {oczekiwana_wartosc}"
    ),
    "z2": Zadanie(
        warunek=lambda ns: {wyrazenie_warunku},
        podpowiedzi=[
            "{Podpowiedź 1 dla zadania 2.}",
        ],
        kod_rozwiazania="{przyklad_rozwiazania}"
    ),
    # Dodaj kolejne zadania według potrzeb:
    # "z3": Zadanie(...),
})
