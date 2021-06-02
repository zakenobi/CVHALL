# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartMenu(object):
    def setupUi(self, StartMenu):
        StartMenu.setObjectName("StartMenu")
        StartMenu.resize(800, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartMenu.sizePolicy().hasHeightForWidth())
        StartMenu.setSizePolicy(sizePolicy)
        StartMenu.setStyleSheet("background-color: rgb(5, 23, 47);")
        self.centralwidget = QtWidgets.QWidget(StartMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_list_label = QtWidgets.QLabel(self.centralwidget)
        self.camera_list_label.setGeometry(QtCore.QRect(50, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.camera_list_label.setFont(font)
        self.camera_list_label.setStyleSheet("border: transparent;\n"
"background-color: transparent;\n"
"color:#228B22;\n"
"font: 75 38pt \"URW Gothic L\";\n"
"")
        self.camera_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_list_label.setObjectName("camera_list_label")
        self.add_cam_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_cam_button.setGeometry(QtCore.QRect(50, 510, 171, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.add_cam_button.setFont(font)
        self.add_cam_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_cam_button.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #228B22;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #006400;\n"
"border: transparent\n"
"}")
        self.add_cam_button.setObjectName("add_cam_button")
        self.main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_menu_button.setGeometry(QtCore.QRect(490, 230, 251, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.main_menu_button.setFont(font)
        self.main_menu_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_menu_button.setStyleSheet("QPushButton{\n"
"font: 75 26pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #228B22;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: #006400;\n"
"border: transparent\n"
"}")
        self.main_menu_button.setObjectName("main_menu_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(490, 320, 251, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.exit_button.setFont(font)
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setStyleSheet("QPushButton{\n"
"font: 75 26pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #8B0000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: rgb(121, 0, 0);\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.delete_cam_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_cam_button.setGeometry(QtCore.QRect(260, 510, 171, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.delete_cam_button.setFont(font)
        self.delete_cam_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_cam_button.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"URW Gothic L\";\n"
"border:1px transparent;\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"background-color: #8B0000;\n"
"border: transparent\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #fff;\n"
"background-color: rgb(121, 0, 0);\n"
"border: transparent\n"
"}\n"
"\n"
"")
        self.delete_cam_button.setObjectName("delete_cam_button")
        self.camera_table = QtWidgets.QTableWidget(self.centralwidget)
        self.camera_table.setGeometry(QtCore.QRect(50, 100, 381, 381))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 180, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 30, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 209, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.camera_table.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.camera_table.setFont(font)
        self.camera_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_table.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.camera_table.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.camera_table.setAutoFillBackground(False)
        self.camera_table.setStyleSheet("QTableWidget {\n"
"color: rgb(21, 180, 8);\n"
"background-color: rgb(20, 30, 60);\n"
"gridline-color: rgb(0, 170, 0);\n"
"selection-background-color: rgb(0, 0, 205);\n"
"hover {background-color: #f5f5f5;}\n"
"}\n"
"\n"
"QHeaderView::section { \n"
"border-bottom: 1px solid green;\n"
"gridline-color: rgb(0, 170, 0);\n"
"background-color: rgb(6, 34, 50);\n"
" }\n"
"")
        self.camera_table.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.camera_table.setLineWidth(1)
        self.camera_table.setMidLineWidth(1)
        self.camera_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.camera_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.camera_table.setAutoScrollMargin(20)
        self.camera_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.camera_table.setDragDropOverwriteMode(False)
        self.camera_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.camera_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.camera_table.setCornerButtonEnabled(False)
        self.camera_table.setRowCount(0)
        self.camera_table.setObjectName("camera_table")
        self.camera_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(6, 34, 67))
        brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.camera_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(6, 34, 68))
        brush = QtGui.QBrush(QtGui.QColor(20, 140, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.camera_table.setHorizontalHeaderItem(1, item)
        self.camera_table.horizontalHeader().setCascadingSectionResizes(False)
        self.camera_table.horizontalHeader().setDefaultSectionSize(180)
        self.camera_table.horizontalHeader().setHighlightSections(True)
        self.camera_table.horizontalHeader().setMinimumSectionSize(40)
        self.camera_table.horizontalHeader().setStretchLastSection(True)
        self.camera_table.verticalHeader().setVisible(False)
        self.camera_table.verticalHeader().setDefaultSectionSize(40)
        self.camera_table.verticalHeader().setMinimumSectionSize(30)
        self.camera_table.verticalHeader().setStretchLastSection(False)
        StartMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        StartMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartMenu)
        self.statusbar.setObjectName("statusbar")
        StartMenu.setStatusBar(self.statusbar)

        self.retranslateUi(StartMenu)
        QtCore.QMetaObject.connectSlotsByName(StartMenu)

    def retranslateUi(self, StartMenu):
        _translate = QtCore.QCoreApplication.translate
        StartMenu.setWindowTitle(_translate("StartMenu", "Face Mask Detector"))
        self.camera_list_label.setText(_translate("StartMenu", "Camera List"))
        self.add_cam_button.setText(_translate("StartMenu", "Add Camera"))
        self.main_menu_button.setText(_translate("StartMenu", "Main Menu"))
        self.exit_button.setText(_translate("StartMenu", "Exit"))
        self.delete_cam_button.setText(_translate("StartMenu", "Delete Camera"))
        item = self.camera_table.horizontalHeaderItem(0)
        item.setText(_translate("StartMenu", "Name"))
        item = self.camera_table.horizontalHeaderItem(1)
        item.setText(_translate("StartMenu", "ID"))

