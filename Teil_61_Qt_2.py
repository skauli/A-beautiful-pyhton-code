from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from Teil_61_Qt.frm_main import Ui_frm_main

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mod_offene_leistungen = QtSql.QSqlRelationalTableModel()
        mod_offene_leistungen.setTable  ("Leistungen")
        mod_offene_leistungen.setRelation(1, QtSql.QSqlRelation("Kunden", "id", "Firma"))
        self.tbl_offene_leistungen.setItemDelegate(QtSql.QSqlRelationalDelegate())
        mod_offene_leistungen.select()
        self.tbl_offene_leistungen.setModel(mod_offene_leistungen)
        
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("Teil_61_Qt/Rechungen.sqlite")        

app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()