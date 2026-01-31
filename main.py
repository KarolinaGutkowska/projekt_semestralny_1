import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QTabWidget, QVBoxLayout, QCheckBox, QLabel, QComboBox, QLineEdit

df = pd.read_csv("pacjenci.csv")


class Okno(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proste GUI z CSV")
        self.setGeometry(300, 300, 500, 500)

        # --- ZMIANA: Dodanie QTabWidget do okna ---
        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(10, 10, 480, 480)

        # --- ZMIANA: Zakładka główna ---
        self.tab_glowna = QWidget()
        self.tabs.addTab(self.tab_glowna, "Zakładka główna")

        self.layout_glowna = QVBoxLayout(self.tab_glowna)

        # --- ZMIANA: Przycisk "Dane" ---
        self.przycisk = QPushButton("Dane")
        self.przycisk.clicked.connect(self.klik)
        self.layout_glowna.addWidget(self.przycisk)

        # --- ZMIANA: Przycisk "Wyświetl dane" ---
        self.przycisk_wyswietl = QPushButton("Wyświetl dane")
        self.przycisk_wyswietl.clicked.connect(self.wyswietl_dane)
        self.layout_glowna.addWidget(self.przycisk_wyswietl)

        # --- ZMIANA: Pole tekstowe ---
        self.pole_tekstowe = QTextEdit()
        self.pole_tekstowe.setPlaceholderText("Tutaj zostaną wyświetlone dane")
        self.pole_tekstowe.setReadOnly(True)
        self.layout_glowna.addWidget(self.pole_tekstowe)

        # --- ZMIANA: Pole do logów ---
        self.pole_logow = QTextEdit()
        self.pole_logow.setPlaceholderText("Tutaj będą logi...")
        self.pole_logow.setReadOnly(True)
        self.layout_glowna.addWidget(self.pole_logow)

        # --- ZMIANA: Zakładka Filtrowanie (pusta, do późniejszego użycia) ---
        self.tab_filtrowanie = QWidget()
        self.tabs.addTab(self.tab_filtrowanie, "Filtrowanie")

        self.layout_filtrowanie = QVBoxLayout(self.tab_filtrowanie)
        # Tutaj można później dodawać widgety do filtrowania
        from PyQt6.QtWidgets import QHBoxLayout, QCheckBox, QLineEdit, QComboBox

        # --- ZMIANA: Opcja 1 – Płeć ---
        self.hbox_plec = QHBoxLayout()
        self.checkbox1 = QCheckBox("Płeć")
        self.hbox_plec.addWidget(self.checkbox1)

        self.combobox_plec = QComboBox()
        self.combobox_plec.addItems(["kobieta", "mężczyzna", "obie"])
        self.hbox_plec.addWidget(self.combobox_plec)

        self.layout_filtrowanie.addLayout(self.hbox_plec)

        # --- ZMIANA: Opcja 2 – Wiek ---
        self.hbox_wiek = QHBoxLayout()
        self.checkbox2 = QCheckBox("Wiek")
        self.hbox_wiek.addWidget(self.checkbox2)

        self.lineedit_wiek_min = QLineEdit()
        self.lineedit_wiek_min.setPlaceholderText("min")
        self.lineedit_wiek_min.setFixedWidth(60)
        self.hbox_wiek.addWidget(self.lineedit_wiek_min)

        self.lineedit_wiek_max = QLineEdit()
        self.lineedit_wiek_max.setPlaceholderText("max")
        self.lineedit_wiek_max.setFixedWidth(60)
        self.hbox_wiek.addWidget(self.lineedit_wiek_max)

        self.layout_filtrowanie.addLayout(self.hbox_wiek)

        # --- ZMIANA: Opcja 3 – Ciśnienie tętnicze ---
        self.hbox_cisnienie = QHBoxLayout()
        self.checkbox3 = QCheckBox("Ciśnienie tętnicze")
        self.hbox_cisnienie.addWidget(self.checkbox3)

        self.lineedit_cisnienie_min = QLineEdit()
        self.lineedit_cisnienie_min.setPlaceholderText("min")
        self.lineedit_cisnienie_min.setFixedWidth(60)
        self.hbox_cisnienie.addWidget(self.lineedit_cisnienie_min)

        self.lineedit_cisnienie_max = QLineEdit()
        self.lineedit_cisnienie_max.setPlaceholderText("max")
        self.lineedit_cisnienie_max.setFixedWidth(60)
        self.hbox_cisnienie.addWidget(self.lineedit_cisnienie_max)

        self.layout_filtrowanie.addLayout(self.hbox_cisnienie)

    def klik(self):
        print("Przycisk 'Dane' został kliknięty")

    def wyswietl_dane(self):
        tekst = df.to_string(index=False)
        self.pole_tekstowe.setText(tekst)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
