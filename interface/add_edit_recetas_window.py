# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_recetas_window.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTimeEdit, QToolButton, QVBoxLayout,
    QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 861)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setGeometry(QRect(10, 10, 1041, 841))
        self.content_frame.setStyleSheet(u"background-color: rgb(245, 240, 225);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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


        self.verticalLayout_4.addWidget(self.top_bar_frame)

        self.horizontalSpacer_119 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_119)

        self.scrollArea = QScrollArea(self.content_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -2836, 1004, 6018))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QSize(0, 6000))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(90, 60, 451, 61))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label)

        self.nombre_line_edit = QLineEdit(self.frame_4)
        self.nombre_line_edit.setObjectName(u"nombre_line_edit")
        self.nombre_line_edit.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout.addWidget(self.nombre_line_edit)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(90, 120, 451, 51))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.nombre_line_edit_2 = QLineEdit(self.frame_5)
        self.nombre_line_edit_2.setObjectName(u"nombre_line_edit_2")
        self.nombre_line_edit_2.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_5.addWidget(self.nombre_line_edit_2)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(90, 170, 451, 51))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.nombre_line_edit_3 = QLineEdit(self.frame_6)
        self.nombre_line_edit_3.setObjectName(u"nombre_line_edit_3")
        self.nombre_line_edit_3.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_6.addWidget(self.nombre_line_edit_3)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(70, 220, 451, 51))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.nombre_line_edit_4 = QLineEdit(self.frame_7)
        self.nombre_line_edit_4.setObjectName(u"nombre_line_edit_4")
        self.nombre_line_edit_4.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_7.addWidget(self.nombre_line_edit_4)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(70, 270, 451, 51))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.nombre_line_edit_5 = QLineEdit(self.frame_8)
        self.nombre_line_edit_5.setObjectName(u"nombre_line_edit_5")
        self.nombre_line_edit_5.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_5.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_8.addWidget(self.nombre_line_edit_5)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(70, 320, 451, 51))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.nombre_line_edit_6 = QLineEdit(self.frame_9)
        self.nombre_line_edit_6.setObjectName(u"nombre_line_edit_6")
        self.nombre_line_edit_6.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_6.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_9.addWidget(self.nombre_line_edit_6)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.label_18)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(70, 360, 451, 51))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.label_20)

        self.nombre_line_edit_7 = QLineEdit(self.frame_10)
        self.nombre_line_edit_7.setObjectName(u"nombre_line_edit_7")
        self.nombre_line_edit_7.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_7.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_10.addWidget(self.nombre_line_edit_7)

        self.label_21 = QLabel(self.frame_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(70, 410, 451, 51))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_22 = QLabel(self.frame_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.nombre_line_edit_8 = QLineEdit(self.frame_11)
        self.nombre_line_edit_8.setObjectName(u"nombre_line_edit_8")
        self.nombre_line_edit_8.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_8.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_11.addWidget(self.nombre_line_edit_8)

        self.label_24 = QLabel(self.frame_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.label_24)

        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 480, 201, 31))
        self.label_26.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(60, 520, 451, 51))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_12.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_12.addWidget(self.label_28)

        self.nombre_line_edit_9 = QLineEdit(self.frame_12)
        self.nombre_line_edit_9.setObjectName(u"nombre_line_edit_9")
        self.nombre_line_edit_9.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_9.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_12.addWidget(self.nombre_line_edit_9)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_12.addWidget(self.label_29)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(60, 570, 451, 51))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_13.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_13.addWidget(self.label_31)

        self.nombre_line_edit_10 = QLineEdit(self.frame_13)
        self.nombre_line_edit_10.setObjectName(u"nombre_line_edit_10")
        self.nombre_line_edit_10.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_10.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_13.addWidget(self.nombre_line_edit_10)

        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_13.addWidget(self.label_32)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(60, 620, 451, 51))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_33 = QLabel(self.frame_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_14)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.label_34)

        self.nombre_line_edit_11 = QLineEdit(self.frame_14)
        self.nombre_line_edit_11.setObjectName(u"nombre_line_edit_11")
        self.nombre_line_edit_11.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_11.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_14.addWidget(self.nombre_line_edit_11)

        self.label_35 = QLabel(self.frame_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 680, 201, 31))
        self.label_36.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(60, 720, 451, 51))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.label_38)

        self.nombre_line_edit_12 = QLineEdit(self.frame_15)
        self.nombre_line_edit_12.setObjectName(u"nombre_line_edit_12")
        self.nombre_line_edit_12.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_12.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_15.addWidget(self.nombre_line_edit_12)

        self.label_39 = QLabel(self.frame_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.label_39)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(60, 770, 451, 51))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_40 = QLabel(self.frame_16)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_16)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.label_41)

        self.nombre_line_edit_13 = QLineEdit(self.frame_16)
        self.nombre_line_edit_13.setObjectName(u"nombre_line_edit_13")
        self.nombre_line_edit_13.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_13.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_16.addWidget(self.nombre_line_edit_13)

        self.label_42 = QLabel(self.frame_16)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.label_42)

        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(60, 820, 451, 51))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_43 = QLabel(self.frame_17)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_17)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_44)

        self.nombre_line_edit_14 = QLineEdit(self.frame_17)
        self.nombre_line_edit_14.setObjectName(u"nombre_line_edit_14")
        self.nombre_line_edit_14.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_14.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_17.addWidget(self.nombre_line_edit_14)

        self.label_45 = QLabel(self.frame_17)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_45)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(60, 870, 451, 51))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_46 = QLabel(self.frame_18)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_18.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_18)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_18.addWidget(self.label_47)

        self.nombre_line_edit_15 = QLineEdit(self.frame_18)
        self.nombre_line_edit_15.setObjectName(u"nombre_line_edit_15")
        self.nombre_line_edit_15.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_15.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_18.addWidget(self.nombre_line_edit_15)

        self.label_48 = QLabel(self.frame_18)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_18.addWidget(self.label_48)

        self.frame_19 = QFrame(self.frame_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(60, 920, 451, 51))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_49 = QLabel(self.frame_19)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.label_49)

        self.label_50 = QLabel(self.frame_19)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.label_50)

        self.nombre_line_edit_16 = QLineEdit(self.frame_19)
        self.nombre_line_edit_16.setObjectName(u"nombre_line_edit_16")
        self.nombre_line_edit_16.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_16.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_19.addWidget(self.nombre_line_edit_16)

        self.label_51 = QLabel(self.frame_19)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.label_51)

        self.frame_20 = QFrame(self.frame_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(60, 970, 451, 51))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.label_52)

        self.label_53 = QLabel(self.frame_20)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.label_53)

        self.nombre_line_edit_17 = QLineEdit(self.frame_20)
        self.nombre_line_edit_17.setObjectName(u"nombre_line_edit_17")
        self.nombre_line_edit_17.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_17.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_20.addWidget(self.nombre_line_edit_17)

        self.label_54 = QLabel(self.frame_20)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.label_54)

        self.frame_21 = QFrame(self.frame_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(60, 1020, 451, 51))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_55 = QLabel(self.frame_21)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.label_55)

        self.label_56 = QLabel(self.frame_21)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.label_56)

        self.nombre_line_edit_18 = QLineEdit(self.frame_21)
        self.nombre_line_edit_18.setObjectName(u"nombre_line_edit_18")
        self.nombre_line_edit_18.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_18.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_21.addWidget(self.nombre_line_edit_18)

        self.label_57 = QLabel(self.frame_21)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.label_57)

        self.frame_22 = QFrame(self.frame_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(60, 1070, 451, 51))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_58 = QLabel(self.frame_22)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_58)

        self.label_59 = QLabel(self.frame_22)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_59)

        self.nombre_line_edit_19 = QLineEdit(self.frame_22)
        self.nombre_line_edit_19.setObjectName(u"nombre_line_edit_19")
        self.nombre_line_edit_19.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_19.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_22.addWidget(self.nombre_line_edit_19)

        self.label_60 = QLabel(self.frame_22)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_60)

        self.frame_23 = QFrame(self.frame_3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(60, 1110, 451, 51))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_61 = QLabel(self.frame_23)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_23)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.label_62)

        self.nombre_line_edit_20 = QLineEdit(self.frame_23)
        self.nombre_line_edit_20.setObjectName(u"nombre_line_edit_20")
        self.nombre_line_edit_20.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_20.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_23.addWidget(self.nombre_line_edit_20)

        self.label_63 = QLabel(self.frame_23)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.label_63)

        self.frame_24 = QFrame(self.frame_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(70, 1150, 451, 51))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_64 = QLabel(self.frame_24)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_24)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.label_65)

        self.nombre_line_edit_21 = QLineEdit(self.frame_24)
        self.nombre_line_edit_21.setObjectName(u"nombre_line_edit_21")
        self.nombre_line_edit_21.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_21.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_24.addWidget(self.nombre_line_edit_21)

        self.label_66 = QLabel(self.frame_24)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.label_66)

        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(60, 1200, 451, 51))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_67 = QLabel(self.frame_25)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.label_67)

        self.label_68 = QLabel(self.frame_25)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.label_68)

        self.nombre_line_edit_22 = QLineEdit(self.frame_25)
        self.nombre_line_edit_22.setObjectName(u"nombre_line_edit_22")
        self.nombre_line_edit_22.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_22.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_25.addWidget(self.nombre_line_edit_22)

        self.label_69 = QLabel(self.frame_25)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.label_69)

        self.frame_26 = QFrame(self.frame_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(70, 1240, 451, 51))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_70 = QLabel(self.frame_26)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.label_70)

        self.label_71 = QLabel(self.frame_26)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.label_71)

        self.nombre_line_edit_23 = QLineEdit(self.frame_26)
        self.nombre_line_edit_23.setObjectName(u"nombre_line_edit_23")
        self.nombre_line_edit_23.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_23.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_26.addWidget(self.nombre_line_edit_23)

        self.label_72 = QLabel(self.frame_26)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.label_72)

        self.frame_27 = QFrame(self.frame_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(60, 1290, 451, 51))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_73 = QLabel(self.frame_27)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_27)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_74)

        self.nombre_line_edit_24 = QLineEdit(self.frame_27)
        self.nombre_line_edit_24.setObjectName(u"nombre_line_edit_24")
        self.nombre_line_edit_24.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_24.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_27.addWidget(self.nombre_line_edit_24)

        self.label_75 = QLabel(self.frame_27)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(320, 1360, 201, 31))
        self.label_76.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";")
        self.label_76.setAlignment(Qt.AlignCenter)
        self.frame_28 = QFrame(self.frame_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(60, 1400, 451, 51))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_77 = QLabel(self.frame_28)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_77)

        self.label_78 = QLabel(self.frame_28)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_78)

        self.nombre_line_edit_25 = QLineEdit(self.frame_28)
        self.nombre_line_edit_25.setObjectName(u"nombre_line_edit_25")
        self.nombre_line_edit_25.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_25.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_28.addWidget(self.nombre_line_edit_25)

        self.label_79 = QLabel(self.frame_28)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_79)

        self.frame_29 = QFrame(self.frame_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(60, 1450, 451, 51))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_80 = QLabel(self.frame_29)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_29)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_81)

        self.nombre_line_edit_26 = QLineEdit(self.frame_29)
        self.nombre_line_edit_26.setObjectName(u"nombre_line_edit_26")
        self.nombre_line_edit_26.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_26.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_29.addWidget(self.nombre_line_edit_26)

        self.label_82 = QLabel(self.frame_29)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_82)

        self.frame_30 = QFrame(self.frame_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(60, 1500, 451, 51))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_83 = QLabel(self.frame_30)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_83)

        self.label_84 = QLabel(self.frame_30)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_84)

        self.nombre_line_edit_27 = QLineEdit(self.frame_30)
        self.nombre_line_edit_27.setObjectName(u"nombre_line_edit_27")
        self.nombre_line_edit_27.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_27.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_30.addWidget(self.nombre_line_edit_27)

        self.label_85 = QLabel(self.frame_30)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_85)

        self.frame_31 = QFrame(self.frame_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(60, 1540, 451, 51))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_86 = QLabel(self.frame_31)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_31)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.label_87)

        self.nombre_line_edit_28 = QLineEdit(self.frame_31)
        self.nombre_line_edit_28.setObjectName(u"nombre_line_edit_28")
        self.nombre_line_edit_28.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_28.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_31.addWidget(self.nombre_line_edit_28)

        self.label_88 = QLabel(self.frame_31)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.label_88)

        self.frame_32 = QFrame(self.frame_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(60, 1590, 451, 51))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_89 = QLabel(self.frame_32)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_89)

        self.label_90 = QLabel(self.frame_32)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_90)

        self.nombre_line_edit_29 = QLineEdit(self.frame_32)
        self.nombre_line_edit_29.setObjectName(u"nombre_line_edit_29")
        self.nombre_line_edit_29.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_29.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_32.addWidget(self.nombre_line_edit_29)

        self.label_91 = QLabel(self.frame_32)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_91)

        self.frame_33 = QFrame(self.frame_3)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(60, 1640, 451, 51))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_92 = QLabel(self.frame_33)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_33.addWidget(self.label_92)

        self.label_93 = QLabel(self.frame_33)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_33.addWidget(self.label_93)

        self.nombre_line_edit_30 = QLineEdit(self.frame_33)
        self.nombre_line_edit_30.setObjectName(u"nombre_line_edit_30")
        self.nombre_line_edit_30.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_30.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_33.addWidget(self.nombre_line_edit_30)

        self.label_94 = QLabel(self.frame_33)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_33.addWidget(self.label_94)

        self.frame_34 = QFrame(self.frame_3)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setEnabled(True)
        self.frame_34.setGeometry(QRect(0, 0, 981, 5991))
        self.frame_34.setMinimumSize(QSize(0, 2200))
        self.frame_34.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_34)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_243 = QLabel(self.frame_34)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setMinimumSize(QSize(0, 40))
        self.label_243.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_243.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_243)

        self.frame_80 = QFrame(self.frame_34)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_237 = QLabel(self.frame_80)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_79.addWidget(self.label_237)

        self.label_238 = QLabel(self.frame_80)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_79.addWidget(self.label_238)

        self.horizontalSpacer_28 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_28)

        self.nombre_line_edit_43 = QLineEdit(self.frame_80)
        self.nombre_line_edit_43.setObjectName(u"nombre_line_edit_43")
        self.nombre_line_edit_43.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_43.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_43.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_79.addWidget(self.nombre_line_edit_43)

        self.label_239 = QLabel(self.frame_80)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_79.addWidget(self.label_239)


        self.verticalLayout_6.addWidget(self.frame_80)

        self.frame_84 = QFrame(self.frame_34)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_250 = QLabel(self.frame_84)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_83.addWidget(self.label_250)

        self.label_251 = QLabel(self.frame_84)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_83.addWidget(self.label_251)

        self.horizontalSpacer_102 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_102)

        self.spinBox = QSpinBox(self.frame_84)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(150, 30))
        self.spinBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"\n"
