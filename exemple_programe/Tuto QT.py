import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MyWindow(QMainWindow): # cree une classe qui herite de QMainWindow
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,400,400) # definit la taille de la fenetre,  args = xpos, ypos, width, height
        self.setWindowTitle("CV Hall") # definit le titre
        self.initUI()

    def initUI(self): # la fonction initUI sert a contenir tout le code applique a la fenetre

        self.label = QtWidgets.QLabel(self) # cree un label dans la fenetre
        self.label.setText('Texte') # ajoute du texte au label
        self.label.move(50,50) # definit la position

        self.button1 = QtWidgets.QPushButton(self) # cree un bouton dans la fenetre win
        self.button1.setText("Click here")
        self.button1.move(100,200)
        self.button1.clicked.connect(self.clic) # lorsque l'evenement 'clicked' survient, appelle la fonction clic
    
    def clic(self): # cree une fonction que l'on declenchera lors du clic
        self.label.setText("Button pressed !") # modifie le texte
        self.update()
    
    def update(self): # fonction d'update que l'on appelera lorsqu'on modifie un texte
        self.label.adjustSize() # ajuste la taille des labels automatiquement


def window():
    app = QApplication(sys.argv) 
    win = MyWindow () # cree la fenetre principale
    win.show() 
    sys.exit(app.exec_())

window() # appelle la fonction et affiche la fenetre