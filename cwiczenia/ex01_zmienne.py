"""
ex01_zmienne.py
Definicje zadań dla modułu 1: Zmienne i typy.
"""

from checker import Zadanie, ZestawZadan

zestaw = ZestawZadan("Moduł 1: Zmienne i typy", {
    "z1": Zadanie(
        zmienna="wiek", oczekiwana=25,
        podpowiedzi=["Użyj zmiennej o nazwie `wiek`.", "Przypisz wartość 25."],
        kod_rozwiazania="wiek = 25"
    ),
    "z2": Zadanie(
        warunek=lambda ns: isinstance(ns.get("cena"), float) and ns["cena"] > 0,
        podpowiedzi=["`cena` powinna być liczbą zmiennoprzecinkową większą od 0."],
        kod_rozwiazania='cena = 19.99'
    ),
})
