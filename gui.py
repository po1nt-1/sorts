# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 450)
        MainWindow.setMinimumSize(QSize(250, 450))
        MainWindow.setMaximumSize(QSize(250, 450))
        MainWindow.setStyleSheet(u"background-color: rgb(41, 43, 47);\n"
"alternate-background-color: rgb(218, 0, 27);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(225, 150))
        self.frame.setMaximumSize(QSize(225, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(41, 43, 47);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.enter_size_list = QLineEdit(self.frame)
        self.enter_size_list.setObjectName(u"enter_size_list")
        self.enter_size_list.setFont(font)
        self.enter_size_list.setStyleSheet(u"selection-background-color: rgb(218, 0, 27);\n"
"background-color: rgb(32, 34, 37);\n"
"color: rgb(255, 255, 255);")
        self.enter_size_list.setInputMethodHints(Qt.ImhNone)
        self.enter_size_list.setMaxLength(7)
        self.enter_size_list.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.enter_size_list, 5, 0, 1, 1)

        self.gen_button = QPushButton(self.frame)
        self.gen_button.setObjectName(u"gen_button")
        self.gen_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 0, 27);")

        self.gridLayout_2.addWidget(self.gen_button, 7, 0, 1, 1)

        self.file_list = QListWidget(self.frame)
        self.file_list.setObjectName(u"file_list")
        self.file_list.setFont(font)
        self.file_list.setStyleSheet(u"background-color: rgb(32, 34, 37);\n"
"selection-background-color: rgb(218, 0, 27);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"alternate-background-color: rgb(214, 0, 26);\n"
"border-color: rgb(214, 0, 26);\n"
"border-top-color: rgb(214, 0, 26);\n"
"border-right-color: rgb(214, 0, 26);\n"
"border-bottom-color: rgb(214, 0, 26);\n"
"border-left-color: rgb(214, 0, 26);\n"
"gridline-color: rgb(214, 0, 26);\n"
"selection-color: rgb(214, 0, 26);")
        self.file_list.setViewMode(QListView.ListMode)

        self.gridLayout_2.addWidget(self.file_list, 10, 0, 1, 1)

        self.select_gen_mode = QComboBox(self.frame)
        self.select_gen_mode.addItem("")
        self.select_gen_mode.addItem("")
        self.select_gen_mode.addItem("")
        self.select_gen_mode.addItem("")
        self.select_gen_mode.addItem("")
        self.select_gen_mode.setObjectName(u"select_gen_mode")
        self.select_gen_mode.setStyleSheet(u"background-color: rgb(32, 34, 37);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.select_gen_mode, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.analyze_button = QPushButton(self.frame)
        self.analyze_button.setObjectName(u"analyze_button")
        self.analyze_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 0, 27);")

        self.horizontalLayout_3.addWidget(self.analyze_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 11, 0, 1, 1)

        self.update_button = QPushButton(self.frame)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(218, 0, 27);")

        self.gridLayout_2.addWidget(self.update_button, 9, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f", None))
        self.enter_size_list.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gen_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.select_gen_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u044e\u0449\u0430\u044f", None))
        self.select_gen_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0423\u0431\u044b\u0432\u0430\u044e\u0449\u0430\u044f", None))
        self.select_gen_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u0430", None))
        self.select_gen_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u0438\u0447\u043d\u043e-\u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u043d\u0430\u044f", None))
        self.select_gen_mode.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0421 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u043c\u0438 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c\u0438", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \n"
"\u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.analyze_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

