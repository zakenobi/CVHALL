# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1280, 720)
        MainMenu.setStyleSheet("QMainWindow \n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(0, 60, 1000, 600)) #cam
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.image_label.setFont(font)
        self.image_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(35, 200, 120, 120))
        camIcon = QtGui.QIcon()
        camIcon.addPixmap(QtGui.QPixmap("resources/CamIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_button.setIcon(camIcon)
        self.start_button.setIconSize(QtCore.QSize(100,100))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setObjectName("start_button")
        self.start_button.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #FFF;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #FFF;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(35, 420, 120, 120))
        crossIcon = QtGui.QIcon()
        crossIcon.addPixmap(QtGui.QPixmap("resources/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(crossIcon)
        self.stop_button.setIconSize(QtCore.QSize(80,80))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.stop_button.setFont(font)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setStyleSheet("QPushButton{\n"
"font: 63 24pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #FFF;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #FFF;\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.stop_button.setObjectName("stop_button")
#         self.camera_list_label = QtWidgets.QLabel(self.centralwidget)
#         self.camera_list_label.setGeometry(QtCore.QRect(1440, 60, 371, 51))
#         font = QtGui.QFont()
#         font.setFamily("URW Gothic L")
#         font.setPointSize(22)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(7)
#         self.camera_list_label.setFont(font)
#         self.camera_list_label.setStyleSheet("border: transparent;\n"
# "background-color: transparent;\n"
# "color:#228B22;\n"
# "font: 63 22pt \"URW Gothic L\";")
#         self.camera_list_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.camera_list_label.setObjectName("camera_list_label")
        self.photo_taken_notification = QtWidgets.QLabel(self.centralwidget)
        self.photo_taken_notification.setEnabled(True)
        self.photo_taken_notification.setGeometry(QtCore.QRect(1200, 0, 420, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.photo_taken_notification.setFont(font)
        self.photo_taken_notification.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.photo_taken_notification.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #DA7720;\n"
"font: 63 24pt \"URW Gothic L\";")
        self.photo_taken_notification.setText("")
        self.photo_taken_notification.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_taken_notification.setObjectName("photo_taken_notification")
#         self.camera_table = QtWidgets.QTableWidget(self.centralwidget)
#         self.camera_table.setGeometry(QtCore.QRect(1440, 120, 381, 871))
#         palette = QtGui.QPalette()
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(210, 105, 30))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
#         self.camera_table.setPalette(palette)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.camera_table.setFont(font)
#         self.camera_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.camera_table.setFocusPolicy(QtCore.Qt.StrongFocus)
#         self.camera_table.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
#         self.camera_table.setAutoFillBackground(False)
#         self.camera_table.setStyleSheet("QTableWidget {\n"
# "color:#D2691E;\n"
# "gridline-color: rgb(0, 170, 0);\n"
# "background-color: rgb(20, 30, 60);\n"
# "hover {background-color: #1E90FF;}\n"
# "}\n"
# "\n"
# "QHeaderView::section { \n"
# "border-bottom: 1px solid green;\n"
# "gridline-color: rgb(0, 170, 0);\n"
# "background-color: rgb(6, 34, 50);\n"
# " }\n"
# "")
#         self.camera_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.camera_table.setFrameShadow(QtWidgets.QFrame.Plain)
#         self.camera_table.setLineWidth(1)
#         self.camera_table.setMidLineWidth(1)
#         self.camera_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
#         self.camera_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.camera_table.setAutoScrollMargin(20)
#         self.camera_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.camera_table.setDragDropOverwriteMode(False)
#         self.camera_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
#         self.camera_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.camera_table.setCornerButtonEnabled(False)
#         self.camera_table.setRowCount(0)
#         self.camera_table.setObjectName("camera_table")
#         self.camera_table.setColumnCount(2)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         font.setKerning(True)
#         item.setFont(font)
#         item.setBackground(QtGui.QColor(6, 34, 67))
#         brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.camera_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setTextAlignment(QtCore.Qt.AlignCenter)
#         font = QtGui.QFont()
#         font.setFamily("Gill Sans MT")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         item.setBackground(QtGui.QColor(6, 34, 68))
#         brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.camera_table.setHorizontalHeaderItem(1, item)
#         self.camera_table.horizontalHeader().setCascadingSectionResizes(False)
#         self.camera_table.horizontalHeader().setDefaultSectionSize(180)
#         self.camera_table.horizontalHeader().setHighlightSections(True)
#         self.camera_table.horizontalHeader().setMinimumSectionSize(40)
#         self.camera_table.horizontalHeader().setStretchLastSection(True)
#         self.camera_table.verticalHeader().setVisible(False)
#         self.camera_table.verticalHeader().setDefaultSectionSize(40)
#         self.camera_table.verticalHeader().setMinimumSectionSize(30)
#         self.camera_table.verticalHeader().setStretchLastSection(False)
        self.mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.mask_count_label.setEnabled(True)
        self.mask_count_label.setGeometry(QtCore.QRect(130, 80, 401, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.mask_count_label.setFont(font)
        self.mask_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mask_count_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.mask_count_label.setText("")
        self.mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mask_count_label.setIndent(10)
        self.mask_count_label.setObjectName("mask_count_label")
        self.no_mask_count_label = QtWidgets.QLabel(self.centralwidget)
        self.no_mask_count_label.setEnabled(True)
        self.no_mask_count_label.setGeometry(QtCore.QRect(530, 80, 431, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.no_mask_count_label.setFont(font)
        self.no_mask_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.no_mask_count_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.no_mask_count_label.setText("")
        self.no_mask_count_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.no_mask_count_label.setIndent(10)
        self.no_mask_count_label.setObjectName("no_mask_count_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setEnabled(True)
        self.status_label.setGeometry(QtCore.QRect(1000, 70, 141, 51))
        self.status_label.setScaledContents(True)
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.status_label.setFont(font)
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 24pt \"URW Gothic L\";")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setIndent(10)
        self.status_label.setObjectName("status_label")
        self.status_type_label = QtWidgets.QLabel(self.centralwidget)
        self.status_type_label.setEnabled(True)
        self.status_type_label.setGeometry(QtCore.QRect(1150, 70, 271, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.status_type_label.setFont(font)
        self.status_type_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_type_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"font: 63 24pt \"URW Gothic L\";")
        self.status_type_label.setText("")
        self.status_type_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.status_type_label.setIndent(10)
        self.status_type_label.setObjectName("status_type_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 0, 781, 62))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camera_select_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_select_label.setFont(font)
        self.camera_select_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_select_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color: #228B22;\n"
"font: 32pt \"Gill Sans MT\";")
        #self.camera_select_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.camera_select_label.move(10,170)
        
        self.camera_select_label.setObjectName("camera_select_label")
        self.horizontalLayout.addWidget(self.camera_select_label)
        self.camera_select = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_select.sizePolicy().hasHeightForWidth())
        self.camera_select.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 76, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.503, 0.0, 0.503, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(190, 201, 184))
        gradient.setColorAt(0.511364, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.camera_select.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.camera_select.setFont(font)
        self.camera_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_select.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.camera_select.setStyleSheet("QComboBox\n"
"{\n"
"font: 14pt \"URW Gothic L\";\n"
"color: #3C4CAD;\n"
"border: 1px solid #D3D3D3;\n"
"background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.503, y2:1, stop:0 rgba(190, 201, 184, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 0, 0);\n"
"border-radius: 16px;\n"
"padding: 1px 15px 1px 10px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0.52, y1:0, x2:0.503, y2:1, stop:0 rgba(143, 198, 118, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"border: 1px solid #D3D3D3;\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.503, y2:1, stop:0 rgba(190, 201, 184, 255), stop:0.511364 rgba(255, 255, 255, 255));\n"
"padding: 1px 15px 1px 10px;\n"
"}\n"
"\n"
"QComboBox::down-\n"
"{\n"
"padding: 10px 10px 5px 5px;\n"
" }\n"
"\n"
"QComboBox::down-arrow:on \n"
"{\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.camera_select.setCurrentText("")
        self.camera_select.setMaxVisibleItems(15)
        self.camera_select.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.camera_select.setObjectName("camera_select")
        self.horizontalLayout.addWidget(self.camera_select)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1880, 22))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.epf = QtWidgets.QLabel(self.centralwidget) # image
        self.epf.setGeometry(QtCore.QRect(0, 0, 195, 90)) 
        self.epf.setPixmap(QtGui.QPixmap("resources/Logo_EPF.png"))
        self.epf.setScaledContents(True)
        #self.epf.setIcon(QtGui.QIcon("resources/epf_logo.png"))
        #self.epf.setIconSize(QtCore.QSize(100,100))
        self.epf.setObjectName("epf")
     
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton1.setGeometry(QtCore.QRect(1050, 100, 200, 100))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton2.setGeometry(QtCore.QRect(1050, 300, 200, 100))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton3.setGeometry(QtCore.QRect(1050, 500, 200, 100))
        self.pushButton3.setObjectName("pushButton3")
    

        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(1050, 650, 80, 40))
        self.arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/LeftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setVisible(False)
        self.arrow.setEnabled(False)

        self.SArrowLeft = QtWidgets.QPushButton(self.centralwidget)
        self.SArrowLeft.setGeometry(QtCore.QRect(50, 600, 80, 40))
        self.SArrowLeft.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/SArrowLeft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SArrowLeft.setVisible(False)
        self.SArrowLeft.setEnabled(False)

        self.SArrowRight = QtWidgets.QPushButton(self.centralwidget)
        self.SArrowRight.setGeometry(QtCore.QRect(130, 600, 80, 40))
        self.SArrowRight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/SArrowRight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SArrowRight.setVisible(False)
        self.SArrowRight.setEnabled(False)

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(100, 200, 100, 70)) # texte de description
        str = open('resources/Description.txt', 'r').read()
        self.description.setText(str)
        self.description.setFont(QtGui.QFont('Arial', 45))
        self.description.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.description.adjustSize()
        self.description.setVisible(False)
        self.description.setEnabled(True)

        self.stats1 = QtWidgets.QLabel(self.centralwidget)
        self.stats1.setGeometry(QtCore.QRect(100, 200, 800, 1000)) 
        self.stats1.setText("stats 1")
        self.stats1.setFont(QtGui.QFont('Arial', 45))
        self.stats1.setStyleSheet("QLabel { background-color : white; color : black; }")
        self.stats1.adjustSize()
        self.stats1.setVisible(False)
        self.stats1.setEnabled(True)

        self.arrow.setIcon(icon)
        self.SArrowLeft.setIcon(icon2)
        self.SArrowRight.setIcon(icon3)
        self.arrow.setObjectName("pushButton")
        #self.arrow.setVisible(False) # par defaut la fleche est desactivee
        #self.arrow.setEnabled(False)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Face Mask Detector"))
        self.image_label.setText(_translate("MainMenu", "Select a Camera"))
        #self.start_button.setText(_translate("MainMenu", "START"))
        #self.stop_button.setText(_translate("MainMenu", "STOP"))
        #self.epf.setText(_translate("MainMenu", "Test"))
        #self.camera_list_label.setText(_translate("MainMenu", "Camera Control Panel"))
        #item = self.camera_table.horizontalHeaderItem(0)
        #item.setText(_translate("MainMenu", "Camera"))
        #item = self.camera_table.horizontalHeaderItem(1)
        #item.setText(_translate("MainMenu", "Status"))
        self.camera_select_label.setText(_translate("MainMenu", "Liste caméras:    "))
        self.camera_select.setProperty("placeholderText", _translate("MainMenu", "Select Camera"))
        self.camera_select.setVisible(False)
        self.camera_select_label.setVisible(False)

        #self.epf.setText(_translate("MainMenu","AAAAAA"))
        self.pushButton1.setText(_translate("MainMenu", "Prendre photo"))
        self.pushButton2.setText(_translate("MainMenu", "Statistiques"))
        self.pushButton3.setText(_translate("MainMenu", "Description du \nprojet"))
        self.status_label.move(1050,60)

        self.pushButton1.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")

        self.pushButton2.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")

        self.pushButton3.setStyleSheet("QPushButton{\n"
"font: 63 28pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #000000;\n"
"border: transparent\n"
"}\n"
"\n"
"")