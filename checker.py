"""
checker.py
Lekki framework do interaktywnych zadań w notebookach (Jupyter/Colab),
inspirowany mechanizmem learntools z Kaggle Learn.

Użycie w notebooku:

    !wget -q https://raw.githubusercontent.com/JoziMate/python-course-notebooks-pl/main/checker.py
    from checker import Zadanie, ZestawZadan

    zestaw = ZestawZadan("Moduł 1: Zmienne", {
        "z1": Zadanie(zmienna="wiek", oczekiwana=25,
                       podpowiedzi=["Użyj zmiennej o nazwie `wiek`.", "Przypisz wartość 25."],
                       kod_rozwiazania="wiek = 25"),
        "z2": Zadanie(warunek=lambda ns: ns.get("imie", "").istitle(),
                       podpowiedzi=["Pierwsza litera powinna być wielka."],
                       kod_rozwiazania='imie = "Anna"'),
    })
    zestaw.wczytaj()   # tworzy z1, z2 w globalnej przestrzeni notebooka
    zestaw.postep()    # pasek postępu

    # w komórce widza:
    wiek = 25
    z1.sprawdz()
    z1.podpowiedz()
    z1.rozwiazanie()
"""

import sys
from IPython.display import display, Markdown, HTML


ZIELONY = "#1e8e3e"
CZERWONY = "#d93025"


class Zadanie:
    """Pojedyncze zadanie sprawdzające wartość zmiennej lub warunek niestandardowy."""

    def __init__(self, zmienna=None, oczekiwana=None, warunek=None,
                 podpowiedzi=None, kod_rozwiazania=None, opis_rozwiazania=None):
        """
        zmienna          - nazwa zmiennej do sprawdzenia (np. "wiek")
        oczekiwana       - oczekiwana wartość zmiennej `zmienna`
        warunek          - funkcja (przestrzen: dict) -> bool, do niestandardowej logiki
                            (ma priorytet nad zmienna/oczekiwana, jeśli podana)
        podpowiedzi      - lista podpowiedzi (kolejne wywołania .podpowiedz() pokazują następną)
        kod_rozwiazania  - fragment kodu pokazywany jako rozwiązanie
        opis_rozwiazania - opisowe rozwiązanie (gdy kod nie jest potrzebny)
        """
        self.zmienna = zmienna
        self.oczekiwana = oczekiwana
        self.warunek = warunek
        self.podpowiedzi = podpowiedzi or []
        self._indeks_podpowiedzi = 0
        self.kod_rozwiazania = kod_rozwiazania
        self.opis_rozwiazania = opis_rozwiazania
        self.proby = 0
        self.rozwiazane = False

    # --- wewnętrzne ---

    def _przestrzen_wywolujacego(self, glebokosc=2):
        """Zwraca globals() notebooka, czyli ramkę wywołującą .sprawdz()/.wczytaj()."""
        ramka = sys._getframe(glebokosc)
        return ramka.f_globals

    def _wartosc_zmiennej(self, ns):
        if self.zmienna not in ns:
            raise NameError(f"nie znaleziono zmiennej `{self.zmienna}` — czy ją zdefiniowałeś/aś?")
        return ns[self.zmienna]

    # --- publiczne API ---

    def sprawdz(self):
        ns = self._przestrzen_wywolujacego(glebokosc=2)
        self.proby += 1
        try:
            if self.warunek is not None:
                ok = bool(self.warunek(ns))
            else:
                ok = self._wartosc_zmiennej(ns) == self.oczekiwana
        except NameError as e:
            display(HTML(f'<span style="color:{CZERWONY}">⚠️ {e}</span>'))
            return False
        except Exception as e:
            display(HTML(f'<span style="color:{CZERWONY}">⚠️ Błąd podczas sprawdzania: {e}</span>'))
            return False

        if ok:
            self.rozwiazane = True
            display(HTML(f'<span style="color:{ZIELONY};font-weight:bold">'
                          f'✅ Poprawnie! Możesz przejść dalej.</span>'))
        else:
            podpowiedz_info = " Wpisz <code>.podpowiedz()</code> po podpowiedź." if self.podpowiedzi else ""
            display(HTML(f'<span style="color:{CZERWONY}">❌ Jeszcze nie tak.{podpowiedz_info}</span>'))
        return ok

    def podpowiedz(self):
        if not self.podpowiedzi:
            display(Markdown("*Brak podpowiedzi dla tego zadania.*"))
            return
        idx = min(self._indeks_podpowiedzi, len(self.podpowiedzi) - 1)
        display(Markdown(f"💡 **Podpowiedź {idx + 1}/{len(self.podpowiedzi)}:** {self.podpowiedzi[idx]}"))
        self._indeks_podpowiedzi = min(self._indeks_podpowiedzi + 1, len(self.podpowiedzi) - 1)

    def rozwiazanie(self):
        if self.kod_rozwiazania:
            display(Markdown(f"**Rozwiązanie:**\n```python\n{self.kod_rozwiazania}\n```"))
        elif self.opis_rozwiazania:
            display(Markdown(f"**Rozwiązanie:** {self.opis_rozwiazania}"))
        else:
            display(Markdown("*Brak rozwiązania do wyświetlenia.*"))


class ZestawZadan:
    """Grupa zadań (Zadanie) dla jednego modułu/notebooka z podsumowaniem postępu."""

    def __init__(self, nazwa, zadania):
        """zadania: dict {"z1": Zadanie(...), "z2": Zadanie(...), ...}"""
        self.nazwa = nazwa
        self.zadania = zadania

    def wczytaj(self):
        """Wstawia obiekty Zadanie jako zmienne globalne w notebooku (z1, z2, ...)."""
        ns = sys._getframe(1).f_globals
        for klucz, zadanie in self.zadania.items():
            ns[klucz] = zadanie
        nazwy = ", ".join(self.zadania.keys())
        display(Markdown(f"📘 **{self.nazwa}** — załadowano {len(self.zadania)} zadań: `{nazwy}`"))

    def postep(self):
        rozwiazane = sum(z.rozwiazane for z in self.zadania.values())
        razem = len(self.zadania)
        procent = int(100 * rozwiazane / razem) if razem else 0
        wypelnione = procent // 10
        pasek = "🟩" * wypelnione + "⬜" * (10 - wypelnione)
        display(Markdown(f"**Postęp: {rozwiazane}/{razem} zadań ({procent}%)**\n\n{pasek}"))
