# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720) # resolution de la fenetre principale
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget) # titre
        self.label.setGeometry(QtCore.QRect(500, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font) 
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget) # image
        self.label_2.setGeometry(QtCore.QRect(0, 100, 1280, 720)) 
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Interface QT Designer\epf_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # bouton 1
        self.pushButton.setGeometry(QtCore.QRect(900, 120, 250, 130))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) #bouton 2 
        self.pushButton_2.setGeometry(QtCore.QRect(900, 300, 250, 130))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget) # bouton 3
        self.pushButton_3.setGeometry(QtCore.QRect(900, 480, 250, 130))
        self.pushButton_3.setObjectName("pushButton_3")

        self.arrow = QtWidgets.QPushButton(self.centralwidget)  # bouton fleche
        self.arrow.setGeometry(QtCore.QRect(500, 600, 80, 40))
        self.arrow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface QT Designer\LeftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arrow.setIcon(icon)
        self.arrow.setObjectName("pushButton")
        self.arrow.setVisible(False) # par defaut la fleche est desactivee
        self.arrow.setEnabled(False)

        self.epf = QtWidgets.QLabel(self.centralwidget) # image
        self.epf.setGeometry(QtCore.QRect(200, 200, 331, 61)) 
        self.epf.setText("AAAAAA")
        self.epf.setPixmap(QtGui.QPixmap("resources/epf_logo.jpg"))
        self.epf.setScaledContents(True)
        self.epf.setObjectName("epf")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(550, 230, 100, 100)) # texte de description
        str = open('Interface QT Designer\Description.txt', 'r').read()
        self.description.setText(str)
        self.description.setFont(QtGui.QFont('Arial', 15))
        self.description.setStyleSheet("color: white")
        self.description.adjustSize()
        self.description.setVisible(False)
        self.description.setEnabled(True)

        MainWindow.setCentralWidget(self.centralwidget) # menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcut("")
        self.actionPaste.setObjectName("actionPaste")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CV Hall")) # label titre

        self.pushButton.setText(_translate("MainWindow", "Lancer la détéction")) # texte boutons
        self.pushButton.setFont(QtGui.QFont('Arial', 12))
        self.pushButton_2.setFont(QtGui.QFont('Arial', 12))
        self.pushButton_3.setFont(QtGui.QFont('Arial', 12))
        self.pushButton_2.setText(_translate("MainWindow", "Manuel Utilisateur"))
        self.pushButton_3.setText(_translate("MainWindow", "Description du projet"))
        #self.pushButton.adjustSize()
        #self.pushButton_2.adjustSize()
        #self.pushButton_3.adjustSize()

        self.label.setText(_translate("MainWindow", "CV Hall"))
        self.label.adjustSize() # ajuste la taille du label
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))    # menu et raccourcis
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow","Ctrl+V"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save your file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        
        # -- connexions --
        self.pushButton.clicked.connect(self.hide_fond)
        self.pushButton.clicked.connect(self.reveal_arrow)

        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.reveal_arrow)

        self.pushButton_3.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.reveal_arrow)
        self.pushButton_3.clicked.connect(self.reveal_info)

        self.arrow.clicked.connect(self.reveal)
        self.arrow.clicked.connect(self.hide_arrow) 
        self.arrow.clicked.connect(self.hide_info)       

        # -- fonctions --

    def hide(self): # fonction permettant de cacher et desactiver les boutons
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)

    def hide_fond(self): # cache les boutons et affiche le fond bleu uni
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.label_2.setPixmap(QtGui.QPixmap("Interface QT Designer\Wallpaper_fond.jpg"))
    
    def reveal_arrow(self): # permet de reveler la fleche de retour
        self.arrow.setVisible(True)
        self.arrow.setEnabled(True)

    def hide_arrow(self): # cache la fleche
        self.arrow.setVisible(False)
        self.arrow.setEnabled(False)
    
    def reveal(self): # permet d'affiher et reactiver les boutons d'accueil
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.label_2.setPixmap(QtGui.QPixmap("Interface QT Designer\Wallpaper.jpg"))
    
    def reveal_info(self): # affiche la description
        self.description.setVisible(True)
    def hide_info(self):
        self.description.setVisible(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())