from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from Teil_62_Qt.frm_main import Ui_frm_main
from Teil_62_Qt.frm_kundenauswahl import Ui_frm_kundenauswahl

class Frm_kundenauswahl(QMainWindow, Ui_frm_kundenauswahl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mod_offene_leistungen = QtSql.QSqlRelationalTableModel()
        self.mod_offene_leistungen.setTable  ("Leistungen")
        self.mod_offene_leistungen.setRelation(1, QtSql.QSqlRelation("Kunden", "id", "Firma"))
        self.tbl_offene_leistungen.setItemDelegate(QtSql.QSqlRelationalDelegate())
        self.bt_rechnung_erstellen.clicked.connect(self.rechnungen_erstellen)
        self.leistungen_anzeigen()
        
        
    def rechnungen_erstellen(self):
        frm_kundenauswahl.show()
    
    def leistungen_anzeigen(self):
        model = self.mod_offene_leistungen
        query = QtSql.QSqlQuery()
        abfrage = """update Leistungen set
                     Summe_brutto = Menge * Preis,
                     Summe_netto =  Menge * (Preis / (100.00 + MwSt) * 100)"""
        
        query.exec(abfrage)
        model.select()
        self.tbl_offene_leistungen.setModel(model)
        gesamt_brutto = sum([model.data(model.index(zeile,8)) for zeile in range(model.rowCount())])
        t = f'Offene Leistungen ({gesamt_brutto:0.2f} €)'
        self.lbl_offene_leistungen.setText(t)
        
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("Teil_62_Qt/Rechungen.sqlite")        

app = QApplication()
frm_main = Frm_main()
frm_main.show()
frm_kundenauswahl = Frm_kundenauswahl()
app.exec()

print("Änderung1")