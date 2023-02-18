# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_kundenauswahl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_frm_kundenauswahl(object):
    def setupUi(self, frm_kundenauswahl):
        if not frm_kundenauswahl.objectName():
            frm_kundenauswahl.setObjectName(u"frm_kundenauswahl")
        frm_kundenauswahl.resize(548, 420)
        self.label = QLabel(frm_kundenauswahl)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 7, 371, 20))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.bt_ok = QPushButton(frm_kundenauswahl)
        self.bt_ok.setObjectName(u"bt_ok")
        self.bt_ok.setGeometry(QRect(10, 390, 75, 24))
        self.bt_abbruch = QPushButton(frm_kundenauswahl)
        self.bt_abbruch.setObjectName(u"bt_abbruch")
        self.bt_abbruch.setGeometry(QRect(470, 390, 75, 24))
        self.tbl_kunden = QTableView(frm_kundenauswahl)
        self.tbl_kunden.setObjectName(u"tbl_kunden")
        self.tbl_kunden.setGeometry(QRect(10, 40, 531, 261))

        self.retranslateUi(frm_kundenauswahl)

        QMetaObject.connectSlotsByName(frm_kundenauswahl)
    # setupUi

    def retranslateUi(self, frm_kundenauswahl):
        frm_kundenauswahl.setWindowTitle(QCoreApplication.translate("frm_kundenauswahl", u"Form", None))
        self.label.setText(QCoreApplication.translate("frm_kundenauswahl", u"Bitte Kunden ausw\u00e4hlen", None))
        self.bt_ok.setText(QCoreApplication.translate("frm_kundenauswahl", u"ok", None))
        self.bt_abbruch.setText(QCoreApplication.translate("frm_kundenauswahl", u"Abbruch", None))
    # retranslateUi

