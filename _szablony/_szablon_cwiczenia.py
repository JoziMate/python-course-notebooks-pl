"""
cwiczenie{XX}_{temat}.py
Definicje zadań dla modułu {NUMER}: {TYTUŁ MODUŁU}.
Ten plik NIE jest pokazywany widzowi w notebooku — leży w repo
w folderze cwiczenia/, notebook tylko go importuje.

INSTRUKCJA UŻYCIA SZABLONU:
1. Zmień nazwę pliku na: cwiczenieXX_temat.py (XX = numer modułu z zerem wiodącym, np. 02)
2. Zastąp poniższe zadania (z1, z2, ...) właściwą treścią
3. Liczba zadań tutaj MUSI się zgadzać z liczbą zN.sprawdz() w notebooku
4. Usuń ten komentarz z instrukcją przed wgraniem do repo (opcjonalnie)
"""

from checker import Zadanie, ZestawZadan

zestaw = ZestawZadan("Moduł {NUMER}: {TYTUŁ MODUŁU}", {

    # --- Zadanie 1 ---
    # Najprostszy wariant: sprawdzenie wartości jednej zmiennej.
    "z1": Zadanie(
        zmienna="{nazwa_zmiennej}",
        oczekiwana="{oczekiwana_wartość}",
        podpowiedzi=[
            "{podpowiedź 1 — ogólna, np. jakiej funkcji/operatora użyć}",
            "{podpowiedź 2 — bardziej konkretna, blisko rozwiązania}",
        ],
        kod_rozwiazania="{nazwa_zmiennej} = {oczekiwana_wartość}"
    ),

    # --- Zadanie 2 ---
    # Wariant z warunkiem niestandardowym — gdy sama równość nie wystarcza
    # (np. sprawdzenie typu, zakresu wartości, długości listy, kilku warunków naraz).
    "z2": Zadanie(
        warunek=lambda ns: True,  # TODO: zastąp własną logiką, np.:
                                  # isinstance(ns.get("x"), float) and ns["x"] > 0
        podpowiedzi=[
            "{podpowiedź 1}",
        ],
        kod_rozwiazania="{przykładowy kod rozwiązania}"
    ),

    # --- Skopiuj blok wyżej dla kolejnych zadań (z3, z4, ...) ---

})
