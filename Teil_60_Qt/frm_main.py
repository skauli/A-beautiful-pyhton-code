# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(1200, 800)
        self.actionQuit = QAction(frm_main)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionKunden_verwalten = QAction(frm_main)
        self.actionKunden_verwalten.setObjectName(u"actionKunden_verwalten")
        self.actionAuftraggeber_verwalten = QAction(frm_main)
        self.actionAuftraggeber_verwalten.setObjectName(u"actionAuftraggeber_verwalten")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_offene_leistungen = QLabel(self.centralwidget)
        self.lbl_offene_leistungen.setObjectName(u"lbl_offene_leistungen")
        self.lbl_offene_leistungen.setGeometry(QRect(10, 30, 1181, 20))
        font = QFont()
        font.setPointSize(16)
        self.lbl_offene_leistungen.setFont(font)
        self.lbl_offene_leistungen.setAlignment(Qt.AlignCenter)
        self.lbl_offene_rechnungen = QLabel(self.centralwidget)
        self.lbl_offene_rechnungen.setObjectName(u"lbl_offene_rechnungen")
        self.lbl_offene_rechnungen.setGeometry(QRect(10, 350, 1181, 20))
        self.lbl_offene_rechnungen.setFont(font)
        self.lbl_offene_rechnungen.setAlignment(Qt.AlignCenter)
        self.tbl_offene_leistungen = QTableView(self.centralwidget)
        self.tbl_offene_leistungen.setObjectName(u"tbl_offene_leistungen")
        self.tbl_offene_leistungen.setGeometry(QRect(10, 60, 1181, 241))
        self.tbl_offene_rechnungen = QTableView(self.centralwidget)
        self.tbl_offene_rechnungen.setObjectName(u"tbl_offene_rechnungen")
        self.tbl_offene_rechnungen.setGeometry(QRect(10, 380, 1181, 241))
        self.bt_leistungen_erfassen = QPushButton(self.centralwidget)
        self.bt_leistungen_erfassen.setObjectName(u"bt_leistungen_erfassen")
        self.bt_leistungen_erfassen.setGeometry(QRect(30, 650, 171, 41))
        self.bt_rechnung_erstellen = QPushButton(self.centralwidget)
        self.bt_rechnung_erstellen.setObjectName(u"bt_rechnung_erstellen")
        self.bt_rechnung_erstellen.setGeometry(QRect(500, 650, 171, 41))
        self.bt_zahlung_erfassen = QPushButton(self.centralwidget)
        self.bt_zahlung_erfassen.setObjectName(u"bt_zahlung_erfassen")
        self.bt_zahlung_erfassen.setGeometry(QRect(980, 650, 171, 41))
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuStammdaten = QMenu(self.menubar)
        self.menuStammdaten.setObjectName(u"menuStammdaten")
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        frm_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuStammdaten.menuAction())
        self.menuDatei.addAction(self.actionQuit)
        self.menuStammdaten.addAction(self.actionKunden_verwalten)
        self.menuStammdaten.addAction(self.actionAuftraggeber_verwalten)

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("frm_main", u"Quit", None))
        self.actionKunden_verwalten.setText(QCoreApplication.translate("frm_main", u"Kunden verwalten", None))
        self.actionAuftraggeber_verwalten.setText(QCoreApplication.translate("frm_main", u"Auftraggeber verwalten", None))
        self.lbl_offene_leistungen.setText(QCoreApplication.translate("frm_main", u"Offene Leistungen", None))
        self.lbl_offene_rechnungen.setText(QCoreApplication.translate("frm_main", u"Offene Rechnungen", None))
        self.bt_leistungen_erfassen.setText(QCoreApplication.translate("frm_main", u"Leistungen erfassen", None))
        self.bt_rechnung_erstellen.setText(QCoreApplication.translate("frm_main", u"Rechnung erstellen", None))
        self.bt_zahlung_erfassen.setText(QCoreApplication.translate("frm_main", u"Zahlung erfassen", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
        self.menuStammdaten.setTitle(QCoreApplication.translate("frm_main", u"Stammdaten", None))
    # retranslateUi

