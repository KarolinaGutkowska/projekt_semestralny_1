import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QTableWidget, QWidget, QTableWidgetItem, QPushButton, QTextEdit, QTabWidget, QVBoxLayout, QCheckBox, QLabel, QComboBox, QLineEdit

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
        self.checkbox1 = QCheckBox("płeć")
        self.hbox_plec.addWidget(self.checkbox1)

        self.combobox_plec = QComboBox()
        self.combobox_plec.addItems(["K", "M", "obie"])
        self.hbox_plec.addWidget(self.combobox_plec)

        self.layout_filtrowanie.addLayout(self.hbox_plec)

        # --- ZMIANA: Opcja 2 – Wiek ---
        self.hbox_wiek = QHBoxLayout()
        self.checkbox2 = QCheckBox("wiek")
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
        self.checkbox3 = QCheckBox("ciśnienie_krwi")
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

        # --- ZMIANA: Dodanie nowej zakładki "Tabela przefiltrowana" ---
        self.tab_tabela_przefiltrowana = QWidget()
        self.tabs.addTab(self.tab_tabela_przefiltrowana, "Tabela przefiltrowana")

        self.layout_tabela_przefiltrowana = QVBoxLayout(self.tab_tabela_przefiltrowana)

    def klik(self):
        print("Przycisk 'Dane' został kliknięty")

    def wyswietl_dane(self):
        tekst = df.to_string(index=False)
        self.pole_tekstowe.setText(tekst)

    def akcja_filtruj(self):
        logi = ">>> START filtracji\n"

        # 1️⃣ Stwórz kopię danych
        df_filtr = df.copy()
        logi += f"Początkowy df_filtr.shape: {df_filtr.shape}\n"
        logi += f"{df_filtr.head()}\n\n"
        print(">>> START filtracji, początkowy df_filtr.shape:", df_filtr.shape)
        print(df_filtr.head())

        # --- Opcja 1: Płeć ---
        if self.checkbox1.isChecked():
            plec = self.combobox_plec.currentText()
            logi += f"Płeć: zaznaczona, wybrano -> {plec}\n"
            try:
                if plec.lower() != "obie":
                    maska = (df_filtr['płeć'].str.strip().str.lower() == plec.lower())
                    df_filtr = df_filtr[maska]
            except KeyError as e:
                logi += f"Błąd: brak kolumny {e}\n"
            logi += f">>> Po filtrze płeć: {df_filtr.shape}\n"
            logi += f"{df_filtr.head()}\n\n"
            print(">>> Po filtrze płeć:", df_filtr.shape)
            print(df_filtr.head())
        else:
            logi += "Płeć: niezaznaczona\n\n"

        # --- Opcja 2: Wiek ---
        if self.checkbox2.isChecked():
            min_wiek = self.lineedit_wiek_min.text()
            max_wiek = self.lineedit_wiek_max.text()
            logi += f"Wiek: zaznaczony, min -> {min_wiek or 'brak'}, max -> {max_wiek or 'brak'}\n"
            try:
                if min_wiek.isdigit():
                    df_filtr = df_filtr[df_filtr['wiek'] >= int(min_wiek)]
                if max_wiek.isdigit():
                    df_filtr = df_filtr[df_filtr['wiek'] <= int(max_wiek)]
            except KeyError as e:
                logi += f"Błąd: brak kolumny {e}\n"
            logi += f">>> Po filtrze wiek: {df_filtr.shape}\n"
            logi += f"{df_filtr.head()}\n\n"
            print(">>> Po filtrze wiek:", df_filtr.shape)
            print(df_filtr.head())
        else:
            logi += "Wiek: niezaznaczony\n\n"

        # --- Opcja 3: Ciśnienie tętnicze ---
        if self.checkbox3.isChecked():
            min_cisn = self.lineedit_cisnienie_min.text()
            max_cisn = self.lineedit_cisnienie_max.text()
            logi += f"Ciśnienie tętnicze: zaznaczone, min -> {min_cisn or 'brak'}, max -> {max_cisn or 'brak'}\n"
            try:
                if min_cisn.isdigit():
                    df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] >= int(min_cisn)]
                if max_cisn.isdigit():
                    df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] <= int(max_cisn)]
            except KeyError as e:
                logi += f"Błąd: brak kolumny {e}\n"
            logi += f">>> Po filtrze ciśnienie: {df_filtr.shape}\n"
            logi += f"{df_filtr.head()}\n\n"
            print(">>> Po filtrze ciśnienie:", df_filtr.shape)
            print(df_filtr.head())
        else:
            logi += "Ciśnienie tętnicze: niezaznaczone\n\n"

        # --- Końcowe informacje ---
        logi += f">>> df_filtr końcowy: {df_filtr.shape}\n"
        logi += f"{df_filtr.head()}\n"
        self.pole_logow.setText(logi)
        print(">>> df_filtr końcowy:", df_filtr.shape)
        print(df_filtr.head())

        # --- Wywołanie funkcji tworzącej tabelę ---
        self.pokaz_tabele_przefiltrowana(df_filtr)

        def akcja_filtruj(self):
            logi = ">>> START filtracji\n"
            df_filtr = df.copy()

            # --- Filtr Płeć ---
            if self.checkbox1.isChecked():
                plec = self.combobox_plec.currentText()
                logi += f"Płeć: zaznaczona, wybrano -> {plec}\n"
                try:
                    if plec.lower() != "obie":
                        df_filtr = df_filtr[df_filtr['płeć'].str.strip().str.lower() == plec.lower()]
                except KeyError as e:
                    logi += f"Błąd: brak kolumny {e}\n"
                print(">>> Po filtrze płeć:", df_filtr.shape)
            else:
                logi += "Płeć: niezaznaczona\n"

            # --- Filtr Wiek ---
            if self.checkbox2.isChecked():
                min_wiek = self.lineedit_wiek_min.text()
                max_wiek = self.lineedit_wiek_max.text()
                logi += f"Wiek: zaznaczony, min -> {min_wiek or 'brak'}, max -> {max_wiek or 'brak'}\n"
                try:
                    if min_wiek.isdigit():
                        df_filtr = df_filtr[df_filtr['wiek'] >= int(min_wiek)]
                    if max_wiek.isdigit():
                        df_filtr = df_filtr[df_filtr['wiek'] <= int(max_wiek)]
                except KeyError as e:
                    logi += f"Błąd: brak kolumny {e}\n"
                print(">>> Po filtrze wiek:", df_filtr.shape)
            else:
                logi += "Wiek: niezaznaczony\n"

            # --- Filtr Ciśnienie ---
            if self.checkbox3.isChecked():
                min_cisn = self.lineedit_cisnienie_min.text()
                max_cisn = self.lineedit_cisnienie_max.text()
                logi += f"Ciśnienie tętnicze: zaznaczone, min -> {min_cisn or 'brak'}, max -> {max_cisn or 'brak'}\n"
                try:
                    if min_cisn.isdigit():
                        df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] >= int(min_cisn)]
                    if max_cisn.isdigit():
                        df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] <= int(max_cisn)]
                except KeyError as e:
                    logi += f"Błąd: brak kolumny {e}\n"
                print(">>> Po filtrze ciśnienie:", df_filtr.shape)
            else:
                logi += "Ciśnienie tętnicze: niezaznaczone\n"

    def akcja_filtruj(self):
        logi = ">>> Filtracja rozpoczęta:\n"

        # 1️⃣ Stwórz kopię danych
        df_filtr = df.copy()
        logi += f"Start df_filtr.shape: {df_filtr.shape}\n"
        logi += f"{df_filtr.head()}\n"
        print(logi)

        # --- Opcja 1: Płeć ---
        if self.checkbox1.isChecked():
            plec = self.combobox_plec.currentText()
            logi += f">>> Płeć: zaznaczona, wybrano -> {plec}\n"
            try:
                if plec.lower() != "obie":
                    df_filtr = df_filtr[df_filtr['płeć'].str.strip().str.lower() == plec.lower()]
                logi += f">>> Po filtrze płeć df_filtr.shape: {df_filtr.shape}\n"
                logi += f"{df_filtr.head()}\n"
            except KeyError as e:
                logi += f"!!! Błąd: brak kolumny {e}\n"
            except Exception as e:
                logi += f"!!! Inny błąd przy filtrze płeć: {e}\n"
        else:
            logi += ">>> Płeć: niezaznaczona\n"

        # --- Opcja 2: Wiek ---
        if self.checkbox2.isChecked():
            min_wiek = self.lineedit_wiek_min.text()
            max_wiek = self.lineedit_wiek_max.text()
            logi += f">>> Wiek: zaznaczony, min -> {min_wiek or 'brak'}, max -> {max_wiek or 'brak'}\n"
            try:
                df_filtr['wiek'] = pd.to_numeric(df_filtr['wiek'], errors='coerce')
                if min_wiek.isdigit():
                    df_filtr = df_filtr[df_filtr['wiek'] >= int(min_wiek)]
                if max_wiek.isdigit():
                    df_filtr = df_filtr[df_filtr['wiek'] <= int(max_wiek)]
                logi += f">>> Po filtrze wiek df_filtr.shape: {df_filtr.shape}\n"
                logi += f"{df_filtr.head()}\n"
            except KeyError as e:
                logi += f"!!! Błąd: brak kolumny {e}\n"
            except Exception as e:
                logi += f"!!! Inny błąd przy filtrze wiek: {e}\n"
        else:
            logi += ">>> Wiek: niezaznaczony\n"

        # --- Opcja 3: Ciśnienie tętnicze ---
        if self.checkbox3.isChecked():
            min_cisn = self.lineedit_cisnienie_min.text()
            max_cisn = self.lineedit_cisnienie_max.text()
            logi += f">>> Ciśnienie tętnicze: zaznaczone, min -> {min_cisn or 'brak'}, max -> {max_cisn or 'brak'}\n"
            try:
                df_filtr['ciśnienie_krwi'] = pd.to_numeric(df_filtr['ciśnienie_krwi'], errors='coerce')
                if min_cisn.isdigit():
                    df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] >= int(min_cisn)]
                if max_cisn.isdigit():
                    df_filtr = df_filtr[df_filtr['ciśnienie_krwi'] <= int(max_cisn)]
                logi += f">>> Po filtrze ciśnienie df_filtr.shape: {df_filtr.shape}\n"
                logi += f"{df_filtr.head()}\n"
            except KeyError as e:
                logi += f"!!! Błąd: brak kolumny {e}\n"
            except Exception as e:
                logi += f"!!! Inny błąd przy filtrze ciśnienie: {e}\n"
        else:
            logi += ">>> Ciśnienie tętnicze: niezaznaczone\n"

        # --- Logi w GUI ---
        self.pole_logow.setText(logi)
        print(">>> df_filtr końcowy:", df_filtr.shape)
        print(df_filtr.head())

        # --- Tworzymy grupy wiekowe ---
        try:
            df_filtr['grupa_wiekowa'] = pd.cut(
                df_filtr['wiek'], bins=[0, 30, 60, 90], labels=["0-30", "30-60", "60-90"], right=False
            )
            df_filtr = df_filtr.dropna(subset=['grupa_wiekowa'])
            logi += f">>> df_filtr po utworzeniu grup wiekowych df_filtr.shape: {df_filtr.shape}\n"
            logi += f"{df_filtr[['wiek', 'grupa_wiekowa']].head()}\n"
            print(logi)
        except Exception as e:
            logi += f"!!! Błąd przy tworzeniu grup wiekowych: {e}\n"
            print(logi)

        # --- Grupowanie po płci i grupie wiekowej ---
        try:
            grupa = df_filtr.groupby(['płeć', 'grupa_wiekowa'])
            statystyki = grupa[['ciśnienie_krwi', 'wiek', 'tętno']].agg(['mean', 'median']).reset_index()
            # Spłaszczamy MultiIndex kolumn
            statystyki.columns = ['_'.join(col).strip('_') if isinstance(col, tuple) else col for col in
                                  statystyki.columns]
            logi += f">>> Statystyki końcowe df.shape: {statystyki.shape}\n"
            logi += f"{statystyki.head()}\n"
            print(logi)
        except Exception as e:
            logi += f"!!! Błąd przy grupowaniu lub obliczaniu statystyk: {e}\n"
            print(logi)
            statystyki = pd.DataFrame()  # pusty DF w przypadku błędu

        # --- Wywołanie funkcji tworzącej tabelę ---
        self.pokaz_tabele_przefiltrowana(statystyki)

    def pokaz_tabele_przefiltrowana(self, df_filtr):
        print(">>> START funkcji pokaz_tabele_przefiltrowana")

        if df_filtr.empty:
            self.pole_logow.append("Brak danych do wyświetlenia")
            return

        # --- Usuń poprzednią tabelę ---
        if hasattr(self, 'tabela_przefiltrowana'):
            print(">>> Usuwanie starej tabeli")
            try:
                self.layout_tabela_przefiltrowana.removeWidget(self.tabela_przefiltrowana)
                self.tabela_przefiltrowana.deleteLater()
                del self.tabela_przefiltrowana
                print(">>> Stara tabela usunięta")
            except Exception as e:
                print("!!! Błąd przy usuwaniu starej tabeli:", e)

        # --- Utwórz nową tabelę ---
        try:
            print(">>> Tworzenie nowej tabeli")
            self.tabela_przefiltrowana = QTableWidget()
            self.tabela_przefiltrowana.setRowCount(len(df_filtr))
            self.tabela_przefiltrowana.setColumnCount(len(df_filtr.columns))
            self.tabela_przefiltrowana.setHorizontalHeaderLabels(df_filtr.columns.tolist())
            print(">>> Nowa tabela utworzona")
        except Exception as e:
            print("!!! Błąd przy tworzeniu tabeli:", e)

        # --- Wypełnij tabelę danymi ---
        try:
            print(">>> Wypełnianie tabeli danymi")
            for i, row in enumerate(df_filtr.itertuples(index=False)):
                for j, value in enumerate(row):
                    self.tabela_przefiltrowana.setItem(i, j, QTableWidgetItem(str(value)))
            print(">>> Dane w tabeli wypełnione")
        except Exception as e:
            print("!!! Błąd przy wypełnianiu tabeli:", e)

        # --- Dodaj tabelę do layoutu i pokaż ---
        try:
            print(">>> Dodawanie tabeli do layoutu")
            self.layout_tabela_przefiltrowana.addWidget(self.tabela_przefiltrowana)
            self.tabela_przefiltrowana.show()
            print(">>> Tabela powinna być teraz widoczna")
        except Exception as e:
            print("!!! Błąd przy dodawaniu tabeli do layoutu:", e)

        print(">>> KONIEC funkcji pokaz_tabele_przefiltrowana")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
