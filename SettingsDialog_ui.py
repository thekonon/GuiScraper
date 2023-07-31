# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(658, 427)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.UDUrlEdit = QLineEdit(Dialog)
        self.UDUrlEdit.setObjectName(u"UDUrlEdit")

        self.gridLayout.addWidget(self.UDUrlEdit, 1, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.BRUrlEdit = QLineEdit(Dialog)
        self.BRUrlEdit.setObjectName(u"BRUrlEdit")

        self.gridLayout.addWidget(self.BRUrlEdit, 0, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.BrowserSelectCombo = QComboBox(Dialog)
        self.BrowserSelectCombo.addItem("")
        self.BrowserSelectCombo.addItem("")
        self.BrowserSelectCombo.addItem("")
        self.BrowserSelectCombo.setObjectName(u"BrowserSelectCombo")

        self.gridLayout.addWidget(self.BrowserSelectCombo, 3, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
"background-color: #4CAF50;\n"
"border: 2px solid #008CBA;\n"
"border-radius: 25px;\n"
"color: white;\n"
"font-size: 16px;}\n"
"QPushButton:hover {\n"
"background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #ff0000;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.saveButton, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Prohl\u00ed\u017ee\u010d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"BezRealitkyURL", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"UlovDomovURL", None))
        self.BrowserSelectCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Firefox - silent", None))
        self.BrowserSelectCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Firefox - normal", None))
        self.BrowserSelectCombo.setItemText(2, QCoreApplication.translate("Dialog", u"Chrome", None))

        self.saveButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

