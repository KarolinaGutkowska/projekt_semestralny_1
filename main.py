import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit

df = pd.read_csv("pacjenci.csv")


class Okno(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proste GUI z CSV")
        self.setGeometry(300, 300, 500, 400)

        # --- ZMIANA: Przycisk "Dane" (stary przycisk, dla testów) ---
        self.przycisk = QPushButton("Dane", self)
        self.przycisk.setGeometry(50, 20, 100, 30)
        self.przycisk.clicked.connect(self.klik)

        # --- ZMIANA: Przycisk "Wyświetl dane" ---
        self.przycisk_wyswietl = QPushButton("Wyświetl dane", self)
        self.przycisk_wyswietl.setGeometry(200, 20, 120, 30)
        self.przycisk_wyswietl.clicked.connect(self.wyswietl_dane)

        # --- ZMIANA: Pole tekstowe ---
        self.pole_tekstowe = QTextEdit(self)
        self.pole_tekstowe.setGeometry(50, 70, 400, 300)
        self.pole_tekstowe.setPlaceholderText("Tutaj zostaną wyświetlone dane")
        self.pole_tekstowe.setReadOnly(True)  # tylko do odczytu

        # --- ZMIANA: Dodanie pola do logów ---
        self.pole_logow = QTextEdit(self)
        self.pole_logow.setGeometry(50, 380, 400, 100)  # pozycja i rozmiar
        self.pole_logow.setPlaceholderText("Tutaj będą logi...")
        self.pole_logow.setReadOnly(True)  # tylko do odczytu

    def klik(self):
        print("Przycisk 'Dane' został kliknięty")

    # --- ZMIANA: Metoda wyświetlająca dane z CSV w polu tekstowym ---
    def wyswietl_dane(self):
        # Konwertujemy DataFrame na tekst
        tekst = df.to_string(index=False)
        self.pole_tekstowe.setText(tekst)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
