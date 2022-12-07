# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'capture_cicle_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1383, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setGeometry(QRect(10, 10, 1361, 841))
        self.content_frame.setStyleSheet(u"background-color: rgb(255, 255, 225);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../../pys6-recipes-organizer/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../../pys6-recipes-organizer/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../../pys6-recipes-organizer/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 21, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout.addWidget(self.top_bar_frame)

        self.frame_3 = QFrame(self.content_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"background-color: #1e3d59;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_edit_button = QPushButton(self.frame_6)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setMinimumSize(QSize(150, 0))
        self.add_edit_button.setFont(font)
        self.add_edit_button.setStyleSheet(u"QPushButton { \n"
"background-color : #ff6e40;\n"
"color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon4 = QIcon()
        icon4.addFile(u"../../pys6-recipes-organizer/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edit_button.setIcon(icon4)
        self.add_edit_button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.add_edit_button)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 250))
        self.frame_2.setStyleSheet(u"\n"
"border: 0px solid black;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))
        self.label_5.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 0))
        self.label_6.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(250, 0))
        self.frame_8.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(150, 16777215))
        self.label_10.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_5.setStyleSheet(u"border-color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(50, 16777215))
        self.label_13.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_13, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_4.setStyleSheet(u"border-color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 5)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 16777215))
        self.label_14.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))
        self.label_9.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(50, 16777215))
        self.label_11.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_11, 3, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.lineEdit_8 = QLineEdit(self.frame_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(20, 100, 221, 30))
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setMaximumSize(QSize(250, 16777215))
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 231, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lineEdit_7 = QLineEdit(self.frame_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(107, 170, 91, 30))
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setMaximumSize(QSize(250, 16777215))
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 175, 91, 21))
        self.label_15.setMaximumSize(QSize(150, 16777215))
        self.label_15.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(210, 180, 16, 20))
        self.label_17.setMaximumSize(QSize(50, 16777215))
        self.label_17.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(260, 200, 6, 20))
        self.label_16.setMaximumSize(QSize(50, 16777215))
        self.label_16.setStyleSheet(u"border: 0px solid black;")

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: 0px solid black;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(800, 0))
        self.frame_11.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.graphicsView = QGraphicsView(self.frame_11)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_5.addWidget(self.graphicsView)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(250, 100))
        self.frame_10.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_12)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 0))
        self.label_22.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.comboBox = QComboBox(self.frame_12)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.view_button_3 = QPushButton(self.frame_12)
        self.view_button_3.setObjectName(u"view_button_3")
        self.view_button_3.setMinimumSize(QSize(150, 30))
        self.view_button_3.setFont(font)
        self.view_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color : #17A2B8;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.view_button_3.setIconSize(QSize(20, 20))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.view_button_3)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_13)
        self.formLayout.setObjectName(u"formLayout")
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_10 = QLineEdit(self.frame_13)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(50, 0))
        self.label_18.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_9 = QLineEdit(self.frame_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_9)

        self.lineEdit_12 = QLineEdit(self.frame_13)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_21)

        self.lineEdit_11 = QLineEdit(self.frame_13)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(50, 0))
        self.label_20.setStyleSheet(u"border: 0px solid black;\n"
"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_20)


        self.verticalLayout_4.addWidget(self.frame_13)


        self.horizontalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.view_button_4 = QPushButton(self.frame_14)
        self.view_button_4.setObjectName(u"view_button_4")
        self.view_button_4.setMinimumSize(QSize(150, 30))
        self.view_button_4.setFont(font)
        self.view_button_4.setStyleSheet(u"QPushButton{\n"
"	background-color : #17A2B8;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.view_button_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.view_button_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.view_button_2 = QPushButton(self.frame_14)
        self.view_button_2.setObjectName(u"view_button_2")
        self.view_button_2.setMinimumSize(QSize(150, 30))
        self.view_button_2.setFont(font)
        self.view_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color : #17A2B8;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.view_button_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.view_button_2)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.view_button = QPushButton(self.frame_14)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setMinimumSize(QSize(150, 30))
        self.view_button.setFont(font)
        self.view_button.setStyleSheet(u"QPushButton{\n"
"	background-color : #17A2B8;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.view_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.view_button)


        self.verticalLayout_3.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)

        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Sterilization System", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pre Head", None))
        self.add_edit_button.setText(QCoreApplication.translate("MainWindow", u"Recetas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Press:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"KPA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chamber Conditions", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Temp Setpoint:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"F.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Phase Especifications", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Jacket Offset:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Jacket S.P:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"F.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"F.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Phase Especifications", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Jacket Temp:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"F.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Cicle", None))
        self.view_button_3.setText(QCoreApplication.translate("MainWindow", u"Select Cicle", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Estimated remaining:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Estimated in Required Weight :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tank Lot :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tare Weight :", None))
        self.view_button_4.setText(QCoreApplication.translate("MainWindow", u"Cylce Information", None))
        self.view_button_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"Data Capture", None))
    # retranslateUi

