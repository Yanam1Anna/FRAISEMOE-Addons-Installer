# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime,
                            QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QSplitter, QVBoxLayout, QWidget)
from pic_data import img_data
from PySide6.QtCore import QByteArray
import base64


class Ui_mainwin(object):

    def setupUi(self, mainwin):
        if not mainwin.objectName():
            mainwin.setObjectName(u"mainwin")
        mainwin.setWindowModality(Qt.WindowModality.NonModal)
        mainwin.resize(1280, 720)
        mainwin.setMinimumSize(QSize(1280, 720))
        mainwin.setMaximumSize(QSize(1280, 720))

        pixmap = QPixmap()

        icon = QIcon()
        pixmap.loadFromData(QByteArray(base64.b64decode(img_data['icon'])))
        icon.addPixmap(pixmap)

        mainwin.setWindowIcon(icon)

        self.mainbg = QLabel(mainwin)
        self.mainbg.setObjectName(u"mainbg")
        self.mainbg.setEnabled(True)
        self.mainbg.setGeometry(QRect(0, 0, 1280, 720))
        self.mainbg.setMinimumSize(QSize(1280, 720))
        self.mainbg.setMaximumSize(QSize(1280, 720))
        self.mainbg.setTextFormat(Qt.TextFormat.AutoText)

        pixmap.loadFromData(QByteArray(base64.b64decode(img_data['bg'])))

        self.mainbg.setPixmap(pixmap)
        self.mainbg.setScaledContents(False)
        self.mainbg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover = QSplitter(mainwin)
        self.cover.setObjectName(u"cover")
        self.cover.setGeometry(QRect(0, 320, 213, 400))
        self.cover.setOrientation(Qt.Orientation.Vertical)
        self.Cover_1 = QLabel(self.cover)
        self.Cover_1.setObjectName(u"Cover_1")
        self.Cover_1.setMinimumSize(QSize(213, 100))
        self.Cover_1.setMaximumSize(QSize(213, 100))
        self.Cover_1.setTextFormat(Qt.TextFormat.AutoText)

        pixmap.loadFromData(
            QByteArray(base64.b64decode(img_data['vol_1_cover'])))
        self.Cover_1.setPixmap(pixmap)

        self.Cover_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover.addWidget(self.Cover_1)
        self.Cover_2 = QLabel(self.cover)
        self.Cover_2.setObjectName(u"Cover_2")
        self.Cover_2.setMinimumSize(QSize(213, 100))
        self.Cover_2.setMaximumSize(QSize(213, 100))
        self.Cover_2.setTextFormat(Qt.TextFormat.AutoText)

        pixmap.loadFromData(
            QByteArray(base64.b64decode(img_data['vol_2_cover'])))
        self.Cover_2.setPixmap(pixmap)

        self.Cover_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover.addWidget(self.Cover_2)
        self.Cover_3 = QLabel(self.cover)
        self.Cover_3.setObjectName(u"Cover_3")
        self.Cover_3.setMinimumSize(QSize(213, 100))
        self.Cover_3.setMaximumSize(QSize(213, 100))
        self.Cover_3.setTextFormat(Qt.TextFormat.AutoText)

        pixmap.loadFromData(
            QByteArray(base64.b64decode(img_data['vol_3_cover'])))
        self.Cover_3.setPixmap(pixmap)

        self.Cover_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover.addWidget(self.Cover_3)
        self.Cover_4 = QLabel(self.cover)
        self.Cover_4.setObjectName(u"Cover_4")
        self.Cover_4.setMinimumSize(QSize(213, 100))
        self.Cover_4.setMaximumSize(QSize(213, 100))
        self.Cover_4.setTextFormat(Qt.TextFormat.AutoText)

        pixmap.loadFromData(
            QByteArray(base64.b64decode(img_data['vol_4_cover'])))
        self.Cover_4.setPixmap(pixmap)

        self.Cover_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover.addWidget(self.Cover_4)
        self.menubg = QLabel(mainwin)
        self.menubg.setObjectName(u"menubg")
        self.menubg.setGeometry(QRect(800, 0, 480, 720))
        self.menubg.setMinimumSize(QSize(480, 720))
        self.menubg.setMaximumSize(QSize(480, 720))

        pixmap.loadFromData(QByteArray(base64.b64decode(img_data['menubg'])))
        self.menubg.setPixmap(pixmap)

        self.menubg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(mainwin)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(940, 340, 212, 204))
        self.button = QVBoxLayout(self.layoutWidget)
        self.button.setObjectName(u"button")
        self.button.setContentsMargins(0, 0, 0, 0)
        self.startbtn = QPushButton(self.layoutWidget)
        self.startbtn.setObjectName(u"startbtn")
        self.startbtn.setMinimumSize(QSize(210, 98))
        self.startbtn.setMaximumSize(QSize(210, 98))

        icon1 = QIcon()
        pixmap.loadFromData(QByteArray(base64.b64decode(img_data['btn01bg'])))
        icon1.addPixmap(pixmap)

        self.startbtn.setIcon(icon1)
        self.startbtn.setIconSize(QSize(210, 98))
        self.startbtn.setFlat(True)

        self.button.addWidget(self.startbtn)

        self.exitbtn = QPushButton(self.layoutWidget)
        self.exitbtn.setObjectName(u"exitbtn")
        self.exitbtn.setMinimumSize(QSize(210, 98))
        self.exitbtn.setMaximumSize(QSize(210, 98))

        icon2 = QIcon()
        pixmap.loadFromData(QByteArray(base64.b64decode(img_data['btn02bg'])))
        icon2.addPixmap(pixmap)

        self.exitbtn.setIcon(icon2)
        self.exitbtn.setIconSize(QSize(210, 98))
        self.exitbtn.setFlat(True)

        self.button.addWidget(self.exitbtn)

        self.sup_info = QLabel(mainwin)
        self.sup_info.setObjectName(u"sup_info")
        self.sup_info.setGeometry(QRect(0, 230, 213, 100))
        self.sup_info.setMinimumSize(QSize(213, 100))
        self.sup_info.setMaximumSize(QSize(213, 100))

        pixmap.loadFromData(
            QByteArray(base64.b64decode(img_data['support_info'])))
        self.sup_info.setPixmap(pixmap)

        self.future_info = QLabel(mainwin)
        self.future_info.setObjectName(u"future_info")
        self.future_info.setGeometry(QRect(860, 700, 370, 16))
        self.future_info.setMinimumSize(QSize(370, 16))
        self.future_info.setMaximumSize(QSize(370, 16))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setBold(True)
        font.setItalic(True)
        self.future_info.setFont(font)
        self.future_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainbg.raise_()
        self.cover.raise_()
        self.menubg.raise_()
        self.layoutWidget.raise_()
        self.future_info.raise_()
        self.sup_info.raise_()

        self.retranslateUi(mainwin)

        QMetaObject.connectSlotsByName(mainwin)

    # setupUi

    def retranslateUi(self, mainwin):
        mainwin.setWindowTitle(
            QCoreApplication.translate(
                "mainwin", u"FRAISEMOE Addons Installer V4.2.0.25600", None))
        self.mainbg.setText("")
        self.Cover_1.setText("")
        self.Cover_2.setText("")
        self.Cover_3.setText("")
        self.Cover_4.setText("")
        self.menubg.setText("")
        self.startbtn.setText("")
        self.exitbtn.setText("")
        self.sup_info.setText("")
        self.future_info.setText(
            QCoreApplication.translate(
                "mainwin",
                u"Nekopara After La Vraie Famille COMMING SOON IN 2025", None))

    # retranslateUi