"")

        self.horizontalLayout_83.addWidget(self.spinBox)

        self.label_252 = QLabel(self.frame_84)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_83.addWidget(self.label_252)


        self.verticalLayout_6.addWidget(self.frame_84)

        self.frame_81 = QFrame(self.frame_34)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_240 = QLabel(self.frame_81)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_80.addWidget(self.label_240)

        self.label_241 = QLabel(self.frame_81)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_80.addWidget(self.label_241)

        self.horizontalSpacer_47 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_47)

        self.spinBox_2 = QSpinBox(self.frame_81)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(150, 30))
        self.spinBox_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_80.addWidget(self.spinBox_2)

        self.label_242 = QLabel(self.frame_81)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_80.addWidget(self.label_242)


        self.verticalLayout_6.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.frame_34)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_244 = QLabel(self.frame_82)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_81.addWidget(self.label_244)

        self.label_245 = QLabel(self.frame_82)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_81.addWidget(self.label_245)

        self.horizontalSpacer_82 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_82)

        self.spinBox_3 = QSpinBox(self.frame_82)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(150, 30))
        self.spinBox_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_81.addWidget(self.spinBox_3)

        self.label_246 = QLabel(self.frame_82)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_81.addWidget(self.label_246)


        self.verticalLayout_6.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_34)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_247 = QLabel(self.frame_83)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_82.addWidget(self.label_247)

        self.label_248 = QLabel(self.frame_83)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_82.addWidget(self.label_248)

        self.horizontalSpacer_100 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_100)

        self.spinBox_4 = QSpinBox(self.frame_83)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(150, 30))
        self.spinBox_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_82.addWidget(self.spinBox_4)

        self.label_249 = QLabel(self.frame_83)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_82.addWidget(self.label_249)


        self.verticalLayout_6.addWidget(self.frame_83)

        self.frame_85 = QFrame(self.frame_34)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_253 = QLabel(self.frame_85)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_84.addWidget(self.label_253)

        self.label_254 = QLabel(self.frame_85)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_84.addWidget(self.label_254)

        self.horizontalSpacer_107 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_107)

        self.spinBox_5 = QSpinBox(self.frame_85)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimumSize(QSize(150, 30))
        self.spinBox_5.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_84.addWidget(self.spinBox_5)

        self.label_255 = QLabel(self.frame_85)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_84.addWidget(self.label_255)


        self.verticalLayout_6.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_34)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_256 = QLabel(self.frame_86)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_85.addWidget(self.label_256)

        self.label_257 = QLabel(self.frame_86)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_85.addWidget(self.label_257)

        self.horizontalSpacer_108 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_108)

        self.spinBox_6 = QSpinBox(self.frame_86)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMinimumSize(QSize(150, 30))
        self.spinBox_6.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_85.addWidget(self.spinBox_6)

        self.label_258 = QLabel(self.frame_86)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_85.addWidget(self.label_258)


        self.verticalLayout_6.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_34)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_259 = QLabel(self.frame_87)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_86.addWidget(self.label_259)

        self.label_260 = QLabel(self.frame_87)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_86.addWidget(self.label_260)

        self.horizontalSpacer_109 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_109)

        self.spinBox_7 = QSpinBox(self.frame_87)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMinimumSize(QSize(150, 30))
        self.spinBox_7.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_86.addWidget(self.spinBox_7)

        self.label_261 = QLabel(self.frame_87)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_86.addWidget(self.label_261)


        self.verticalLayout_6.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.frame_34)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_262 = QLabel(self.frame_88)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_87.addWidget(self.label_262)

        self.label_263 = QLabel(self.frame_88)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_87.addWidget(self.label_263)

        self.horizontalSpacer_110 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_87.addItem(self.horizontalSpacer_110)

        self.spinBox_8 = QSpinBox(self.frame_88)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimumSize(QSize(150, 30))
        self.spinBox_8.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_87.addWidget(self.spinBox_8)

        self.label_264 = QLabel(self.frame_88)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_87.addWidget(self.label_264)


        self.verticalLayout_6.addWidget(self.frame_88)

        self.label_119 = QLabel(self.frame_34)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 40))
        self.label_119.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_119)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_95 = QLabel(self.frame_35)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_95)

        self.label_96 = QLabel(self.frame_35)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_96)

        self.horizontalSpacer_5 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_35)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.doubleSpinBox)

        self.label_97 = QLabel(self.frame_35)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_97)


        self.verticalLayout_6.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_98 = QLabel(self.frame_36)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.label_98)

        self.label_99 = QLabel(self.frame_36)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.label_99)

        self.horizontalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_36)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.doubleSpinBox_2)

        self.label_100 = QLabel(self.frame_36)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.label_100)


        self.verticalLayout_6.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_101 = QLabel(self.frame_37)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.label_101)

        self.label_102 = QLabel(self.frame_37)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.label_102)

        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_7)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_37)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.doubleSpinBox_3)

        self.label_103 = QLabel(self.frame_37)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.label_103)


        self.verticalLayout_6.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_104 = QLabel(self.frame_38)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.label_104)

        self.label_105 = QLabel(self.frame_38)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.label_105)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_8)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_38)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.doubleSpinBox_4)

        self.label_106 = QLabel(self.frame_38)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.label_106)


        self.verticalLayout_6.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_34)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_107 = QLabel(self.frame_39)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.label_107)

        self.label_108 = QLabel(self.frame_39)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.label_108)

        self.horizontalSpacer_9 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_9)

        self.timeEdit = QTimeEdit(self.frame_39)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(150, 30))
        self.timeEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.timeEdit)

        self.label_109 = QLabel(self.frame_39)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.label_109)


        self.verticalLayout_6.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_34)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_110 = QLabel(self.frame_40)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.label_110)

        self.label_111 = QLabel(self.frame_40)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.label_111)

        self.horizontalSpacer_10 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_10)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_40)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_5.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.doubleSpinBox_5)

        self.label_112 = QLabel(self.frame_40)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.label_112)


        self.verticalLayout_6.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_34)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_113 = QLabel(self.frame_41)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.label_113)

        self.label_114 = QLabel(self.frame_41)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.label_114)

        self.horizontalSpacer_11 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_11)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_41)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_6.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.doubleSpinBox_6)

        self.label_115 = QLabel(self.frame_41)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.label_115)


        self.verticalLayout_6.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_34)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_116 = QLabel(self.frame_42)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.label_116)

        self.label_117 = QLabel(self.frame_42)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.label_117)

        self.horizontalSpacer_12 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_12)

        self.timeEdit_2 = QTimeEdit(self.frame_42)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMinimumSize(QSize(150, 30))
        self.timeEdit_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.timeEdit_2)

        self.label_118 = QLabel(self.frame_42)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.label_118)


        self.verticalLayout_6.addWidget(self.frame_42)

        self.label_120 = QLabel(self.frame_34)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 40))
        self.label_120.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_120.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_120)

        self.frame_43 = QFrame(self.frame_34)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_121 = QLabel(self.frame_43)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.label_121)

        self.label_122 = QLabel(self.frame_43)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.label_122)

        self.horizontalSpacer_13 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_13)

        self.timeEdit_22 = QTimeEdit(self.frame_43)
        self.timeEdit_22.setObjectName(u"timeEdit_22")
        self.timeEdit_22.setMinimumSize(QSize(150, 30))
        self.timeEdit_22.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.timeEdit_22)

        self.label_123 = QLabel(self.frame_43)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.label_123)


        self.verticalLayout_6.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_34)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_124 = QLabel(self.frame_44)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.label_124)

        self.label_125 = QLabel(self.frame_44)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.label_125)

        self.horizontalSpacer_15 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_15)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.frame_44)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_7.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.doubleSpinBox_7)

        self.label_126 = QLabel(self.frame_44)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.label_126)


        self.verticalLayout_6.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_34)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_127 = QLabel(self.frame_45)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.label_127)

        self.label_128 = QLabel(self.frame_45)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.label_128)

        self.horizontalSpacer_14 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_14)

        self.timeEdit_3 = QTimeEdit(self.frame_45)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setMinimumSize(QSize(150, 30))
        self.timeEdit_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.timeEdit_3)

        self.label_129 = QLabel(self.frame_45)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.label_129)


        self.verticalLayout_6.addWidget(self.frame_45)

        self.label_130 = QLabel(self.frame_34)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(0, 40))
        self.label_130.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_130)

        self.frame_46 = QFrame(self.frame_34)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_131 = QLabel(self.frame_46)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.label_131)

        self.label_132 = QLabel(self.frame_46)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.label_132)

        self.horizontalSpacer_16 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_16)

        self.nombre_line_edit_42 = QLineEdit(self.frame_46)
        self.nombre_line_edit_42.setObjectName(u"nombre_line_edit_42")
        self.nombre_line_edit_42.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_42.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_42.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.nombre_line_edit_42)

        self.label_133 = QLabel(self.frame_46)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.label_133)


        self.verticalLayout_6.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_34)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_134 = QLabel(self.frame_47)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.label_134)

        self.label_135 = QLabel(self.frame_47)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.label_135)

        self.horizontalSpacer_17 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_17)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.frame_47)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_8.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.doubleSpinBox_8)

        self.label_136 = QLabel(self.frame_47)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.label_136)


        self.verticalLayout_6.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_34)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_137 = QLabel(self.frame_48)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.label_137)

        self.label_138 = QLabel(self.frame_48)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.label_138)

        self.horizontalSpacer_18 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_18)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.frame_48)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_9.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.doubleSpinBox_9)

        self.label_139 = QLabel(self.frame_48)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.label_139)


        self.verticalLayout_6.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_34)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_140 = QLabel(self.frame_49)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_140)

        self.label_141 = QLabel(self.frame_49)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_141)

        self.horizontalSpacer_20 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_20)

        self.timeEdit_4 = QTimeEdit(self.frame_49)
        self.timeEdit_4.setObjectName(u"timeEdit_4")
        self.timeEdit_4.setMinimumSize(QSize(150, 30))
        self.timeEdit_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.timeEdit_4)

        self.label_142 = QLabel(self.frame_49)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_142)


        self.verticalLayout_6.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_34)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_143 = QLabel(self.frame_50)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.label_143)

        self.label_144 = QLabel(self.frame_50)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.label_144)

        self.horizontalSpacer_19 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_19)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.frame_50)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_11.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.doubleSpinBox_11)

        self.label_145 = QLabel(self.frame_50)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.label_145)


        self.verticalLayout_6.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_34)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_146 = QLabel(self.frame_51)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.label_146)

        self.label_147 = QLabel(self.frame_51)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.label_147)

        self.horizontalSpacer_21 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_21)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.frame_51)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_10.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.doubleSpinBox_10)

        self.label_148 = QLabel(self.frame_51)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.label_148)


        self.verticalLayout_6.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_34)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_149 = QLabel(self.frame_52)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.label_149)

        self.label_150 = QLabel(self.frame_52)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.label_150)

        self.horizontalSpacer_22 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_22)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.frame_52)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_12.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.doubleSpinBox_12)

        self.label_151 = QLabel(self.frame_52)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.label_151)


        self.verticalLayout_6.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_34)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_152 = QLabel(self.frame_53)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.label_152)

        self.label_153 = QLabel(self.frame_53)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.label_153)

        self.horizontalSpacer_23 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_23)

        self.timeEdit_5 = QTimeEdit(self.frame_53)
        self.timeEdit_5.setObjectName(u"timeEdit_5")
        self.timeEdit_5.setMinimumSize(QSize(150, 30))
        self.timeEdit_5.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.timeEdit_5)

        self.label_154 = QLabel(self.frame_53)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.label_154)


        self.verticalLayout_6.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_34)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_155 = QLabel(self.frame_54)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.label_155)

        self.label_156 = QLabel(self.frame_54)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.label_156)

        self.horizontalSpacer_24 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_24)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.frame_54)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")
        self.doubleSpinBox_13.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_13.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.doubleSpinBox_13)

        self.label_157 = QLabel(self.frame_54)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.label_157)


        self.verticalLayout_6.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_34)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_158 = QLabel(self.frame_55)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_158)

        self.label_159 = QLabel(self.frame_55)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_159)

        self.horizontalSpacer_26 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_26)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.frame_55)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_14.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.doubleSpinBox_14)

        self.label_160 = QLabel(self.frame_55)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_160)


        self.verticalLayout_6.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_34)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_161 = QLabel(self.frame_56)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.label_161)

        self.label_162 = QLabel(self.frame_56)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.label_162)

        self.horizontalSpacer_25 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_25)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.frame_56)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")
        self.doubleSpinBox_16.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_16.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.doubleSpinBox_16)

        self.label_163 = QLabel(self.frame_56)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.label_163)


        self.verticalLayout_6.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_34)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_164 = QLabel(self.frame_57)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.label_164)

        self.label_165 = QLabel(self.frame_57)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.label_165)

        self.horizontalSpacer_27 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_27)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.frame_57)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")
        self.doubleSpinBox_15.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_15.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.doubleSpinBox_15)

        self.label_166 = QLabel(self.frame_57)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.label_166)


        self.verticalLayout_6.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_34)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_167 = QLabel(self.frame_58)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.label_167)

        self.label_168 = QLabel(self.frame_58)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.label_168)

        self.horizontalSpacer_29 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_29)

        self.timeEdit_6 = QTimeEdit(self.frame_58)
        self.timeEdit_6.setObjectName(u"timeEdit_6")
        self.timeEdit_6.setMinimumSize(QSize(150, 30))
        self.timeEdit_6.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.timeEdit_6)

        self.label_169 = QLabel(self.frame_58)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.label_169)


        self.verticalLayout_6.addWidget(self.frame_58)

        self.label_170 = QLabel(self.frame_34)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMinimumSize(QSize(0, 40))
        self.label_170.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_170.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_170)

        self.frame_59 = QFrame(self.frame_34)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_171 = QLabel(self.frame_59)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.label_171)

        self.label_172 = QLabel(self.frame_59)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.label_172)

        self.horizontalSpacer_30 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_30)

        self.nombre_line_edit_55 = QLineEdit(self.frame_59)
        self.nombre_line_edit_55.setObjectName(u"nombre_line_edit_55")
        self.nombre_line_edit_55.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_55.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_55.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.nombre_line_edit_55)

        self.label_173 = QLabel(self.frame_59)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.label_173)


        self.verticalLayout_6.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_34)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_174 = QLabel(self.frame_60)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.label_174)

        self.label_175 = QLabel(self.frame_60)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.label_175)

        self.horizontalSpacer_31 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_31)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.frame_60)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")
        self.doubleSpinBox_17.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_17.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.doubleSpinBox_17)

        self.label_176 = QLabel(self.frame_60)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.label_176)


        self.verticalLayout_6.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_34)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_177 = QLabel(self.frame_61)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.label_177)

        self.label_178 = QLabel(self.frame_61)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.label_178)

        self.horizontalSpacer_32 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_32)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.frame_61)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")
        self.doubleSpinBox_18.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_18.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.doubleSpinBox_18)

        self.label_179 = QLabel(self.frame_61)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.label_179)


        self.verticalLayout_6.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_34)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_180 = QLabel(self.frame_62)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_61.addWidget(self.label_180)

        self.label_181 = QLabel(self.frame_62)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_61.addWidget(self.label_181)

        self.horizontalSpacer_33 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_33)

        self.timeEdit_7 = QTimeEdit(self.frame_62)
        self.timeEdit_7.setObjectName(u"timeEdit_7")
        self.timeEdit_7.setMinimumSize(QSize(150, 30))
        self.timeEdit_7.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_61.addWidget(self.timeEdit_7)

        self.label_182 = QLabel(self.frame_62)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_61.addWidget(self.label_182)


        self.verticalLayout_6.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_34)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_183 = QLabel(self.frame_63)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_62.addWidget(self.label_183)

        self.label_184 = QLabel(self.frame_63)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_62.addWidget(self.label_184)

        self.horizontalSpacer_35 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_35)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.frame_63)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")
        self.doubleSpinBox_19.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_19.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_62.addWidget(self.doubleSpinBox_19)

        self.label_185 = QLabel(self.frame_63)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_62.addWidget(self.label_185)


        self.verticalLayout_6.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_34)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_186 = QLabel(self.frame_64)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_63.addWidget(self.label_186)

        self.label_187 = QLabel(self.frame_64)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_63.addWidget(self.label_187)

        self.horizontalSpacer_34 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_34)

        self.timeEdit_8 = QTimeEdit(self.frame_64)
        self.timeEdit_8.setObjectName(u"timeEdit_8")
        self.timeEdit_8.setMinimumSize(QSize(150, 30))
        self.timeEdit_8.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_63.addWidget(self.timeEdit_8)

        self.label_188 = QLabel(self.frame_64)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_63.addWidget(self.label_188)


        self.verticalLayout_6.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_34)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_189 = QLabel(self.frame_65)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_64.addWidget(self.label_189)

        self.label_190 = QLabel(self.frame_65)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_64.addWidget(self.label_190)

        self.horizontalSpacer_36 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_36)

        self.timeEdit_9 = QTimeEdit(self.frame_65)
        self.timeEdit_9.setObjectName(u"timeEdit_9")
        self.timeEdit_9.setMinimumSize(QSize(150, 30))
        self.timeEdit_9.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_64.addWidget(self.timeEdit_9)

        self.label_191 = QLabel(self.frame_65)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_64.addWidget(self.label_191)


        self.verticalLayout_6.addWidget(self.frame_65)

        self.label_192 = QLabel(self.frame_34)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setMinimumSize(QSize(0, 40))
        self.label_192.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_192.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_192)

        self.frame_66 = QFrame(self.frame_34)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_193 = QLabel(self.frame_66)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_65.addWidget(self.label_193)

        self.label_194 = QLabel(self.frame_66)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_65.addWidget(self.label_194)

        self.horizontalSpacer_37 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_37)

        self.nombre_line_edit_62 = QLineEdit(self.frame_66)
        self.nombre_line_edit_62.setObjectName(u"nombre_line_edit_62")
        self.nombre_line_edit_62.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_62.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_62.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_65.addWidget(self.nombre_line_edit_62)

        self.label_195 = QLabel(self.frame_66)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_65.addWidget(self.label_195)


        self.verticalLayout_6.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_34)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_196 = QLabel(self.frame_67)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_66.addWidget(self.label_196)

        self.label_197 = QLabel(self.frame_67)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_66.addWidget(self.label_197)

        self.horizontalSpacer_38 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_38)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.frame_67)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")
        self.doubleSpinBox_20.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_20.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_66.addWidget(self.doubleSpinBox_20)

        self.label_198 = QLabel(self.frame_67)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_66.addWidget(self.label_198)


        self.verticalLayout_6.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_34)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_199 = QLabel(self.frame_68)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_67.addWidget(self.label_199)

        self.label_200 = QLabel(self.frame_68)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_67.addWidget(self.label_200)

        self.horizontalSpacer_39 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_39)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.frame_68)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")
        self.doubleSpinBox_21.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_21.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_67.addWidget(self.doubleSpinBox_21)

        self.label_201 = QLabel(self.frame_68)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_67.addWidget(self.label_201)


        self.verticalLayout_6.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_34)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_202 = QLabel(self.frame_69)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_68.addWidget(self.label_202)

        self.label_203 = QLabel(self.frame_69)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_68.addWidget(self.label_203)

        self.horizontalSpacer_40 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_40)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.frame_69)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_22.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_68.addWidget(self.doubleSpinBox_22)

        self.label_204 = QLabel(self.frame_69)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_68.addWidget(self.label_204)


        self.verticalLayout_6.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_34)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_205 = QLabel(self.frame_70)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_69.addWidget(self.label_205)

        self.label_206 = QLabel(self.frame_70)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_69.addWidget(self.label_206)

        self.horizontalSpacer_41 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_41)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.frame_70)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")
        self.doubleSpinBox_24.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_24.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_69.addWidget(self.doubleSpinBox_24)

        self.label_207 = QLabel(self.frame_70)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_69.addWidget(self.label_207)


        self.verticalLayout_6.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_34)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_208 = QLabel(self.frame_71)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_70.addWidget(self.label_208)

        self.label_209 = QLabel(self.frame_71)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_70.addWidget(self.label_209)

        self.horizontalSpacer_42 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_42)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.frame_71)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")
        self.doubleSpinBox_23.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_23.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_70.addWidget(self.doubleSpinBox_23)

        self.label_210 = QLabel(self.frame_71)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_70.addWidget(self.label_210)


        self.verticalLayout_6.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_34)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_211 = QLabel(self.frame_72)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_71.addWidget(self.label_211)

        self.label_212 = QLabel(self.frame_72)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_71.addWidget(self.label_212)

        self.horizontalSpacer_44 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_44)

        self.timeEdit_24 = QTimeEdit(self.frame_72)
        self.timeEdit_24.setObjectName(u"timeEdit_24")
        self.timeEdit_24.setMinimumSize(QSize(150, 30))
        self.timeEdit_24.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_71.addWidget(self.timeEdit_24)

        self.label_213 = QLabel(self.frame_72)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_71.addWidget(self.label_213)


        self.verticalLayout_6.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_34)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_214 = QLabel(self.frame_73)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_72.addWidget(self.label_214)

        self.label_215 = QLabel(self.frame_73)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_72.addWidget(self.label_215)

        self.horizontalSpacer_43 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_43)

        self.timeEdit_23 = QTimeEdit(self.frame_73)
        self.timeEdit_23.setObjectName(u"timeEdit_23")
        self.timeEdit_23.setMinimumSize(QSize(150, 30))
        self.timeEdit_23.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_72.addWidget(self.timeEdit_23)

        self.label_216 = QLabel(self.frame_73)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_72.addWidget(self.label_216)


        self.verticalLayout_6.addWidget(self.frame_73)

        self.label_217 = QLabel(self.frame_34)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMinimumSize(QSize(0, 40))
        self.label_217.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_217.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_217)

        self.frame_74 = QFrame(self.frame_34)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_218 = QLabel(self.frame_74)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_73.addWidget(self.label_218)

        self.label_219 = QLabel(self.frame_74)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_73.addWidget(self.label_219)

        self.horizontalSpacer_45 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_45)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.frame_74)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")
        self.doubleSpinBox_25.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_25.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_73.addWidget(self.doubleSpinBox_25)

        self.label_220 = QLabel(self.frame_74)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_73.addWidget(self.label_220)


        self.verticalLayout_6.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_34)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_221 = QLabel(self.frame_75)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_74.addWidget(self.label_221)

        self.label_222 = QLabel(self.frame_75)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_74.addWidget(self.label_222)

        self.horizontalSpacer_46 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_46)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.frame_75)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")
        self.doubleSpinBox_26.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_26.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_74.addWidget(self.doubleSpinBox_26)

        self.label_223 = QLabel(self.frame_75)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_74.addWidget(self.label_223)


        self.verticalLayout_6.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_34)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_224 = QLabel(self.frame_76)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.label_224)

        self.label_225 = QLabel(self.frame_76)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.label_225)

        self.horizontalSpacer_48 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_48)

        self.timeEdit_10 = QTimeEdit(self.frame_76)
        self.timeEdit_10.setObjectName(u"timeEdit_10")
        self.timeEdit_10.setMinimumSize(QSize(150, 30))
        self.timeEdit_10.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.timeEdit_10)

        self.label_226 = QLabel(self.frame_76)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.label_226)


        self.verticalLayout_6.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_34)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_227 = QLabel(self.frame_77)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_76.addWidget(self.label_227)

        self.label_228 = QLabel(self.frame_77)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_76.addWidget(self.label_228)

        self.horizontalSpacer_49 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_49)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.frame_77)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")
        self.doubleSpinBox_27.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_27.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_76.addWidget(self.doubleSpinBox_27)

        self.label_229 = QLabel(self.frame_77)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_76.addWidget(self.label_229)


        self.verticalLayout_6.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_34)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_230 = QLabel(self.frame_78)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_77.addWidget(self.label_230)

        self.label_231 = QLabel(self.frame_78)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_77.addWidget(self.label_231)

        self.horizontalSpacer_50 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_50)

        self.timeEdit_11 = QTimeEdit(self.frame_78)
        self.timeEdit_11.setObjectName(u"timeEdit_11")
        self.timeEdit_11.setMinimumSize(QSize(150, 30))
        self.timeEdit_11.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_77.addWidget(self.timeEdit_11)

        self.label_232 = QLabel(self.frame_78)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_77.addWidget(self.label_232)


        self.verticalLayout_6.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_34)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_233 = QLabel(self.frame_79)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_78.addWidget(self.label_233)

        self.label_234 = QLabel(self.frame_79)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_78.addWidget(self.label_234)

        self.horizontalSpacer_51 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_51)

        self.nombre_line_edit_75 = QLineEdit(self.frame_79)
        self.nombre_line_edit_75.setObjectName(u"nombre_line_edit_75")
        self.nombre_line_edit_75.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_75.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_75.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_78.addWidget(self.nombre_line_edit_75)

        self.label_235 = QLabel(self.frame_79)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_78.addWidget(self.label_235)


        self.verticalLayout_6.addWidget(self.frame_79)

        self.label_236 = QLabel(self.frame_34)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setMinimumSize(QSize(0, 40))
        self.label_236.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_236.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_236)

        self.frame_137 = QFrame(self.frame_34)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_416 = QLabel(self.frame_137)
        self.label_416.setObjectName(u"label_416")
        self.label_416.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_136.addWidget(self.label_416)

        self.label_417 = QLabel(self.frame_137)
        self.label_417.setObjectName(u"label_417")
        self.label_417.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_136.addWidget(self.label_417)

        self.horizontalSpacer_52 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_52)

        self.doubleSpinBox_28 = QDoubleSpinBox(self.frame_137)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")
        self.doubleSpinBox_28.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_28.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_136.addWidget(self.doubleSpinBox_28)

        self.label_418 = QLabel(self.frame_137)
        self.label_418.setObjectName(u"label_418")
        self.label_418.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_136.addWidget(self.label_418)


        self.verticalLayout_6.addWidget(self.frame_137)

        self.frame_138 = QFrame(self.frame_34)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.label_419 = QLabel(self.frame_138)
        self.label_419.setObjectName(u"label_419")
        self.label_419.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_137.addWidget(self.label_419)

        self.label_420 = QLabel(self.frame_138)
        self.label_420.setObjectName(u"label_420")
        self.label_420.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_137.addWidget(self.label_420)

        self.horizontalSpacer_53 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_53)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.frame_138)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")
        self.doubleSpinBox_29.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_29.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_137.addWidget(self.doubleSpinBox_29)

        self.label_421 = QLabel(self.frame_138)
        self.label_421.setObjectName(u"label_421")
        self.label_421.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_137.addWidget(self.label_421)


        self.verticalLayout_6.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_34)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_422 = QLabel(self.frame_139)
        self.label_422.setObjectName(u"label_422")
        self.label_422.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_138.addWidget(self.label_422)

        self.label_423 = QLabel(self.frame_139)
        self.label_423.setObjectName(u"label_423")
        self.label_423.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_138.addWidget(self.label_423)

        self.horizontalSpacer_54 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_138.addItem(self.horizontalSpacer_54)

        self.timeEdit_34 = QTimeEdit(self.frame_139)
        self.timeEdit_34.setObjectName(u"timeEdit_34")
        self.timeEdit_34.setMinimumSize(QSize(150, 30))
        self.timeEdit_34.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_138.addWidget(self.timeEdit_34)

        self.label_515 = QLabel(self.frame_139)
        self.label_515.setObjectName(u"label_515")
        self.label_515.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_138.addWidget(self.label_515)


        self.verticalLayout_6.addWidget(self.frame_139)

        self.frame_143 = QFrame(self.frame_34)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_434 = QLabel(self.frame_143)
        self.label_434.setObjectName(u"label_434")
        self.label_434.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_142.addWidget(self.label_434)

        self.label_435 = QLabel(self.frame_143)
        self.label_435.setObjectName(u"label_435")
        self.label_435.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_142.addWidget(self.label_435)

        self.horizontalSpacer_55 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_55)

        self.doubleSpinBox_31 = QDoubleSpinBox(self.frame_143)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")
        self.doubleSpinBox_31.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_31.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_142.addWidget(self.doubleSpinBox_31)

        self.horizontalSpacer_138 = QSpacerItem(48, 48, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_138)


        self.verticalLayout_6.addWidget(self.frame_143)

        self.frame_140 = QFrame(self.frame_34)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_425 = QLabel(self.frame_140)
        self.label_425.setObjectName(u"label_425")
        self.label_425.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_139.addWidget(self.label_425)

        self.label_426 = QLabel(self.frame_140)
        self.label_426.setObjectName(u"label_426")
        self.label_426.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_139.addWidget(self.label_426)

        self.horizontalSpacer_56 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_56)

        self.timeEdit_12 = QTimeEdit(self.frame_140)
        self.timeEdit_12.setObjectName(u"timeEdit_12")
        self.timeEdit_12.setMinimumSize(QSize(150, 30))
        self.timeEdit_12.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_139.addWidget(self.timeEdit_12)

        self.label_517 = QLabel(self.frame_140)
        self.label_517.setObjectName(u"label_517")
        self.label_517.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_139.addWidget(self.label_517)


        self.verticalLayout_6.addWidget(self.frame_140)

        self.frame_141 = QFrame(self.frame_34)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.label_428 = QLabel(self.frame_141)
        self.label_428.setObjectName(u"label_428")
        self.label_428.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_140.addWidget(self.label_428)

        self.label_429 = QLabel(self.frame_141)
        self.label_429.setObjectName(u"label_429")
        self.label_429.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_140.addWidget(self.label_429)

        self.horizontalSpacer_57 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_57)

        self.timeEdit_35 = QTimeEdit(self.frame_141)
        self.timeEdit_35.setObjectName(u"timeEdit_35")
        self.timeEdit_35.setMinimumSize(QSize(150, 30))
        self.timeEdit_35.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_140.addWidget(self.timeEdit_35)

        self.label_518 = QLabel(self.frame_141)
        self.label_518.setObjectName(u"label_518")
        self.label_518.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_140.addWidget(self.label_518)


        self.verticalLayout_6.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_34)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_431 = QLabel(self.frame_142)
        self.label_431.setObjectName(u"label_431")
        self.label_431.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_141.addWidget(self.label_431)

        self.label_432 = QLabel(self.frame_142)
        self.label_432.setObjectName(u"label_432")
        self.label_432.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_141.addWidget(self.label_432)

        self.horizontalSpacer_58 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_58)

        self.doubleSpinBox_33 = QDoubleSpinBox(self.frame_142)
        self.doubleSpinBox_33.setObjectName(u"doubleSpinBox_33")
        self.doubleSpinBox_33.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_33.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_141.addWidget(self.doubleSpinBox_33)

        self.label_424 = QLabel(self.frame_142)
        self.label_424.setObjectName(u"label_424")
        self.label_424.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_141.addWidget(self.label_424)


        self.verticalLayout_6.addWidget(self.frame_142)

        self.frame_144 = QFrame(self.frame_34)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_437 = QLabel(self.frame_144)
        self.label_437.setObjectName(u"label_437")
        self.label_437.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_143.addWidget(self.label_437)

        self.label_438 = QLabel(self.frame_144)
        self.label_438.setObjectName(u"label_438")
        self.label_438.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_143.addWidget(self.label_438)

        self.horizontalSpacer_59 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_59)

        self.doubleSpinBox_62 = QDoubleSpinBox(self.frame_144)
        self.doubleSpinBox_62.setObjectName(u"doubleSpinBox_62")
        self.doubleSpinBox_62.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_62.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_143.addWidget(self.doubleSpinBox_62)

        self.label_427 = QLabel(self.frame_144)
        self.label_427.setObjectName(u"label_427")
        self.label_427.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_143.addWidget(self.label_427)


        self.verticalLayout_6.addWidget(self.frame_144)

        self.frame_170 = QFrame(self.frame_34)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_446 = QLabel(self.frame_170)
        self.label_446.setObjectName(u"label_446")
        self.label_446.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_158.addWidget(self.label_446)

        self.label_449 = QLabel(self.frame_170)
        self.label_449.setObjectName(u"label_449")
        self.label_449.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_158.addWidget(self.label_449)

        self.horizontalSpacer_136 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_158.addItem(self.horizontalSpacer_136)

        self.doubleSpinBox_63 = QDoubleSpinBox(self.frame_170)
        self.doubleSpinBox_63.setObjectName(u"doubleSpinBox_63")
        self.doubleSpinBox_63.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_63.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_158.addWidget(self.doubleSpinBox_63)

        self.label_430 = QLabel(self.frame_170)
        self.label_430.setObjectName(u"label_430")
        self.label_430.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_158.addWidget(self.label_430)


        self.verticalLayout_6.addWidget(self.frame_170)

        self.frame_171 = QFrame(self.frame_34)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.label_484 = QLabel(self.frame_171)
        self.label_484.setObjectName(u"label_484")
        self.label_484.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_168.addWidget(self.label_484)

        self.label_485 = QLabel(self.frame_171)
        self.label_485.setObjectName(u"label_485")
        self.label_485.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_168.addWidget(self.label_485)

        self.horizontalSpacer_137 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_168.addItem(self.horizontalSpacer_137)

        self.timeEdit_33 = QTimeEdit(self.frame_171)
        self.timeEdit_33.setObjectName(u"timeEdit_33")
        self.timeEdit_33.setMinimumSize(QSize(150, 30))
        self.timeEdit_33.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_168.addWidget(self.timeEdit_33)

        self.label_516 = QLabel(self.frame_171)
        self.label_516.setObjectName(u"label_516")
        self.label_516.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_168.addWidget(self.label_516)


        self.verticalLayout_6.addWidget(self.frame_171)

        self.frame_145 = QFrame(self.frame_34)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_440 = QLabel(self.frame_145)
        self.label_440.setObjectName(u"label_440")
        self.label_440.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_144.addWidget(self.label_440)

        self.label_441 = QLabel(self.frame_145)
        self.label_441.setObjectName(u"label_441")
        self.label_441.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_144.addWidget(self.label_441)

        self.horizontalSpacer_60 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_60)

        self.timeEdit_13 = QTimeEdit(self.frame_145)
        self.timeEdit_13.setObjectName(u"timeEdit_13")
        self.timeEdit_13.setMinimumSize(QSize(150, 30))
        self.timeEdit_13.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_144.addWidget(self.timeEdit_13)

        self.label_442 = QLabel(self.frame_145)
        self.label_442.setObjectName(u"label_442")
        self.label_442.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_144.addWidget(self.label_442)


        self.verticalLayout_6.addWidget(self.frame_145)

        self.label_1112 = QLabel(self.frame_34)
        self.label_1112.setObjectName(u"label_1112")
        self.label_1112.setMinimumSize(QSize(0, 40))
        self.label_1112.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_1112.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_1112)

        self.frame_146 = QFrame(self.frame_34)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.label_444 = QLabel(self.frame_146)
        self.label_444.setObjectName(u"label_444")
        self.label_444.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_145.addWidget(self.label_444)

        self.label_445 = QLabel(self.frame_146)
        self.label_445.setObjectName(u"label_445")
        self.label_445.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_145.addWidget(self.label_445)

        self.horizontalSpacer_61 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_61)

        self.doubleSpinBox_34 = QDoubleSpinBox(self.frame_146)
        self.doubleSpinBox_34.setObjectName(u"doubleSpinBox_34")
        self.doubleSpinBox_34.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_34.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_145.addWidget(self.doubleSpinBox_34)

        self.label_1138 = QLabel(self.frame_146)
        self.label_1138.setObjectName(u"label_1138")
        self.label_1138.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_145.addWidget(self.label_1138)


        self.verticalLayout_6.addWidget(self.frame_146)

        self.frame_338 = QFrame(self.frame_34)
        self.frame_338.setObjectName(u"frame_338")
        self.frame_338.setFrameShape(QFrame.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_361 = QHBoxLayout(self.frame_338)
        self.horizontalLayout_361.setObjectName(u"horizontalLayout_361")
        self.label_1113 = QLabel(self.frame_338)
        self.label_1113.setObjectName(u"label_1113")
        self.label_1113.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_361.addWidget(self.label_1113)

        self.label_1114 = QLabel(self.frame_338)
        self.label_1114.setObjectName(u"label_1114")
        self.label_1114.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_361.addWidget(self.label_1114)

        self.horizontalSpacer_62 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_361.addItem(self.horizontalSpacer_62)

        self.doubleSpinBox_35 = QDoubleSpinBox(self.frame_338)
        self.doubleSpinBox_35.setObjectName(u"doubleSpinBox_35")
        self.doubleSpinBox_35.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_35.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_361.addWidget(self.doubleSpinBox_35)

        self.label_1137 = QLabel(self.frame_338)
        self.label_1137.setObjectName(u"label_1137")
        self.label_1137.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_361.addWidget(self.label_1137)


        self.verticalLayout_6.addWidget(self.frame_338)

        self.frame_339 = QFrame(self.frame_34)
        self.frame_339.setObjectName(u"frame_339")
        self.frame_339.setFrameShape(QFrame.StyledPanel)
        self.frame_339.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_362 = QHBoxLayout(self.frame_339)
        self.horizontalLayout_362.setObjectName(u"horizontalLayout_362")
        self.label_1116 = QLabel(self.frame_339)
        self.label_1116.setObjectName(u"label_1116")
        self.label_1116.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_362.addWidget(self.label_1116)

        self.label_1117 = QLabel(self.frame_339)
        self.label_1117.setObjectName(u"label_1117")
        self.label_1117.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_362.addWidget(self.label_1117)

        self.horizontalSpacer_63 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_362.addItem(self.horizontalSpacer_63)

        self.doubleSpinBox_36 = QDoubleSpinBox(self.frame_339)
        self.doubleSpinBox_36.setObjectName(u"doubleSpinBox_36")
        self.doubleSpinBox_36.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_36.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_362.addWidget(self.doubleSpinBox_36)

        self.label_1118 = QLabel(self.frame_339)
        self.label_1118.setObjectName(u"label_1118")
        self.label_1118.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_362.addWidget(self.label_1118)


        self.verticalLayout_6.addWidget(self.frame_339)

        self.frame_344 = QFrame(self.frame_34)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setFrameShape(QFrame.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_363 = QHBoxLayout(self.frame_344)
        self.horizontalLayout_363.setObjectName(u"horizontalLayout_363")
        self.label_1119 = QLabel(self.frame_344)
        self.label_1119.setObjectName(u"label_1119")
        self.label_1119.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_363.addWidget(self.label_1119)

        self.label_1120 = QLabel(self.frame_344)
        self.label_1120.setObjectName(u"label_1120")
        self.label_1120.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_363.addWidget(self.label_1120)

        self.horizontalSpacer_64 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_363.addItem(self.horizontalSpacer_64)

        self.doubleSpinBox_37 = QDoubleSpinBox(self.frame_344)
        self.doubleSpinBox_37.setObjectName(u"doubleSpinBox_37")
        self.doubleSpinBox_37.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_37.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_363.addWidget(self.doubleSpinBox_37)

        self.label_1121 = QLabel(self.frame_344)
        self.label_1121.setObjectName(u"label_1121")
        self.label_1121.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_363.addWidget(self.label_1121)


        self.verticalLayout_6.addWidget(self.frame_344)

        self.frame_345 = QFrame(self.frame_34)
        self.frame_345.setObjectName(u"frame_345")
        self.frame_345.setFrameShape(QFrame.StyledPanel)
        self.frame_345.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_364 = QHBoxLayout(self.frame_345)
        self.horizontalLayout_364.setObjectName(u"horizontalLayout_364")
        self.label_1122 = QLabel(self.frame_345)
        self.label_1122.setObjectName(u"label_1122")
        self.label_1122.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_364.addWidget(self.label_1122)

        self.label_1123 = QLabel(self.frame_345)
        self.label_1123.setObjectName(u"label_1123")
        self.label_1123.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_364.addWidget(self.label_1123)

        self.horizontalSpacer_65 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_364.addItem(self.horizontalSpacer_65)

        self.timeEdit_14 = QTimeEdit(self.frame_345)
        self.timeEdit_14.setObjectName(u"timeEdit_14")
        self.timeEdit_14.setMinimumSize(QSize(150, 30))
        self.timeEdit_14.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_364.addWidget(self.timeEdit_14)

        self.label_1124 = QLabel(self.frame_345)
        self.label_1124.setObjectName(u"label_1124")
        self.label_1124.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_364.addWidget(self.label_1124)


        self.verticalLayout_6.addWidget(self.frame_345)

        self.frame_346 = QFrame(self.frame_34)
        self.frame_346.setObjectName(u"frame_346")
        self.frame_346.setFrameShape(QFrame.StyledPanel)
        self.frame_346.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_365 = QHBoxLayout(self.frame_346)
        self.horizontalLayout_365.setObjectName(u"horizontalLayout_365")
        self.label_1125 = QLabel(self.frame_346)
        self.label_1125.setObjectName(u"label_1125")
        self.label_1125.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_365.addWidget(self.label_1125)

        self.label_1126 = QLabel(self.frame_346)
        self.label_1126.setObjectName(u"label_1126")
        self.label_1126.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_365.addWidget(self.label_1126)

        self.horizontalSpacer_66 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_365.addItem(self.horizontalSpacer_66)

        self.doubleSpinBox_38 = QDoubleSpinBox(self.frame_346)
        self.doubleSpinBox_38.setObjectName(u"doubleSpinBox_38")
        self.doubleSpinBox_38.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_38.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_365.addWidget(self.doubleSpinBox_38)

        self.label_1127 = QLabel(self.frame_346)
        self.label_1127.setObjectName(u"label_1127")
        self.label_1127.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_365.addWidget(self.label_1127)


        self.verticalLayout_6.addWidget(self.frame_346)

        self.frame_347 = QFrame(self.frame_34)
        self.frame_347.setObjectName(u"frame_347")
        self.frame_347.setFrameShape(QFrame.StyledPanel)
        self.frame_347.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_366 = QHBoxLayout(self.frame_347)
        self.horizontalLayout_366.setObjectName(u"horizontalLayout_366")
        self.label_1128 = QLabel(self.frame_347)
        self.label_1128.setObjectName(u"label_1128")
        self.label_1128.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_366.addWidget(self.label_1128)

        self.label_1129 = QLabel(self.frame_347)
        self.label_1129.setObjectName(u"label_1129")
        self.label_1129.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_366.addWidget(self.label_1129)

        self.horizontalSpacer_67 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_366.addItem(self.horizontalSpacer_67)

        self.doubleSpinBox_39 = QDoubleSpinBox(self.frame_347)
        self.doubleSpinBox_39.setObjectName(u"doubleSpinBox_39")
        self.doubleSpinBox_39.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_39.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_366.addWidget(self.doubleSpinBox_39)

        self.label_1130 = QLabel(self.frame_347)
        self.label_1130.setObjectName(u"label_1130")
        self.label_1130.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_366.addWidget(self.label_1130)


        self.verticalLayout_6.addWidget(self.frame_347)

        self.frame_348 = QFrame(self.frame_34)
        self.frame_348.setObjectName(u"frame_348")
        self.frame_348.setFrameShape(QFrame.StyledPanel)
        self.frame_348.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_367 = QHBoxLayout(self.frame_348)
        self.horizontalLayout_367.setObjectName(u"horizontalLayout_367")
        self.label_1131 = QLabel(self.frame_348)
        self.label_1131.setObjectName(u"label_1131")
        self.label_1131.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_367.addWidget(self.label_1131)

        self.label_1132 = QLabel(self.frame_348)
        self.label_1132.setObjectName(u"label_1132")
        self.label_1132.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_367.addWidget(self.label_1132)

        self.horizontalSpacer_68 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_367.addItem(self.horizontalSpacer_68)

        self.timeEdit_26 = QTimeEdit(self.frame_348)
        self.timeEdit_26.setObjectName(u"timeEdit_26")
        self.timeEdit_26.setMinimumSize(QSize(150, 30))
        self.timeEdit_26.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_367.addWidget(self.timeEdit_26)

        self.label_1133 = QLabel(self.frame_348)
        self.label_1133.setObjectName(u"label_1133")
        self.label_1133.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_367.addWidget(self.label_1133)


        self.verticalLayout_6.addWidget(self.frame_348)

        self.frame_349 = QFrame(self.frame_34)
        self.frame_349.setObjectName(u"frame_349")
        self.frame_349.setFrameShape(QFrame.StyledPanel)
        self.frame_349.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_368 = QHBoxLayout(self.frame_349)
        self.horizontalLayout_368.setObjectName(u"horizontalLayout_368")
        self.label_1134 = QLabel(self.frame_349)
        self.label_1134.setObjectName(u"label_1134")
        self.label_1134.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_368.addWidget(self.label_1134)

        self.label_1135 = QLabel(self.frame_349)
        self.label_1135.setObjectName(u"label_1135")
        self.label_1135.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_368.addWidget(self.label_1135)

        self.horizontalSpacer_69 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_368.addItem(self.horizontalSpacer_69)

        self.timeEdit_15 = QTimeEdit(self.frame_349)
        self.timeEdit_15.setObjectName(u"timeEdit_15")
        self.timeEdit_15.setMinimumSize(QSize(150, 30))
        self.timeEdit_15.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_368.addWidget(self.timeEdit_15)

        self.label_1136 = QLabel(self.frame_349)
        self.label_1136.setObjectName(u"label_1136")
        self.label_1136.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_368.addWidget(self.label_1136)


        self.verticalLayout_6.addWidget(self.frame_349)

        self.label_443 = QLabel(self.frame_34)
        self.label_443.setObjectName(u"label_443")
        self.label_443.setMinimumSize(QSize(0, 40))
        self.label_443.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_443.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_443)

        self.frame_337 = QFrame(self.frame_34)
        self.frame_337.setObjectName(u"frame_337")
        self.frame_337.setFrameShape(QFrame.StyledPanel)
        self.frame_337.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_360 = QHBoxLayout(self.frame_337)
        self.horizontalLayout_360.setObjectName(u"horizontalLayout_360")
        self.label_1109 = QLabel(self.frame_337)
        self.label_1109.setObjectName(u"label_1109")
        self.label_1109.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_360.addWidget(self.label_1109)

        self.label_1110 = QLabel(self.frame_337)
        self.label_1110.setObjectName(u"label_1110")
        self.label_1110.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_360.addWidget(self.label_1110)

        self.horizontalSpacer_70 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_360.addItem(self.horizontalSpacer_70)

        self.nombre_line_edit_357 = QLineEdit(self.frame_337)
        self.nombre_line_edit_357.setObjectName(u"nombre_line_edit_357")
        self.nombre_line_edit_357.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_357.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_357.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_360.addWidget(self.nombre_line_edit_357)

        self.label_1142 = QLabel(self.frame_337)
        self.label_1142.setObjectName(u"label_1142")
        self.label_1142.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_360.addWidget(self.label_1142)


        self.verticalLayout_6.addWidget(self.frame_337)

        self.frame_147 = QFrame(self.frame_34)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_447 = QLabel(self.frame_147)
        self.label_447.setObjectName(u"label_447")
        self.label_447.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_146.addWidget(self.label_447)

        self.label_448 = QLabel(self.frame_147)
        self.label_448.setObjectName(u"label_448")
        self.label_448.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_146.addWidget(self.label_448)

        self.horizontalSpacer_71 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_71)

        self.nombre_line_edit_143 = QLineEdit(self.frame_147)
        self.nombre_line_edit_143.setObjectName(u"nombre_line_edit_143")
        self.nombre_line_edit_143.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_143.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_143.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_146.addWidget(self.nombre_line_edit_143)

        self.label_1141 = QLabel(self.frame_147)
        self.label_1141.setObjectName(u"label_1141")
        self.label_1141.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_146.addWidget(self.label_1141)


        self.verticalLayout_6.addWidget(self.frame_147)

        self.frame_148 = QFrame(self.frame_34)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_450 = QLabel(self.frame_148)
        self.label_450.setObjectName(u"label_450")
        self.label_450.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_147.addWidget(self.label_450)

        self.label_451 = QLabel(self.frame_148)
        self.label_451.setObjectName(u"label_451")
        self.label_451.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_147.addWidget(self.label_451)

        self.horizontalSpacer_72 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_72)

        self.doubleSpinBox_40 = QDoubleSpinBox(self.frame_148)
        self.doubleSpinBox_40.setObjectName(u"doubleSpinBox_40")
        self.doubleSpinBox_40.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_40.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_147.addWidget(self.doubleSpinBox_40)

        self.label_452 = QLabel(self.frame_148)
        self.label_452.setObjectName(u"label_452")
        self.label_452.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_147.addWidget(self.label_452)


        self.verticalLayout_6.addWidget(self.frame_148)

        self.frame_149 = QFrame(self.frame_34)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_453 = QLabel(self.frame_149)
        self.label_453.setObjectName(u"label_453")
        self.label_453.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_148.addWidget(self.label_453)

        self.label_454 = QLabel(self.frame_149)
        self.label_454.setObjectName(u"label_454")
        self.label_454.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_148.addWidget(self.label_454)

        self.horizontalSpacer_73 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_73)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.frame_149)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")
        self.doubleSpinBox_41.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_41.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_148.addWidget(self.doubleSpinBox_41)

        self.label_455 = QLabel(self.frame_149)
        self.label_455.setObjectName(u"label_455")
        self.label_455.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_148.addWidget(self.label_455)


        self.verticalLayout_6.addWidget(self.frame_149)

        self.frame_150 = QFrame(self.frame_34)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.label_456 = QLabel(self.frame_150)
        self.label_456.setObjectName(u"label_456")
        self.label_456.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_149.addWidget(self.label_456)

        self.label_457 = QLabel(self.frame_150)
        self.label_457.setObjectName(u"label_457")
        self.label_457.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_149.addWidget(self.label_457)

        self.horizontalSpacer_75 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_75)

        self.doubleSpinBox_42 = QDoubleSpinBox(self.frame_150)
        self.doubleSpinBox_42.setObjectName(u"doubleSpinBox_42")
        self.doubleSpinBox_42.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_42.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_149.addWidget(self.doubleSpinBox_42)

        self.label_458 = QLabel(self.frame_150)
        self.label_458.setObjectName(u"label_458")
        self.label_458.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_149.addWidget(self.label_458)


        self.verticalLayout_6.addWidget(self.frame_150)

        self.frame_151 = QFrame(self.frame_34)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_459 = QLabel(self.frame_151)
        self.label_459.setObjectName(u"label_459")
        self.label_459.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_150.addWidget(self.label_459)

        self.label_460 = QLabel(self.frame_151)
        self.label_460.setObjectName(u"label_460")
        self.label_460.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_150.addWidget(self.label_460)

        self.horizontalSpacer_76 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_150.addItem(self.horizontalSpacer_76)

        self.doubleSpinBox_43 = QDoubleSpinBox(self.frame_151)
        self.doubleSpinBox_43.setObjectName(u"doubleSpinBox_43")
        self.doubleSpinBox_43.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_43.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_150.addWidget(self.doubleSpinBox_43)

        self.label_461 = QLabel(self.frame_151)
        self.label_461.setObjectName(u"label_461")
        self.label_461.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_150.addWidget(self.label_461)


        self.verticalLayout_6.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_34)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.label_462 = QLabel(self.frame_152)
        self.label_462.setObjectName(u"label_462")
        self.label_462.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_151.addWidget(self.label_462)

        self.label_463 = QLabel(self.frame_152)
        self.label_463.setObjectName(u"label_463")
        self.label_463.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_151.addWidget(self.label_463)

        self.horizontalSpacer_74 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_74)

        self.doubleSpinBox_44 = QDoubleSpinBox(self.frame_152)
        self.doubleSpinBox_44.setObjectName(u"doubleSpinBox_44")
        self.doubleSpinBox_44.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_44.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_151.addWidget(self.doubleSpinBox_44)

        self.label_464 = QLabel(self.frame_152)
        self.label_464.setObjectName(u"label_464")
        self.label_464.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_151.addWidget(self.label_464)


        self.verticalLayout_6.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_34)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.label_465 = QLabel(self.frame_153)
        self.label_465.setObjectName(u"label_465")
        self.label_465.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_152.addWidget(self.label_465)

        self.label_466 = QLabel(self.frame_153)
        self.label_466.setObjectName(u"label_466")
        self.label_466.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_152.addWidget(self.label_466)

        self.horizontalSpacer_77 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_152.addItem(self.horizontalSpacer_77)

        self.timeEdit_16 = QTimeEdit(self.frame_153)
        self.timeEdit_16.setObjectName(u"timeEdit_16")
        self.timeEdit_16.setMinimumSize(QSize(150, 30))
        self.timeEdit_16.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_152.addWidget(self.timeEdit_16)

        self.label_467 = QLabel(self.frame_153)
        self.label_467.setObjectName(u"label_467")
        self.label_467.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_152.addWidget(self.label_467)


        self.verticalLayout_6.addWidget(self.frame_153)

        self.frame_154 = QFrame(self.frame_34)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.label_468 = QLabel(self.frame_154)
        self.label_468.setObjectName(u"label_468")
        self.label_468.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_153.addWidget(self.label_468)

        self.label_469 = QLabel(self.frame_154)
        self.label_469.setObjectName(u"label_469")
        self.label_469.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_153.addWidget(self.label_469)

        self.horizontalSpacer_78 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_78)

        self.doubleSpinBox_45 = QDoubleSpinBox(self.frame_154)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")
        self.doubleSpinBox_45.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_45.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_153.addWidget(self.doubleSpinBox_45)

        self.label_470 = QLabel(self.frame_154)
        self.label_470.setObjectName(u"label_470")
        self.label_470.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_153.addWidget(self.label_470)


        self.verticalLayout_6.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_34)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.label_471 = QLabel(self.frame_155)
        self.label_471.setObjectName(u"label_471")
        self.label_471.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_154.addWidget(self.label_471)

        self.label_472 = QLabel(self.frame_155)
        self.label_472.setObjectName(u"label_472")
        self.label_472.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_154.addWidget(self.label_472)

        self.horizontalSpacer_79 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_79)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.frame_155)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")
        self.doubleSpinBox_46.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_46.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_154.addWidget(self.doubleSpinBox_46)

        self.label_473 = QLabel(self.frame_155)
        self.label_473.setObjectName(u"label_473")
        self.label_473.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_154.addWidget(self.label_473)


        self.verticalLayout_6.addWidget(self.frame_155)

        self.frame_156 = QFrame(self.frame_34)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.frame_156)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.label_474 = QLabel(self.frame_156)
        self.label_474.setObjectName(u"label_474")
        self.label_474.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_155.addWidget(self.label_474)

        self.label_475 = QLabel(self.frame_156)
        self.label_475.setObjectName(u"label_475")
        self.label_475.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_155.addWidget(self.label_475)

        self.horizontalSpacer_80 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_155.addItem(self.horizontalSpacer_80)

        self.timeEdit_27 = QTimeEdit(self.frame_156)
        self.timeEdit_27.setObjectName(u"timeEdit_27")
        self.timeEdit_27.setMinimumSize(QSize(150, 30))
        self.timeEdit_27.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_155.addWidget(self.timeEdit_27)

        self.label_476 = QLabel(self.frame_156)
        self.label_476.setObjectName(u"label_476")
        self.label_476.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_155.addWidget(self.label_476)


        self.verticalLayout_6.addWidget(self.frame_156)

        self.frame_158 = QFrame(self.frame_34)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_480 = QLabel(self.frame_158)
        self.label_480.setObjectName(u"label_480")
        self.label_480.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_157.addWidget(self.label_480)

        self.label_481 = QLabel(self.frame_158)
        self.label_481.setObjectName(u"label_481")
        self.label_481.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_157.addWidget(self.label_481)

        self.horizontalSpacer_81 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157.addItem(self.horizontalSpacer_81)

        self.doubleSpinBox_47 = QDoubleSpinBox(self.frame_158)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")
        self.doubleSpinBox_47.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_47.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_157.addWidget(self.doubleSpinBox_47)

        self.label_482 = QLabel(self.frame_158)
        self.label_482.setObjectName(u"label_482")
        self.label_482.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_157.addWidget(self.label_482)


        self.verticalLayout_6.addWidget(self.frame_158)

        self.frame_160 = QFrame(self.frame_34)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_486 = QLabel(self.frame_160)
        self.label_486.setObjectName(u"label_486")
        self.label_486.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_159.addWidget(self.label_486)

        self.label_487 = QLabel(self.frame_160)
        self.label_487.setObjectName(u"label_487")
        self.label_487.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_159.addWidget(self.label_487)

        self.horizontalSpacer_83 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_159.addItem(self.horizontalSpacer_83)

        self.timeEdit_17 = QTimeEdit(self.frame_160)
        self.timeEdit_17.setObjectName(u"timeEdit_17")
        self.timeEdit_17.setMinimumSize(QSize(150, 30))
        self.timeEdit_17.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_159.addWidget(self.timeEdit_17)

        self.label_488 = QLabel(self.frame_160)
        self.label_488.setObjectName(u"label_488")
        self.label_488.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_159.addWidget(self.label_488)


        self.verticalLayout_6.addWidget(self.frame_160)

        self.frame_161 = QFrame(self.frame_34)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_489 = QLabel(self.frame_161)
        self.label_489.setObjectName(u"label_489")
        self.label_489.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_160.addWidget(self.label_489)

        self.label_490 = QLabel(self.frame_161)
        self.label_490.setObjectName(u"label_490")
        self.label_490.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_160.addWidget(self.label_490)

        self.horizontalSpacer_84 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_160.addItem(self.horizontalSpacer_84)

        self.doubleSpinBox_48 = QDoubleSpinBox(self.frame_161)
        self.doubleSpinBox_48.setObjectName(u"doubleSpinBox_48")
        self.doubleSpinBox_48.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_48.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_160.addWidget(self.doubleSpinBox_48)

        self.label_491 = QLabel(self.frame_161)
        self.label_491.setObjectName(u"label_491")
        self.label_491.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_160.addWidget(self.label_491)


        self.verticalLayout_6.addWidget(self.frame_161)

        self.frame_162 = QFrame(self.frame_34)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_492 = QLabel(self.frame_162)
        self.label_492.setObjectName(u"label_492")
        self.label_492.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_161.addWidget(self.label_492)

        self.label_493 = QLabel(self.frame_162)
        self.label_493.setObjectName(u"label_493")
        self.label_493.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_161.addWidget(self.label_493)

        self.horizontalSpacer_85 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_161.addItem(self.horizontalSpacer_85)

        self.doubleSpinBox_49 = QDoubleSpinBox(self.frame_162)
        self.doubleSpinBox_49.setObjectName(u"doubleSpinBox_49")
        self.doubleSpinBox_49.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_49.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_161.addWidget(self.doubleSpinBox_49)

        self.label_494 = QLabel(self.frame_162)
        self.label_494.setObjectName(u"label_494")
        self.label_494.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_161.addWidget(self.label_494)


        self.verticalLayout_6.addWidget(self.frame_162)

        self.frame_163 = QFrame(self.frame_34)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_495 = QLabel(self.frame_163)
        self.label_495.setObjectName(u"label_495")
        self.label_495.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_162.addWidget(self.label_495)

        self.label_496 = QLabel(self.frame_163)
        self.label_496.setObjectName(u"label_496")
        self.label_496.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_162.addWidget(self.label_496)

        self.horizontalSpacer_86 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_162.addItem(self.horizontalSpacer_86)

        self.timeEdit_28 = QTimeEdit(self.frame_163)
        self.timeEdit_28.setObjectName(u"timeEdit_28")
        self.timeEdit_28.setMinimumSize(QSize(150, 30))
        self.timeEdit_28.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_162.addWidget(self.timeEdit_28)

        self.label_497 = QLabel(self.frame_163)
        self.label_497.setObjectName(u"label_497")
        self.label_497.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_162.addWidget(self.label_497)


        self.verticalLayout_6.addWidget(self.frame_163)

        self.frame_167 = QFrame(self.frame_34)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.frame_167)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_508 = QLabel(self.frame_167)
        self.label_508.setObjectName(u"label_508")
        self.label_508.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_166.addWidget(self.label_508)

        self.label_509 = QLabel(self.frame_167)
        self.label_509.setObjectName(u"label_509")
        self.label_509.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_166.addWidget(self.label_509)

        self.horizontalSpacer_87 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_166.addItem(self.horizontalSpacer_87)

        self.timeEdit_18 = QTimeEdit(self.frame_167)
        self.timeEdit_18.setObjectName(u"timeEdit_18")
        self.timeEdit_18.setMinimumSize(QSize(150, 30))
        self.timeEdit_18.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_166.addWidget(self.timeEdit_18)

        self.label_510 = QLabel(self.frame_167)
        self.label_510.setObjectName(u"label_510")
        self.label_510.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_166.addWidget(self.label_510)


        self.verticalLayout_6.addWidget(self.frame_167)

        self.label_504 = QLabel(self.frame_34)
        self.label_504.setObjectName(u"label_504")
        self.label_504.setMinimumSize(QSize(0, 40))
        self.label_504.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_504.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_504)

        self.frame_340 = QFrame(self.frame_34)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setFrameShape(QFrame.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_369 = QHBoxLayout(self.frame_340)
        self.horizontalLayout_369.setObjectName(u"horizontalLayout_369")
        self.label_1115 = QLabel(self.frame_340)
        self.label_1115.setObjectName(u"label_1115")
        self.label_1115.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_369.addWidget(self.label_1115)

        self.label_1139 = QLabel(self.frame_340)
        self.label_1139.setObjectName(u"label_1139")
        self.label_1139.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_369.addWidget(self.label_1139)

        self.horizontalSpacer_90 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_369.addItem(self.horizontalSpacer_90)

        self.nombre_line_edit_366 = QLineEdit(self.frame_340)
        self.nombre_line_edit_366.setObjectName(u"nombre_line_edit_366")
        self.nombre_line_edit_366.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_366.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_366.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_369.addWidget(self.nombre_line_edit_366)

        self.label_1140 = QLabel(self.frame_340)
        self.label_1140.setObjectName(u"label_1140")
        self.label_1140.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_369.addWidget(self.label_1140)


        self.verticalLayout_6.addWidget(self.frame_340)

        self.frame_166 = QFrame(self.frame_34)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.label_511 = QLabel(self.frame_166)
        self.label_511.setObjectName(u"label_511")
        self.label_511.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_167.addWidget(self.label_511)

        self.label_512 = QLabel(self.frame_166)
        self.label_512.setObjectName(u"label_512")
        self.label_512.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_167.addWidget(self.label_512)

        self.horizontalSpacer_93 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_167.addItem(self.horizontalSpacer_93)

        self.nombre_line_edit_164 = QLineEdit(self.frame_166)
        self.nombre_line_edit_164.setObjectName(u"nombre_line_edit_164")
        self.nombre_line_edit_164.setMinimumSize(QSize(0, 30))
        self.nombre_line_edit_164.setMaximumSize(QSize(150, 16777215))
        self.nombre_line_edit_164.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_167.addWidget(self.nombre_line_edit_164)

        self.label_513 = QLabel(self.frame_166)
        self.label_513.setObjectName(u"label_513")
        self.label_513.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_167.addWidget(self.label_513)


        self.verticalLayout_6.addWidget(self.frame_166)

        self.frame_157 = QFrame(self.frame_34)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_477 = QLabel(self.frame_157)
        self.label_477.setObjectName(u"label_477")
        self.label_477.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_156.addWidget(self.label_477)

        self.label_478 = QLabel(self.frame_157)
        self.label_478.setObjectName(u"label_478")
        self.label_478.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_156.addWidget(self.label_478)

        self.horizontalSpacer_88 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_156.addItem(self.horizontalSpacer_88)

        self.doubleSpinBox_50 = QDoubleSpinBox(self.frame_157)
        self.doubleSpinBox_50.setObjectName(u"doubleSpinBox_50")
        self.doubleSpinBox_50.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_50.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_156.addWidget(self.doubleSpinBox_50)

        self.label_479 = QLabel(self.frame_157)
        self.label_479.setObjectName(u"label_479")
        self.label_479.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_156.addWidget(self.label_479)


        self.verticalLayout_6.addWidget(self.frame_157)

        self.frame_164 = QFrame(self.frame_34)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_501 = QLabel(self.frame_164)
        self.label_501.setObjectName(u"label_501")
        self.label_501.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_164.addWidget(self.label_501)

        self.label_502 = QLabel(self.frame_164)
        self.label_502.setObjectName(u"label_502")
        self.label_502.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_164.addWidget(self.label_502)

        self.horizontalSpacer_91 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_164.addItem(self.horizontalSpacer_91)

        self.doubleSpinBox_51 = QDoubleSpinBox(self.frame_164)
        self.doubleSpinBox_51.setObjectName(u"doubleSpinBox_51")
        self.doubleSpinBox_51.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_51.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_164.addWidget(self.doubleSpinBox_51)

        self.label_503 = QLabel(self.frame_164)
        self.label_503.setObjectName(u"label_503")
        self.label_503.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_164.addWidget(self.label_503)


        self.verticalLayout_6.addWidget(self.frame_164)

        self.frame_159 = QFrame(self.frame_34)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.label_498 = QLabel(self.frame_159)
        self.label_498.setObjectName(u"label_498")
        self.label_498.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_163.addWidget(self.label_498)

        self.label_499 = QLabel(self.frame_159)
        self.label_499.setObjectName(u"label_499")
        self.label_499.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_163.addWidget(self.label_499)

        self.horizontalSpacer_89 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_89)

        self.doubleSpinBox_52 = QDoubleSpinBox(self.frame_159)
        self.doubleSpinBox_52.setObjectName(u"doubleSpinBox_52")
        self.doubleSpinBox_52.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_52.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_163.addWidget(self.doubleSpinBox_52)

        self.label_500 = QLabel(self.frame_159)
        self.label_500.setObjectName(u"label_500")
        self.label_500.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_163.addWidget(self.label_500)


        self.verticalLayout_6.addWidget(self.frame_159)

        self.frame_168 = QFrame(self.frame_34)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_339 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_339.setObjectName(u"horizontalLayout_339")
        self.label_1046 = QLabel(self.frame_168)
        self.label_1046.setObjectName(u"label_1046")
        self.label_1046.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_339.addWidget(self.label_1046)

        self.label_1047 = QLabel(self.frame_168)
        self.label_1047.setObjectName(u"label_1047")
        self.label_1047.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_339.addWidget(self.label_1047)

        self.horizontalSpacer_94 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_339.addItem(self.horizontalSpacer_94)

        self.doubleSpinBox_53 = QDoubleSpinBox(self.frame_168)
        self.doubleSpinBox_53.setObjectName(u"doubleSpinBox_53")
        self.doubleSpinBox_53.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_53.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_339.addWidget(self.doubleSpinBox_53)

        self.label_1048 = QLabel(self.frame_168)
        self.label_1048.setObjectName(u"label_1048")
        self.label_1048.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_339.addWidget(self.label_1048)


        self.verticalLayout_6.addWidget(self.frame_168)

        self.frame_165 = QFrame(self.frame_34)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_505 = QLabel(self.frame_165)
        self.label_505.setObjectName(u"label_505")
        self.label_505.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_165.addWidget(self.label_505)

        self.label_506 = QLabel(self.frame_165)
        self.label_506.setObjectName(u"label_506")
        self.label_506.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_165.addWidget(self.label_506)

        self.horizontalSpacer_92 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_165.addItem(self.horizontalSpacer_92)

        self.doubleSpinBox_54 = QDoubleSpinBox(self.frame_165)
        self.doubleSpinBox_54.setObjectName(u"doubleSpinBox_54")
        self.doubleSpinBox_54.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_54.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_165.addWidget(self.doubleSpinBox_54)

        self.label_507 = QLabel(self.frame_165)
        self.label_507.setObjectName(u"label_507")
        self.label_507.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_165.addWidget(self.label_507)


        self.verticalLayout_6.addWidget(self.frame_165)

        self.frame_169 = QFrame(self.frame_34)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_340 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_340.setObjectName(u"horizontalLayout_340")
        self.label_1049 = QLabel(self.frame_169)
        self.label_1049.setObjectName(u"label_1049")
        self.label_1049.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_340.addWidget(self.label_1049)

        self.label_1050 = QLabel(self.frame_169)
        self.label_1050.setObjectName(u"label_1050")
        self.label_1050.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_340.addWidget(self.label_1050)

        self.horizontalSpacer_95 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_340.addItem(self.horizontalSpacer_95)

        self.timeEdit_19 = QTimeEdit(self.frame_169)
        self.timeEdit_19.setObjectName(u"timeEdit_19")
        self.timeEdit_19.setMinimumSize(QSize(150, 30))
        self.timeEdit_19.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_340.addWidget(self.timeEdit_19)

        self.label_1051 = QLabel(self.frame_169)
        self.label_1051.setObjectName(u"label_1051")
        self.label_1051.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_340.addWidget(self.label_1051)


        self.verticalLayout_6.addWidget(self.frame_169)

        self.frame_336 = QFrame(self.frame_34)
        self.frame_336.setObjectName(u"frame_336")
        self.frame_336.setFrameShape(QFrame.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_350 = QHBoxLayout(self.frame_336)
        self.horizontalLayout_350.setObjectName(u"horizontalLayout_350")
        self.label_1079 = QLabel(self.frame_336)
        self.label_1079.setObjectName(u"label_1079")
        self.label_1079.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_350.addWidget(self.label_1079)

        self.label_1080 = QLabel(self.frame_336)
        self.label_1080.setObjectName(u"label_1080")
        self.label_1080.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_350.addWidget(self.label_1080)

        self.horizontalSpacer_97 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_350.addItem(self.horizontalSpacer_97)

        self.doubleSpinBox_55 = QDoubleSpinBox(self.frame_336)
        self.doubleSpinBox_55.setObjectName(u"doubleSpinBox_55")
        self.doubleSpinBox_55.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_55.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_350.addWidget(self.doubleSpinBox_55)

        self.label_1081 = QLabel(self.frame_336)
        self.label_1081.setObjectName(u"label_1081")
        self.label_1081.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_350.addWidget(self.label_1081)


        self.verticalLayout_6.addWidget(self.frame_336)

        self.frame_341 = QFrame(self.frame_34)
        self.frame_341.setObjectName(u"frame_341")
        self.frame_341.setFrameShape(QFrame.StyledPanel)
        self.frame_341.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_351 = QHBoxLayout(self.frame_341)
        self.horizontalLayout_351.setObjectName(u"horizontalLayout_351")
        self.label_1082 = QLabel(self.frame_341)
        self.label_1082.setObjectName(u"label_1082")
        self.label_1082.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_351.addWidget(self.label_1082)

        self.label_1083 = QLabel(self.frame_341)
        self.label_1083.setObjectName(u"label_1083")
        self.label_1083.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_351.addWidget(self.label_1083)

        self.horizontalSpacer_98 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_351.addItem(self.horizontalSpacer_98)

        self.doubleSpinBox_56 = QDoubleSpinBox(self.frame_341)
        self.doubleSpinBox_56.setObjectName(u"doubleSpinBox_56")
        self.doubleSpinBox_56.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_56.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_351.addWidget(self.doubleSpinBox_56)

        self.label_1084 = QLabel(self.frame_341)
        self.label_1084.setObjectName(u"label_1084")
        self.label_1084.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_351.addWidget(self.label_1084)


        self.verticalLayout_6.addWidget(self.frame_341)

        self.frame_342 = QFrame(self.frame_34)
        self.frame_342.setObjectName(u"frame_342")
        self.frame_342.setFrameShape(QFrame.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_352 = QHBoxLayout(self.frame_342)
        self.horizontalLayout_352.setObjectName(u"horizontalLayout_352")
        self.label_1085 = QLabel(self.frame_342)
        self.label_1085.setObjectName(u"label_1085")
        self.label_1085.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_352.addWidget(self.label_1085)

        self.label_1086 = QLabel(self.frame_342)
        self.label_1086.setObjectName(u"label_1086")
        self.label_1086.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_352.addWidget(self.label_1086)

        self.horizontalSpacer_99 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_352.addItem(self.horizontalSpacer_99)

        self.timeEdit_59 = QTimeEdit(self.frame_342)
        self.timeEdit_59.setObjectName(u"timeEdit_59")
        self.timeEdit_59.setMinimumSize(QSize(150, 30))
        self.timeEdit_59.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_352.addWidget(self.timeEdit_59)

        self.label_1087 = QLabel(self.frame_342)
        self.label_1087.setObjectName(u"label_1087")
        self.label_1087.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_352.addWidget(self.label_1087)


        self.verticalLayout_6.addWidget(self.frame_342)

        self.frame_335 = QFrame(self.frame_34)
        self.frame_335.setObjectName(u"frame_335")
        self.frame_335.setFrameShape(QFrame.StyledPanel)
        self.frame_335.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_341 = QHBoxLayout(self.frame_335)
        self.horizontalLayout_341.setObjectName(u"horizontalLayout_341")
        self.label_1052 = QLabel(self.frame_335)
        self.label_1052.setObjectName(u"label_1052")
        self.label_1052.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_341.addWidget(self.label_1052)

        self.label_1053 = QLabel(self.frame_335)
        self.label_1053.setObjectName(u"label_1053")
        self.label_1053.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_341.addWidget(self.label_1053)

        self.horizontalSpacer_96 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_341.addItem(self.horizontalSpacer_96)

        self.doubleSpinBox_57 = QDoubleSpinBox(self.frame_335)
        self.doubleSpinBox_57.setObjectName(u"doubleSpinBox_57")
        self.doubleSpinBox_57.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_57.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_341.addWidget(self.doubleSpinBox_57)

        self.label_1054 = QLabel(self.frame_335)
        self.label_1054.setObjectName(u"label_1054")
        self.label_1054.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_341.addWidget(self.label_1054)


        self.verticalLayout_6.addWidget(self.frame_335)

        self.frame_343 = QFrame(self.frame_34)
        self.frame_343.setObjectName(u"frame_343")
        self.frame_343.setFrameShape(QFrame.StyledPanel)
        self.frame_343.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_354 = QHBoxLayout(self.frame_343)
        self.horizontalLayout_354.setObjectName(u"horizontalLayout_354")
        self.label_1091 = QLabel(self.frame_343)
        self.label_1091.setObjectName(u"label_1091")
        self.label_1091.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_354.addWidget(self.label_1091)

        self.label_1092 = QLabel(self.frame_343)
        self.label_1092.setObjectName(u"label_1092")
        self.label_1092.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_354.addWidget(self.label_1092)

        self.horizontalSpacer_101 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_354.addItem(self.horizontalSpacer_101)

        self.timeEdit_20 = QTimeEdit(self.frame_343)
        self.timeEdit_20.setObjectName(u"timeEdit_20")
        self.timeEdit_20.setMinimumSize(QSize(150, 30))
        self.timeEdit_20.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_354.addWidget(self.timeEdit_20)

        self.label_1093 = QLabel(self.frame_343)
        self.label_1093.setObjectName(u"label_1093")
        self.label_1093.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_354.addWidget(self.label_1093)


        self.verticalLayout_6.addWidget(self.frame_343)

        self.frame_352 = QFrame(self.frame_34)
        self.frame_352.setObjectName(u"frame_352")
        self.frame_352.setFrameShape(QFrame.StyledPanel)
        self.frame_352.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_358 = QHBoxLayout(self.frame_352)
        self.horizontalLayout_358.setObjectName(u"horizontalLayout_358")
        self.label_1103 = QLabel(self.frame_352)
        self.label_1103.setObjectName(u"label_1103")
        self.label_1103.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_358.addWidget(self.label_1103)

        self.label_1104 = QLabel(self.frame_352)
        self.label_1104.setObjectName(u"label_1104")
        self.label_1104.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_358.addWidget(self.label_1104)

        self.horizontalSpacer_105 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_358.addItem(self.horizontalSpacer_105)

        self.doubleSpinBox_58 = QDoubleSpinBox(self.frame_352)
        self.doubleSpinBox_58.setObjectName(u"doubleSpinBox_58")
        self.doubleSpinBox_58.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_58.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_358.addWidget(self.doubleSpinBox_58)

        self.label_1105 = QLabel(self.frame_352)
        self.label_1105.setObjectName(u"label_1105")
        self.label_1105.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_358.addWidget(self.label_1105)


        self.verticalLayout_6.addWidget(self.frame_352)

        self.frame_351 = QFrame(self.frame_34)
        self.frame_351.setObjectName(u"frame_351")
        self.frame_351.setFrameShape(QFrame.StyledPanel)
        self.frame_351.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_357 = QHBoxLayout(self.frame_351)
        self.horizontalLayout_357.setObjectName(u"horizontalLayout_357")
        self.label_1100 = QLabel(self.frame_351)
        self.label_1100.setObjectName(u"label_1100")
        self.label_1100.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_357.addWidget(self.label_1100)

        self.label_1101 = QLabel(self.frame_351)
        self.label_1101.setObjectName(u"label_1101")
        self.label_1101.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_357.addWidget(self.label_1101)

        self.horizontalSpacer_104 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_357.addItem(self.horizontalSpacer_104)

        self.doubleSpinBox_59 = QDoubleSpinBox(self.frame_351)
        self.doubleSpinBox_59.setObjectName(u"doubleSpinBox_59")
        self.doubleSpinBox_59.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_59.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_357.addWidget(self.doubleSpinBox_59)

        self.label_1102 = QLabel(self.frame_351)
        self.label_1102.setObjectName(u"label_1102")
        self.label_1102.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_357.addWidget(self.label_1102)


        self.verticalLayout_6.addWidget(self.frame_351)

        self.frame_353 = QFrame(self.frame_34)
        self.frame_353.setObjectName(u"frame_353")
        self.frame_353.setFrameShape(QFrame.StyledPanel)
        self.frame_353.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_359 = QHBoxLayout(self.frame_353)
        self.horizontalLayout_359.setObjectName(u"horizontalLayout_359")
        self.label_1106 = QLabel(self.frame_353)
        self.label_1106.setObjectName(u"label_1106")
        self.label_1106.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_359.addWidget(self.label_1106)

        self.label_1107 = QLabel(self.frame_353)
        self.label_1107.setObjectName(u"label_1107")
        self.label_1107.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_359.addWidget(self.label_1107)

        self.horizontalSpacer_106 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_359.addItem(self.horizontalSpacer_106)

        self.timeEdit_29 = QTimeEdit(self.frame_353)
        self.timeEdit_29.setObjectName(u"timeEdit_29")
        self.timeEdit_29.setMinimumSize(QSize(150, 30))
        self.timeEdit_29.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_359.addWidget(self.timeEdit_29)

        self.label_1108 = QLabel(self.frame_353)
        self.label_1108.setObjectName(u"label_1108")
        self.label_1108.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_359.addWidget(self.label_1108)


        self.verticalLayout_6.addWidget(self.frame_353)

        self.frame_350 = QFrame(self.frame_34)
        self.frame_350.setObjectName(u"frame_350")
        self.frame_350.setFrameShape(QFrame.StyledPanel)
        self.frame_350.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_356 = QHBoxLayout(self.frame_350)
        self.horizontalLayout_356.setObjectName(u"horizontalLayout_356")
        self.label_1097 = QLabel(self.frame_350)
        self.label_1097.setObjectName(u"label_1097")
        self.label_1097.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_356.addWidget(self.label_1097)

        self.label_1098 = QLabel(self.frame_350)
        self.label_1098.setObjectName(u"label_1098")
        self.label_1098.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_356.addWidget(self.label_1098)

        self.horizontalSpacer_103 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_356.addItem(self.horizontalSpacer_103)

        self.timeEdit_21 = QTimeEdit(self.frame_350)
        self.timeEdit_21.setObjectName(u"timeEdit_21")
        self.timeEdit_21.setMinimumSize(QSize(150, 30))
        self.timeEdit_21.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_356.addWidget(self.timeEdit_21)

        self.label_1099 = QLabel(self.frame_350)
        self.label_1099.setObjectName(u"label_1099")
        self.label_1099.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_356.addWidget(self.label_1099)


        self.verticalLayout_6.addWidget(self.frame_350)

        self.label_514 = QLabel(self.frame_34)
        self.label_514.setObjectName(u"label_514")
        self.label_514.setMinimumSize(QSize(0, 40))
        self.label_514.setStyleSheet(u"color: black;\n"
"font: 18pt \"Segoe UI\";\n"
"border-color: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.label_514.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_514)

        self.frame_357 = QFrame(self.frame_34)
        self.frame_357.setObjectName(u"frame_357")
        self.frame_357.setFrameShape(QFrame.StyledPanel)
        self.frame_357.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_374 = QHBoxLayout(self.frame_357)
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.label_1154 = QLabel(self.frame_357)
        self.label_1154.setObjectName(u"label_1154")
        self.label_1154.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_374.addWidget(self.label_1154)

        self.label_1155 = QLabel(self.frame_357)
        self.label_1155.setObjectName(u"label_1155")
        self.label_1155.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_374.addWidget(self.label_1155)

        self.horizontalSpacer_115 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_374.addItem(self.horizontalSpacer_115)

        self.doubleSpinBox_60 = QDoubleSpinBox(self.frame_357)
        self.doubleSpinBox_60.setObjectName(u"doubleSpinBox_60")
        self.doubleSpinBox_60.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_60.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_374.addWidget(self.doubleSpinBox_60)

        self.label_1144 = QLabel(self.frame_357)
        self.label_1144.setObjectName(u"label_1144")
        self.label_1144.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_374.addWidget(self.label_1144)


        self.verticalLayout_6.addWidget(self.frame_357)

        self.frame_359 = QFrame(self.frame_34)
        self.frame_359.setObjectName(u"frame_359")
        self.frame_359.setFrameShape(QFrame.StyledPanel)
        self.frame_359.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_376 = QHBoxLayout(self.frame_359)
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.label_1160 = QLabel(self.frame_359)
        self.label_1160.setObjectName(u"label_1160")
        self.label_1160.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_376.addWidget(self.label_1160)

        self.label_1161 = QLabel(self.frame_359)
        self.label_1161.setObjectName(u"label_1161")
        self.label_1161.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_376.addWidget(self.label_1161)

        self.horizontalSpacer_117 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_376.addItem(self.horizontalSpacer_117)

        self.doubleSpinBox_61 = QDoubleSpinBox(self.frame_359)
        self.doubleSpinBox_61.setObjectName(u"doubleSpinBox_61")
        self.doubleSpinBox_61.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_61.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_376.addWidget(self.doubleSpinBox_61)

        self.label_1147 = QLabel(self.frame_359)
        self.label_1147.setObjectName(u"label_1147")
        self.label_1147.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_376.addWidget(self.label_1147)


        self.verticalLayout_6.addWidget(self.frame_359)

        self.frame_358 = QFrame(self.frame_34)
        self.frame_358.setObjectName(u"frame_358")
        self.frame_358.setFrameShape(QFrame.StyledPanel)
        self.frame_358.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_375 = QHBoxLayout(self.frame_358)
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.label_1157 = QLabel(self.frame_358)
        self.label_1157.setObjectName(u"label_1157")
        self.label_1157.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_375.addWidget(self.label_1157)

        self.label_1158 = QLabel(self.frame_358)
        self.label_1158.setObjectName(u"label_1158")
        self.label_1158.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_375.addWidget(self.label_1158)

        self.horizontalSpacer_116 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_375.addItem(self.horizontalSpacer_116)

        self.timeEdit_30 = QTimeEdit(self.frame_358)
        self.timeEdit_30.setObjectName(u"timeEdit_30")
        self.timeEdit_30.setMinimumSize(QSize(150, 30))
        self.timeEdit_30.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_375.addWidget(self.timeEdit_30)

        self.label_1148 = QLabel(self.frame_358)
        self.label_1148.setObjectName(u"label_1148")
        self.label_1148.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_375.addWidget(self.label_1148)


        self.verticalLayout_6.addWidget(self.frame_358)

        self.frame_354 = QFrame(self.frame_34)
        self.frame_354.setObjectName(u"frame_354")
        self.frame_354.setFrameShape(QFrame.StyledPanel)
        self.frame_354.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_370 = QHBoxLayout(self.frame_354)
        self.horizontalLayout_370.setObjectName(u"horizontalLayout_370")
        self.label_1111 = QLabel(self.frame_354)
        self.label_1111.setObjectName(u"label_1111")
        self.label_1111.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_370.addWidget(self.label_1111)

        self.label_1143 = QLabel(self.frame_354)
        self.label_1143.setObjectName(u"label_1143")
        self.label_1143.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_370.addWidget(self.label_1143)

        self.horizontalSpacer_111 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_370.addItem(self.horizontalSpacer_111)

        self.doubleSpinBox_64 = QDoubleSpinBox(self.frame_354)
        self.doubleSpinBox_64.setObjectName(u"doubleSpinBox_64")
        self.doubleSpinBox_64.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_64.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_370.addWidget(self.doubleSpinBox_64)

        self.label_1149 = QLabel(self.frame_354)
        self.label_1149.setObjectName(u"label_1149")
        self.label_1149.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_370.addWidget(self.label_1149)


        self.verticalLayout_6.addWidget(self.frame_354)

        self.frame_355 = QFrame(self.frame_34)
        self.frame_355.setObjectName(u"frame_355")
        self.frame_355.setFrameShape(QFrame.StyledPanel)
        self.frame_355.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_371 = QHBoxLayout(self.frame_355)
        self.horizontalLayout_371.setObjectName(u"horizontalLayout_371")
        self.label_1145 = QLabel(self.frame_355)
        self.label_1145.setObjectName(u"label_1145")
        self.label_1145.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_371.addWidget(self.label_1145)

        self.label_1146 = QLabel(self.frame_355)
        self.label_1146.setObjectName(u"label_1146")
        self.label_1146.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_371.addWidget(self.label_1146)

        self.horizontalSpacer_112 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_371.addItem(self.horizontalSpacer_112)

        self.doubleSpinBox_65 = QDoubleSpinBox(self.frame_355)
        self.doubleSpinBox_65.setObjectName(u"doubleSpinBox_65")
        self.doubleSpinBox_65.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_65.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_371.addWidget(self.doubleSpinBox_65)

        self.label_1150 = QLabel(self.frame_355)
        self.label_1150.setObjectName(u"label_1150")
        self.label_1150.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_371.addWidget(self.label_1150)


        self.verticalLayout_6.addWidget(self.frame_355)

        self.frame_356 = QFrame(self.frame_34)
        self.frame_356.setObjectName(u"frame_356")
        self.frame_356.setFrameShape(QFrame.StyledPanel)
        self.frame_356.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_373 = QHBoxLayout(self.frame_356)
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.label_1151 = QLabel(self.frame_356)
        self.label_1151.setObjectName(u"label_1151")
        self.label_1151.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_373.addWidget(self.label_1151)

        self.label_1152 = QLabel(self.frame_356)
        self.label_1152.setObjectName(u"label_1152")
        self.label_1152.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_373.addWidget(self.label_1152)

        self.horizontalSpacer_114 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_373.addItem(self.horizontalSpacer_114)

        self.timeEdit_31 = QTimeEdit(self.frame_356)
        self.timeEdit_31.setObjectName(u"timeEdit_31")
        self.timeEdit_31.setMinimumSize(QSize(150, 30))
        self.timeEdit_31.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"font: 18pt \"Segoe UI\";")

        self.horizontalLayout_373.addWidget(self.timeEdit_31)

        self.label_1153 = QLabel(self.frame_356)
        self.label_1153.setObjectName(u"label_1153")
        self.label_1153.setStyleSheet(u"color: black;\n"
"font: 12pt \"Segoe UI\";")

        self.horizontalLayout_373.addWidget(self.label_1153)


        self.verticalLayout_6.addWidget(self.frame_356)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.action_bar_frame_2 = QFrame(self.content_frame)
        self.action_bar_frame_2.setObjectName(u"action_bar_frame_2")
        self.action_bar_frame_2.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.action_bar_frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.edit_button_3 = QPushButton(self.action_bar_frame_2)
        self.edit_button_3.setObjectName(u"edit_button_3")
        self.edit_button_3.setMinimumSize(QSize(150, 30))
        self.edit_button_3.setFont(font)
        self.edit_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color : #007BFF;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon4 = QIcon()
        icon4.addFile(u"../../pys6-recipes-organizer/assets/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button_3.setIcon(icon4)
        self.edit_button_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.edit_button_3)


        self.verticalLayout_4.addWidget(self.action_bar_frame_2)

        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Recetas", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"16. ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"17. ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation Pressure:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"18. ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gas Interlock Pressure:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"19. ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"20. ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"21.", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"22.", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Slow Increment Termination Pressure:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Print Interval: ", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"LEAK TEST", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Leak Test Time:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Leak Test Tolerance:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Print Interval: ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"INTER DILUTION ", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"# Of Dilution Cycles:", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Inert Gas Pressure:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Inert Pressure Increment:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Inert Time Increment:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Inert Fast Increment Tolerance:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pressure Increment:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Vacuum Time Increment:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Vacuum Fast Inc Tolerance:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"INHG", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Vacuum Slow Inc Termination Pressure:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation pressure:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Hi Pressure:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"HUMIDIFICATION", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"RECIPE", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"7.", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_239.setText("")
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"8.", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Sterilant Selection:", None))
        self.label_252.setText("")
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"9.", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Temperature Setpoint:", None))
        self.label_242.setText("")
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"10.", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Jacket Differential Offset:", None))
        self.label_246.setText("")
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"11.", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"Maximum Temperature:", None))
        self.label_249.setText("")
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"12.", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Hi Temperature Tolerance:", None))
        self.label_255.setText("")
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"13.", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"Lo Temperature Tolerance:", None))
        self.label_258.setText("")
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"14.", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Cycle Start Temperature Tolerance:", None))
        self.label_261.setText("")
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"15. ", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Pressure Units:", None))
        self.label_264.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"VACCUM", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"16. ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"17. ", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation Pressure:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"18. ", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Gas Interlock Pressure:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"19. ", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"20. ", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"21.", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"22.", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Slow Increment Termination Pressure:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"23.", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Print Interval: ", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"LEAK TEST", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"24.", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Leak Test Time:", None))
        self.timeEdit_22.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm ", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"25.", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Leak Test Tolerance:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"26.", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Print Interval: ", None))
        self.timeEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"INTER DILUTION ", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"27.", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"# Of Dilution Cycles:", None))
        self.label_133.setText("")
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"28.", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Inert Gas Pressure:", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"29.", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Inert Pressure Increment:", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"INHG  ", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"30.", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Inert Time Increment:", None))
        self.timeEdit_4.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"31.", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Inert Fast Increment Tolerance:", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"32.", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"33.", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pressure Increment:", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"34.", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Vacuum Time Increment:", None))
        self.timeEdit_5.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"35.", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Vacuum Fast Inc Tolerance:", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"36.", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Vacuum Slow Inc Termination Pressure:", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"37.", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation pressure:", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"38.", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Hi Pressure:", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"39.", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_6.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"HUMIDIFICATION", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"40.", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.label_173.setText("")
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"41.", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Pressure Rise:", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"42.", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"43.", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.timeEdit_7.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"44.", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"45.", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Maximum Time:", None))
        self.timeEdit_8.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"46.", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_9.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"HUMIDIFICATION DWELL", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"47.", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.label_195.setText("")
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"48.", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Control Pressure:", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"49.", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Control Differential:", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"50.", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Hi Humidity:", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"51.", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Lo Humidity:", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"52.", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Maximum Humidity:", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"53.", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Dwell Time:", None))
        self.timeEdit_24.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"54.", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_23.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"GAS", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"55.", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Gas Pressure:", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"56.", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"57.", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.timeEdit_10.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"58.", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"59.", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_11.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"60.", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Gas by Weight:", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"LBS      ", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"GAS DWELL", None))
        self.label_416.setText(QCoreApplication.translate("MainWindow", u"61.", None))
        self.label_417.setText(QCoreApplication.translate("MainWindow", u"Control Pressure:", None))
        self.label_418.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_419.setText(QCoreApplication.translate("MainWindow", u"62.", None))
        self.label_420.setText(QCoreApplication.translate("MainWindow", u"Control Differential:", None))
        self.label_421.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_422.setText(QCoreApplication.translate("MainWindow", u"63.", None))
        self.label_423.setText(QCoreApplication.translate("MainWindow", u"Dwell Time:", None))
        self.timeEdit_34.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_515.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_434.setText(QCoreApplication.translate("MainWindow", u"64.", None))
        self.label_435.setText(QCoreApplication.translate("MainWindow", u"Maximum # Makeups", None))
        self.label_425.setText(QCoreApplication.translate("MainWindow", u"65.", None))
        self.label_426.setText(QCoreApplication.translate("MainWindow", u"Long Exposure:", None))
        self.timeEdit_12.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_517.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_428.setText(QCoreApplication.translate("MainWindow", u"66.", None))
        self.label_429.setText(QCoreApplication.translate("MainWindow", u"Short Exposure:", None))
        self.timeEdit_35.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_518.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_431.setText(QCoreApplication.translate("MainWindow", u"67.", None))
        self.label_432.setText(QCoreApplication.translate("MainWindow", u"Hi Pressure:", None))
        self.label_424.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_437.setText(QCoreApplication.translate("MainWindow", u"68.", None))
        self.label_438.setText(QCoreApplication.translate("MainWindow", u"Lo Pressure:", None))
        self.label_427.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_446.setText(QCoreApplication.translate("MainWindow", u"68.", None))
        self.label_449.setText(QCoreApplication.translate("MainWindow", u"Hi Pressure Abort:", None))
        self.label_430.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_484.setText(QCoreApplication.translate("MainWindow", u"68.", None))
        self.label_485.setText(QCoreApplication.translate("MainWindow", u"Emission Control Lead Time:", None))
        self.timeEdit_33.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_516.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_440.setText(QCoreApplication.translate("MainWindow", u"69.", None))
        self.label_441.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_13.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_442.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_1112.setText(QCoreApplication.translate("MainWindow", u"AFTER VACUUM", None))
        self.label_444.setText(QCoreApplication.translate("MainWindow", u"70.", None))
        self.label_445.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_1138.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_1113.setText(QCoreApplication.translate("MainWindow", u"71.", None))
        self.label_1114.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation Pressure:", None))
        self.label_1137.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_1116.setText(QCoreApplication.translate("MainWindow", u"72.", None))
        self.label_1117.setText(QCoreApplication.translate("MainWindow", u"Air Interlock Pressure:", None))
        self.label_1118.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_1119.setText(QCoreApplication.translate("MainWindow", u"73.", None))
        self.label_1120.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_1121.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_1122.setText(QCoreApplication.translate("MainWindow", u"74.", None))
        self.label_1123.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.timeEdit_14.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1124.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_1125.setText(QCoreApplication.translate("MainWindow", u"75.", None))
        self.label_1126.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_1127.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_1128.setText(QCoreApplication.translate("MainWindow", u"76.", None))
        self.label_1129.setText(QCoreApplication.translate("MainWindow", u"Slow Increment Termination Pressure:", None))
        self.label_1130.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_1131.setText(QCoreApplication.translate("MainWindow", u"77.", None))
        self.label_1132.setText(QCoreApplication.translate("MainWindow", u"Vacumm Hold Time:", None))
        self.timeEdit_26.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_1133.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_1134.setText(QCoreApplication.translate("MainWindow", u"78.", None))
        self.label_1135.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_15.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1136.setText(QCoreApplication.translate("MainWindow", u" MM:SS", None))
        self.label_443.setText(QCoreApplication.translate("MainWindow", u"GAS WASH A ", None))
        self.label_1109.setText(QCoreApplication.translate("MainWindow", u"79.", None))
        self.label_1110.setText(QCoreApplication.translate("MainWindow", u"#Of Wash Cycles:", None))
        self.label_1142.setText("")
        self.label_447.setText(QCoreApplication.translate("MainWindow", u"80.", None))
        self.label_448.setText(QCoreApplication.translate("MainWindow", u"Release Type:", None))
        self.label_1141.setText("")
        self.label_450.setText(QCoreApplication.translate("MainWindow", u"81.", None))
        self.label_451.setText(QCoreApplication.translate("MainWindow", u"Release Pressure:", None))
        self.label_452.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_453.setText(QCoreApplication.translate("MainWindow", u"82.", None))
        self.label_454.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_455.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_456.setText(QCoreApplication.translate("MainWindow", u"83.", None))
        self.label_457.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation Pressure:", None))
        self.label_458.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_459.setText(QCoreApplication.translate("MainWindow", u"84.", None))
        self.label_460.setText(QCoreApplication.translate("MainWindow", u"Hi pressure:", None))
        self.label_461.setText(QCoreApplication.translate("MainWindow", u"INHGA", None))
        self.label_462.setText(QCoreApplication.translate("MainWindow", u"85.", None))
        self.label_463.setText(QCoreApplication.translate("MainWindow", u"Release Pressure Increment:", None))
        self.label_464.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_465.setText(QCoreApplication.translate("MainWindow", u"86.", None))
        self.label_466.setText(QCoreApplication.translate("MainWindow", u"Release Time Increment:", None))
        self.timeEdit_16.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_467.setText(QCoreApplication.translate("MainWindow", u"MM:SS", None))
        self.label_468.setText(QCoreApplication.translate("MainWindow", u"87.", None))
        self.label_469.setText(QCoreApplication.translate("MainWindow", u"Release Fast Inc Tolerance:", None))
        self.label_470.setText(QCoreApplication.translate("MainWindow", u"INHG   ", None))
        self.label_471.setText(QCoreApplication.translate("MainWindow", u"88.", None))
        self.label_472.setText(QCoreApplication.translate("MainWindow", u"Release Slow Increment Termination Pressure:", None))
        self.label_473.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_474.setText(QCoreApplication.translate("MainWindow", u"89.", None))
        self.label_475.setText(QCoreApplication.translate("MainWindow", u"Release Hold Time:", None))
        self.timeEdit_27.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_476.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_480.setText(QCoreApplication.translate("MainWindow", u"90.", None))
        self.label_481.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pressure Increment:", None))
        self.label_482.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_486.setText(QCoreApplication.translate("MainWindow", u"91.", None))
        self.label_487.setText(QCoreApplication.translate("MainWindow", u"Vacuum Time Increment:", None))
        self.timeEdit_17.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_488.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_489.setText(QCoreApplication.translate("MainWindow", u"92.", None))
        self.label_490.setText(QCoreApplication.translate("MainWindow", u"Vacuum Fast Inc Tolerance:", None))
        self.label_491.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_492.setText(QCoreApplication.translate("MainWindow", u"93.", None))
        self.label_493.setText(QCoreApplication.translate("MainWindow", u"Vacuum Slow Increment Termination Pressure:", None))
        self.label_494.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_495.setText(QCoreApplication.translate("MainWindow", u"94.", None))
        self.label_496.setText(QCoreApplication.translate("MainWindow", u"Vacuum Hold Time:", None))
        self.timeEdit_28.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.label_497.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_508.setText(QCoreApplication.translate("MainWindow", u"95.", None))
        self.label_509.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_18.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_510.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_504.setText(QCoreApplication.translate("MainWindow", u"GAS WASH B ", None))
        self.label_1115.setText(QCoreApplication.translate("MainWindow", u"96.", None))
        self.label_1139.setText(QCoreApplication.translate("MainWindow", u"#Of Wash Cycles:", None))
        self.label_1140.setText("")
        self.label_511.setText(QCoreApplication.translate("MainWindow", u"97.", None))
        self.label_512.setText(QCoreApplication.translate("MainWindow", u"Release Type:", None))
        self.label_513.setText("")
        self.label_477.setText(QCoreApplication.translate("MainWindow", u"98.", None))
        self.label_478.setText(QCoreApplication.translate("MainWindow", u"Release Pressure:", None))
        self.label_479.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_501.setText(QCoreApplication.translate("MainWindow", u"99.", None))
        self.label_502.setText(QCoreApplication.translate("MainWindow", u"Evacuation Pressure:", None))
        self.label_503.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_498.setText(QCoreApplication.translate("MainWindow", u"100.", None))
        self.label_499.setText(QCoreApplication.translate("MainWindow", u"Anti-cavitation Pressure:", None))
        self.label_500.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_1046.setText(QCoreApplication.translate("MainWindow", u"101.", None))
        self.label_1047.setText(QCoreApplication.translate("MainWindow", u"Hi pressure:", None))
        self.label_1048.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_505.setText(QCoreApplication.translate("MainWindow", u"102.", None))
        self.label_506.setText(QCoreApplication.translate("MainWindow", u"Release Pressure Increment:", None))
        self.label_507.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_1049.setText(QCoreApplication.translate("MainWindow", u"103.", None))
        self.label_1050.setText(QCoreApplication.translate("MainWindow", u"Release Time Increment:", None))
        self.timeEdit_19.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1051.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_1079.setText(QCoreApplication.translate("MainWindow", u"104.", None))
        self.label_1080.setText(QCoreApplication.translate("MainWindow", u"Release Fast Inc Tolerance:", None))
        self.label_1081.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_1082.setText(QCoreApplication.translate("MainWindow", u"105.", None))
        self.label_1083.setText(QCoreApplication.translate("MainWindow", u"Release Slow Increment Termination Pressure:", None))
        self.label_1084.setText(QCoreApplication.translate("MainWindow", u"INHGA ", None))
        self.label_1085.setText(QCoreApplication.translate("MainWindow", u"106", None))
        self.label_1086.setText(QCoreApplication.translate("MainWindow", u"Release Hold Time:", None))
        self.timeEdit_59.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm  ", None))
        self.label_1087.setText(QCoreApplication.translate("MainWindow", u"HH:MM", None))
        self.label_1052.setText(QCoreApplication.translate("MainWindow", u"107.", None))
        self.label_1053.setText(QCoreApplication.translate("MainWindow", u"Vacuum Pressure Increment:", None))
        self.label_1054.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_1091.setText(QCoreApplication.translate("MainWindow", u"108.", None))
        self.label_1092.setText(QCoreApplication.translate("MainWindow", u"Vacuum Time Increment:", None))
        self.timeEdit_20.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1093.setText(QCoreApplication.translate("MainWindow", u"MM:SS ", None))
        self.label_1103.setText(QCoreApplication.translate("MainWindow", u"109.", None))
        self.label_1104.setText(QCoreApplication.translate("MainWindow", u"Vacuum Fast Inc Tolerance:", None))
        self.label_1105.setText(QCoreApplication.translate("MainWindow", u"INHG    ", None))
        self.label_1100.setText(QCoreApplication.translate("MainWindow", u"110.", None))
        self.label_1101.setText(QCoreApplication.translate("MainWindow", u"Vacuum Slow Increment Termination Pressure:", None))
        self.label_1102.setText(QCoreApplication.translate("MainWindow", u"INHGA  ", None))
        self.label_1106.setText(QCoreApplication.translate("MainWindow", u"111.", None))
        self.label_1107.setText(QCoreApplication.translate("MainWindow", u"Vacuum Hold Time:", None))
        self.timeEdit_29.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm  ", None))
        self.label_1108.setText(QCoreApplication.translate("MainWindow", u"HH:MM ", None))
        self.label_1097.setText(QCoreApplication.translate("MainWindow", u"112.", None))
        self.label_1098.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_21.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1099.setText(QCoreApplication.translate("MainWindow", u"MM:SS  ", None))
        self.label_514.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label_1154.setText(QCoreApplication.translate("MainWindow", u"113.", None))
        self.label_1155.setText(QCoreApplication.translate("MainWindow", u"Release Pressure:", None))
        self.label_1144.setText(QCoreApplication.translate("MainWindow", u"INHGA  ", None))
        self.label_1160.setText(QCoreApplication.translate("MainWindow", u"114.", None))
        self.label_1161.setText(QCoreApplication.translate("MainWindow", u"Pressure Increment:", None))
        self.label_1147.setText(QCoreApplication.translate("MainWindow", u"INHGA  ", None))
        self.label_1157.setText(QCoreApplication.translate("MainWindow", u"115.", None))
        self.label_1158.setText(QCoreApplication.translate("MainWindow", u"Time Increment:", None))
        self.timeEdit_30.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1148.setText(QCoreApplication.translate("MainWindow", u"MM:SS  ", None))
        self.label_1111.setText(QCoreApplication.translate("MainWindow", u"116.", None))
        self.label_1143.setText(QCoreApplication.translate("MainWindow", u"Fast Increment Tolerance:", None))
        self.label_1149.setText(QCoreApplication.translate("MainWindow", u"INHGA  ", None))
        self.label_1145.setText(QCoreApplication.translate("MainWindow", u"117.", None))
        self.label_1146.setText(QCoreApplication.translate("MainWindow", u"Slow Increment Termination Pressure:", None))
        self.label_1150.setText(QCoreApplication.translate("MainWindow", u"INHGA  ", None))
        self.label_1151.setText(QCoreApplication.translate("MainWindow", u"118.", None))
        self.label_1152.setText(QCoreApplication.translate("MainWindow", u"Print Interval:", None))
        self.timeEdit_31.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss  ", None))
        self.label_1153.setText(QCoreApplication.translate("MainWindow", u"MM:SS  ", None))
        self.edit_button_3.setText(QCoreApplication.translate("MainWindow", u"Guardar Receta", None))
    # retranslateUi

