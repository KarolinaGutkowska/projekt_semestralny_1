import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton, QTextEdit, QTabWidget, QVBoxLayout, QCheckBox, QLabel, QComboBox, QLineEdit

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



        # --- ZMIANA: Dodanie przycisku "Filtruj" w zakładce Filtrowanie ---
        self.przycisk_filtruj = QPushButton("Filtruj")
        self.layout_filtrowanie.addWidget(self.przycisk_filtruj)
        self.przycisk_filtruj.clicked.connect(self.akcja_filtruj)

        # --- ZMIANA: Dodanie nowej zakładki "Tabele" ---
        self.tab_tabele = QWidget()
        self.tabs.addTab(self.tab_tabele, "Tabele")

        self.layout_tabele = QVBoxLayout(self.tab_tabele)
        # Tutaj później można dodawać QTableWidget lub inne widgety do wyświetlania tabel


    def klik(self):
        print("Przycisk 'Dane' został kliknięty")

    def wyswietl_dane(self):
        tekst = df.to_string(index=False)
        self.pole_tekstowe.setText(tekst)

    def akcja_filtruj(self):
        logi = "Filtracja rozpoczęta:\n"

        # --- Opcja 1: Płeć ---
        if self.checkbox1.isChecked():
            plec = self.combobox_plec.currentText()
            logi += f"Płeć: zaznaczona, wybrano -> {plec}\n"
        else:
            logi += "Płeć: niezaznaczona\n"

        # --- Opcja 2: Wiek ---
        if self.checkbox2.isChecked():
            min_wiek = self.lineedit_wiek_min.text() or "brak"
            max_wiek = self.lineedit_wiek_max.text() or "brak"
            logi += f"Wiek: zaznaczony, min -> {min_wiek}, max -> {max_wiek}\n"
        else:
            logi += "Wiek: niezaznaczony\n"

        # --- Opcja 3: Ciśnienie tętnicze ---
        if self.checkbox3.isChecked():
            min_cisn = self.lineedit_cisnienie_min.text() or "brak"
            max_cisn = self.lineedit_cisnienie_max.text() or "brak"
            logi += f"Ciśnienie tętnicze: zaznaczone, min -> {min_cisn}, max -> {max_cisn}\n"
        else:
            logi += "Ciśnienie tętnicze: niezaznaczone\n"

        # --- Wypisanie w polu logów ---
        self.pole_logow.setText(logi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
