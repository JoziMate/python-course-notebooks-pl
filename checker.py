"""
checker.py
Lekki framework do sprawdzania ćwiczeń w notebookach edukacyjnych,
inspirowany mechanizmem znanym z Kaggle Learn (learntools).

Użycie w notebooku:

    from checker import Question

    q1 = Question(
        answer_check=lambda: moja_zmienna == 42,
        hint="Sprawdź, czy przypisałeś wartość 42 do zmiennej.",
        solution="moja_zmienna = 42"
    )
    q1.check()
    q1.hint()
    q1.solution()
"""


class Question:
    def __init__(self, answer_check, hint=None, solution=None, title=None):
        """
        answer_check: funkcja (lambda lub def) bez argumentów, zwracająca
                      True/False — sprawdza, czy zadanie zostało wykonane poprawnie.
                      Może też zwrócić tuple (bool, str) jeśli chcesz własny komunikat.
        hint:         tekst podpowiedzi wyświetlany na żądanie (q.hint())
        solution:     przykładowe rozwiązanie wyświetlane na żądanie (q.solution())
        title:        opcjonalna nazwa zadania, używana w komunikatach
        """
        self._check = answer_check
        self._hint = hint
        self._solution = solution
        self._title = title or "To zadanie"
        self._completed = False

    def check(self):
        try:
            result = self._check()
        except NameError as e:
            print(f"❌ Wygląda na to, że nie zdefiniowałeś jeszcze potrzebnej zmiennej.\n   Błąd: {e}")
            return
        except Exception as e:
            print(f"❌ Błąd podczas sprawdzania: {e}")
            return

        # Pozwala na zwrócenie (bool, komunikat) dla bardziej szczegółowego feedbacku
        if isinstance(result, tuple):
            ok, message = result
        else:
            ok, message = result, None

        if ok:
            self._completed = True
            print(f"✅ Poprawnie! {self._title} zaliczone.")
            if message:
                print(f"   {message}")
        else:
            print(f"❌ Jeszcze nie tak. Spróbuj ponownie, albo wpisz hint() po nazwie zadania.")
            if message:
                print(f"   {message}")

    def hint(self):
        if self._hint:
            print(f"💡 Podpowiedź: {self._hint}")
        else:
            print("Brak podpowiedzi dla tego zadania.")

    def solution(self):
        print("📘 Przykładowe rozwiązanie:\n")
        print(self._solution or "Brak zapisanego rozwiązania dla tego zadania.")

    @property
    def is_completed(self):
        return self._completed
