# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1389, 633)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrapeAllButton = QPushButton(self.centralwidget)
        self.scrapeAllButton.setObjectName(u"scrapeAllButton")
        self.scrapeAllButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.verticalLayout.addWidget(self.scrapeAllButton)

        self.BRButton = QPushButton(self.centralwidget)
        self.BRButton.setObjectName(u"BRButton")
        self.BRButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.verticalLayout.addWidget(self.BRButton)

        self.UDButton = QPushButton(self.centralwidget)
        self.UDButton.setObjectName(u"UDButton")
        self.UDButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.verticalLayout.addWidget(self.UDButton)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.verticalLayout.addWidget(self.settingsButton)

        self.ExportButton = QPushButton(self.centralwidget)
        self.ExportButton.setObjectName(u"ExportButton")
        self.ExportButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.verticalLayout.addWidget(self.ExportButton)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 4)
        self.verticalLayout.setStretch(6, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CurrentListingButton = QPushButton(self.centralwidget)
        self.CurrentListingButton.setObjectName(u"CurrentListingButton")
        self.CurrentListingButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.horizontalLayout.addWidget(self.CurrentListingButton)

        self.NewListingButton = QPushButton(self.centralwidget)
        self.NewListingButton.setObjectName(u"NewListingButton")
        self.NewListingButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.horizontalLayout.addWidget(self.NewListingButton)

        self.RemoveListingButton = QPushButton(self.centralwidget)
        self.RemoveListingButton.setObjectName(u"RemoveListingButton")
        self.RemoveListingButton.setStyleSheet(u"QPushButton {padding: 25px;\n"
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

        self.horizontalLayout.addWidget(self.RemoveListingButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 40)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(1, 70)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scraper", None))
        self.scrapeAllButton.setText(QCoreApplication.translate("MainWindow", u"Scrape v\u0161eho", None))
        self.BRButton.setText(QCoreApplication.translate("MainWindow", u"BezRealitky", None))
        self.UDButton.setText(QCoreApplication.translate("MainWindow", u"UlovDomov", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed", None))
        self.ExportButton.setText(QCoreApplication.translate("MainWindow", u"Exportuj excel\n"
" s nab\u00eddkami", None))
        self.CurrentListingButton.setText(QCoreApplication.translate("MainWindow", u"Aktu\u00e1ln\u00ed nab\u00eddky", None))
        self.NewListingButton.setText(QCoreApplication.translate("MainWindow", u"Nov\u00e9 nab\u00eddky", None))
        self.RemoveListingButton.setText(QCoreApplication.translate("MainWindow", u"Sta\u017een\u00e9 nab\u00eddky", None))
    # retranslateUi

