import os
import sys
import cv2

import board
import busio
import adafruit_mlx90640

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from pathlib import Path
from matplotlib.pyplot import pie, axis, show, figure
#from matplotlib_venn import venn2
from pandas.core.frame import DataFrame

from mailer import Mailer
import numpy as np
from pathlib import Path
from datetime import datetime
from PyQt5.QtCore import QTimer, QRegExp, Qt
from PyQt5.QtGui import QImage, QPixmap, QColor, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox

from main_menu import *

LABELS = ["Masque", "Sans Masque"]
COLORS = [[0, 255, 0], [0, 0, 255]]
weightsPath = "yolo_utils/yolov4-tiny-mask.weights"
configPath = "yolo_utils/yolov4-tiny-mask.cfg"
photo_path = "photos"
camera_list_path = "resources/camera_list.txt"
connect_log_path = "resources/connect_history.log"

current_time=int(datetime.utcnow().timestamp())

i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
max_temp=37.6

nomask_total=0
mask_total=0

i=0
photo_dir = Path(photo_path)
photo_dir.mkdir(parents=True, exist_ok=True)
cam_list_filename = Path(camera_list_path)
cam_list_filename.touch(exist_ok=True)
connect_log_filename = Path(connect_log_path)
connect_log_filename.touch(exist_ok=True)

def get_temp():
    x=0
    frame = [0] * 768
    mlx.getFrame(frame)
    frame.sort()
    max_temp=frame[0]
    if max_temp>41:
        max_temp=frame[1]
    # while frame[-x]>41 :
    #     max_temp=frame[-x] 
    #     x+=1   

    #max_temp=float("{0:.2f}".format(max(frame)))
    return max_temp


# Tres imoprtant pour le reseau de neuronne
def create_detection_net(config_path, weights_path):
    net = cv2.dnn_DetectionModel(config_path, weights_path)
    net.setInputSize(416, 416)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    return net

# Tres important pour obtenir la detection de masque
def get_processed_image(img, net, confThreshold, nmsThreshold):
    global current_time
    global max_temp
    mask_count = 0
    nomask_count = 0
    global nomask_total
    global mask_total
    global i
    i+=1
    if i%50==0:
        max_temp=get_temp()
    
    classes, confidences, boxes = net.detect(img, confThreshold, nmsThreshold)#fonction de detection
    for cl, score, (left, top, width, height) in zip(classes, confidences, boxes):
        mask_count += (1 - cl[0])
        nomask_count += cl[0]
        start_point = (int(left), int(top)) #definie la taille et position du petit carre autour de la tete
        end_point = (int(left + width), int(top + height))
        color = COLORS[cl[0]] #definie la couleur du carre
        img = cv2.rectangle(img, start_point, end_point, color, 2)  #dessine le carre sur l'image 
        text = f'{LABELS[cl[0]]}: {score[0]:0.2f}'
        (test_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_ITALIC, 0.6, 1)
        end_point = (int(left + test_width + 2), int(top - text_height - 2))
        img = cv2.rectangle(img, start_point, end_point, color, -1)
        cv2.putText(img, text, start_point, cv2.FONT_ITALIC, 0.6, COLORS[1 - cl[0]], 1)  #ecrit les information de port du masque sur l'image
    
    img = cv2.rectangle(img,(200, 70),(450,350),(255,0,0),2)
    text = f'Temp : {max_temp}'
    cv2.putText(img, text, (200, 68), cv2.FONT_ITALIC, 0.6,(255, 0, 0),1)
    
    ratio = nomask_count / (mask_count + nomask_count + 0.000001)
    
    if ratio >= 0.1 and nomask_count >= 3: #
        status = "Danger"
    elif ratio != 0 and np.isnan(ratio) is not True:
        status = "Attention"
    else:
        status = "Pas de danger"
    
    if i%200==0:
        i=0
        nomask_total+=nomask_count
        mask_total+=mask_count
    if int(datetime.utcnow().timestamp())-current_time>=60:
        if nomask_total!=0 | mask_total!=0:
            with open('resources/data.csv','a') as fd:
                fd.write(f'\n{datetime.now().strftime("%d/%m/%Y")};{datetime.now().strftime("%H")};{mask_total};{nomask_total};')
            nomask_total=0
            mask_total=0
        current_time=int(datetime.utcnow().timestamp())

    return img, status, mask_count, nomask_count


class Camera(QTimer):
    def __init__(self, camName, camID, confThreshold=0.4, nmsThreshold=0.4):
        super().__init__()
        self.camName = camName
        self.camID = camID
        self.confThreshold = confThreshold
        self.nmsThreshold = nmsThreshold
        self.viewable = False
        self.status = "pas de connexion"
        self.prev_status = "pas de connexion"
        self.last_image = None
        self.camera_name_item = QTableWidgetItem(self.camName)
        self.camera_name_item.setTextAlignment(Qt.AlignCenter)
        self.camera_status_item = QTableWidgetItem(self.status)
        #self.camera_status_item.setTextAlignment(Qt.AlignCenter)
        self.cam = cv2.VideoCapture(self.camID)
        self.timeout.connect(self.camera_run)

    def start_camera(self):
        self.cam = cv2.VideoCapture(self.camID)
        self.cam.set(cv2.CAP_PROP_FPS, 30)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)#attribu optionnel
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 690) # taille max cam


    def take_photo(self):
        today = datetime.now().strftime("%d.%m.%Y")
        photo_dir_today = Path(os.path.join(photo_path, today, self.status))
        photo_dir_today.mkdir(parents=True, exist_ok=True)
        image_name = self.camName + "_" + datetime.now().strftime("%d.%m.%Y_%H") + ".jpg"
        cv2.imwrite(os.path.join(photo_dir_today, image_name), self.last_image)

    def view_disconnected_cam(self):
        mainMenu.ui.image_label.setStyleSheet("color: rgb(210, 105, 30);")
        mainMenu.ui.image_label.setText(self.camName + " pas de connexion")
        status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: rgb(210, 105, 30);"
        mainMenu.ui.image_label.setStyleSheet("color: rgb(210, 105, 30);")
        mainMenu.ui.image_label.setText(self.camName + " pas de connexion")
        mainMenu.ui.mask_count_label.setText("")
        mainMenu.ui.no_mask_count_label.setText("")
        mainMenu.ui.status_label.setText('Status:')
        mainMenu.ui.status_type_label.setText(self.status)
        mainMenu.ui.status_type_label.setStyleSheet(status_stylesheet)

    def camera_run(self):

        if self.status != "pas de connexion":
            try:
                ret, image = self.cam.read() #lecture de la camera
                self.last_image = image.copy()
                image, status, mask_count, nomask_count = get_processed_image(image, mainMenu.net, self.confThreshold, self.nmsThreshold) #recuperation de l'image avec la detection
                

                #self.nomask_total+=nomask_count
                #print(nomask_total)
                #print(datetime.now().strftime("%S"))
                #print(nomask_count)
                self.status = status
                if status == "Pas de danger": #changement de l'etat du text en fonction de l'etat de danger
                    self.camera_name_item.setForeground(QColor(21, 200, 8))
                    self.camera_status_item.setForeground(QColor(21, 200, 8))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: rgb(21, 200, 8);"
                elif status == "Attention":
                    self.camera_name_item.setForeground(QColor("yellow"))
                    self.camera_status_item.setForeground(QColor("yellow"))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: yellow;"
                else:
                    self.camera_name_item.setForeground(QColor("red"))
                    self.camera_status_item.setForeground(QColor("red"))
                    status_stylesheet = "border: transparent; background-color: transparent; font: 63 24pt \"URW Gothic L\"; color: red;"
                self.camera_status_item.setText(self.status)
                if self.viewable is True:
                    mainMenu.ui.image_label.setStyleSheet("color: rgb(255, 255, 255);")
                    mainMenu.ui.image_label.setText("")
                    mainMenu.ui.mask_count_label.setText(f'Avec masque:  {mask_count}')
                    mainMenu.ui.no_mask_count_label.setText(f'Sans masque:  {nomask_count}')
                    mainMenu.ui.status_label.setText('Status:')
                    mainMenu.ui.status_type_label.setText(status)
                    mainMenu.ui.status_type_label.setStyleSheet(status_stylesheet)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    height, width, channel = image.shape
                    step = channel * width
                    qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                    mainMenu.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
                    
        
            except:
                with open(connect_log_path, "a") as connect_log:
                    connect_log.write(datetime.now().strftime("%d/%m/%Y - %H ->\t") + self.camName + " (ID: " + str(self.camID) + ") disconnected from the system.\n\n")
                self.status = "Not Connected"
                self.camera_name_item.setForeground(QColor(210, 105, 30))
                self.camera_status_item.setForeground(QColor(210, 105, 30))
                self.camera_status_item.setText(self.status)
                self.cam.release()
                if self.viewable is True:
                    self.view_disconnected_cam()

        else:
            self.cam = cv2.VideoCapture(self.camID)
            if self.cam.isOpened() and self.cam.get(cv2.CAP_PROP_FPS) != 0:
                with open(connect_log_path, "a") as connect_log:
                    connect_log.write(datetime.now().strftime("%d/%m/%Y - %H ->\t") + self.camName + " (ID: " + str(self.camID) + ") connected to the system.\n\n")

                self.cam.set(cv2.CAP_PROP_FPS, 30)
                self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 690)
                self.status = "Safe"
            elif self.viewable is True:
                self.view_disconnected_cam()
        #automatically take a photo when the status of the camera switches to "Warning" or "Danger"

        # if self.prev_status == "Pas de danger" or self.prev_status == "pas de connexion":
        #     if self.status == "Attention" or self.status == "Danger":
        #         self.take_photo()
        #         self.send_email()
        # elif self.prev_status == "Attention" and self.status == "Danger":
        #     self.take_photo()
        #     self.send_email()
        # elif self.prev_status == "Danger" and self.status == "Attention":
        #     self.take_photo()
        #     self.send_email()
        # self.prev_status = self.status

    def send_email(self):
        mail = Mailer(email='cvhall.epf@gmail.com', password='PMFGE3A.23')
        mail.send(receiver='zac.gagnou@gmail.com', subject='ALERT', message='Individu dangereux demasquer !')


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('resources/medical-mask.ico'))
        self.net = create_detection_net(configPath, weightsPath) #creation de la fonction de detection
        self.camera_list = []
        self.current_camera = None
        self.ui.camera_select.activated.connect(self.change_cam)
        self.ui.pushButton1.clicked.connect(self.take_photo)
        
        #self.ui.pushButton1.clicked.connect(self.hide)
        #self.ui.pushButton1.clicked.connect(self.reveal)
        self.ui.arrow.clicked.connect(self.arrow)
        self.ui.pushButton2.clicked.connect(self.revealArrow)
        self.ui.pushButton2.clicked.connect(self.camCancel)
        self.ui.pushButton2.clicked.connect(self.revealStats)
        self.ui.pushButton3.clicked.connect(self.revealDesc)
        self.ui.pushButton3.clicked.connect(self.camCancel)
        self.ui.start_button.clicked.connect(self.cam)
        self.ui.stop_button.clicked.connect(self.camCancel)

        self.ui.SArrowLeft.clicked.connect(self.leftArrow)
        self.ui.SArrowRight.clicked.connect(self.rightArrow)

        self.camera_dict = {}
        self.get_camera_list_2(cam_list_filename)

    def get_camera_list(self):
        self.camera_list = []
        self.ui.camera_select.clear()
        #self.ui.camera_table.clearContents()
        #self.ui.camera_table.setRowCount(0)
        self.ui.image_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.ui.image_label.setText("")
        for camera in mainMenu.camera_dict:
            self.camera_list.append(Camera(camera, mainMenu.camera_dict[camera]))
        for camera in self.camera_list:
            self.ui.camera_select.addItem(camera.camName)
            #self.ui.camera_table.insertRow(self.ui.camera_table.rowCount())
            #current_row = self.ui.camera_table.rowCount() - 1
            #self.ui.camera_table.setItem(current_row, 0, camera.camera_name_item)
            #self.ui.camera_table.setItem(current_row, 1, camera.camera_status_item)

    def start_cameras(self):
        for camera in self.camera_list:
            camera.start_camera()
            camera.start(30)

    def stop_cameras(self):
        for camera in self.camera_list:
            camera.stop()
            camera.cam.release()

    def change_cam(self, i):
        self.current_camera = self.camera_list[i]
        for camera in self.camera_list:
            camera.viewable = False
        self.current_camera.viewable = True

    def take_photo(self):
        if self.current_camera is not None and self.current_camera.status != "pas de connexion":
            image_name = self.current_camera.camName + "_" + datetime.now().strftime("%d.%m.%Y_%H") + ".jpg"
            cv2.imwrite(os.path.join(photo_path, image_name), self.current_camera.last_image)
            QTimer.singleShot(0, lambda: self.ui.photo_taken_notification.setText("Photo prise!"))
        else:
            QTimer.singleShot(0, lambda: self.ui.photo_taken_notification.setText("Caméra non disponible!"))
        QTimer.singleShot(2000, lambda: self.ui.photo_taken_notification.setText(""))

    def close_app(self):
        self.stop_cameras()
        self.close()

    def insert_dict_in_table(self):
        for camera in self.camera_dict:
            cam_name = QTableWidgetItem(camera)
            cam_name.setTextAlignment(Qt.AlignCenter)
            cam_id = QTableWidgetItem(str(self.camera_dict[camera]))
            cam_id.setTextAlignment(Qt.AlignCenter)

    def get_camera_list_2(self, cam_list_filename):
        self.camera_dict = {}
        for cam_line in [cam_line.strip() for cam_line in open(cam_list_filename)]:
            if cam_line.split(" ")[1].isdigit():
                self.camera_dict[cam_line.split(" ")[0]] = int(cam_line.split(" ")[1])
            else:
                self.camera_dict[cam_line.split(" ")[0]] = cam_line.split(" ")[1]
        self.insert_dict_in_table()
    
    def reveal(self):
        self.ui.description.setVisible(False)
        self.ui.description.setEnabled(False)

    def hide(self):
        self.ui.pushButton1.setVisible(False)
        self.ui.pushButton1.setEnabled(False)

        self.ui.pushButton2.setVisible(False)
        self.ui.pushButton2.setEnabled(False)

        self.ui.pushButton3.setVisible(False)
        self.ui.pushButton3.setEnabled(False)

        self.ui.arrow.setVisible(True)
        self.ui.arrow.setEnabled(True)
    
    def arrow(self):
        self.ui.pushButton1.setVisible(True)
        self.ui.pushButton1.setEnabled(True)
        self.ui.pushButton2.setVisible(True)
        self.ui.pushButton2.setEnabled(True)
        self.ui.pushButton3.setVisible(True)
        self.ui.pushButton3.setEnabled(True)
        self.ui.description.setVisible(False)
        self.ui.arrow.setVisible(False)
        self.ui.arrow.setEnabled(False)
        self.ui.SArrowLeft.setVisible(False)
        self.ui.SArrowLeft.setEnabled(False)
        self.ui.SArrowRight.setVisible(False)
        self.ui.SArrowRight.setEnabled(False)
        self.ui.start_button.setVisible(True)
        self.ui.start_button.setEnabled(True)
        self.ui.stop_button.setVisible(True)
        self.ui.stop_button.setEnabled(True)
        self.ui.chart1.setVisible(False)
        self.ui.chart2.setVisible(False)

    def revealStats(self):
        path = ("resources/data.csv")
        df = pd.read_csv(path,sep=';',index_col=1)
        #dp = df[['Somme_avec_masques','Somme_non_masques']].iloc[[0]]

        # Pie

        #labels = [dp.iloc[0][0],dp.iloc[0][1]]

        sum_masque = df['nb_masques_bien_portes'].sum()
        sum_Nmasque = df['nb_masques_non_portes'].sum()

        #labels = [sum_masque,sum_Nmasque]

        #slices = [sum_masque,sum_Nmasque]

        # venn2(subsets= (sum_masque,sum_Nmasque,sum_Nmasque+sum_masque),set_labels=('Sans masque','Avec masque'))
        # plt.show()
        # plt.savefig("app/resources/Pie")

        # Histogramme 

        hours = df.groupby('Heures').agg('sum')
        hours = hours[['nb_masques_bien_portes','nb_masques_non_portes']]
        hours.plot.bar()
        plt2.title("Nombre de détections en fonction de l'heure")
        plt2.legend(["Masques bien portés","Masques mal portés"],loc = "upper right", facecolor = "lightgray")
        plt2.savefig("Histogram.png")

        file_size =Path(r"resources/data.csv").stat().st_size
        if file_size > pow(10,9) : 
            dc = DataFrame(columns=['Date','Heures','nb_masques_bien_portes','nb_masques_non_portes','Somme_avec_masques','Somme_non_masques'])
            dc.to_csv(r"resources/data.csv",  index = False, sep=';', encoding='utf-8')
    
        self.ui.chart1.setPixmap(QtGui.QPixmap("Pie.png"))
        self.ui.chart1.adjustSize()
        self.ui.chart1.setScaledContents(True)
        self.ui.chart2.setPixmap(QtGui.QPixmap("Histogram.png"))
        self.ui.chart2.adjustSize()
        self.ui.chart2.setScaledContents(True)
        self.ui.SArrowLeft.setVisible(False)
        self.ui.SArrowLeft.setEnabled(False)
        self.ui.SArrowRight.setVisible(True)
        self.ui.SArrowRight.setEnabled(True)
        self.ui.start_button.setVisible(False)
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setVisible(False)
        self.ui.stop_button.setEnabled(False)
        self.ui.description.setVisible(False)
        self.ui.chart1.setVisible(True)
        self.ui.chart2.setVisible(False)

        os.remove("Pie.png")
        os.remove("Histogram.png")
        df.drop(["nb_masques_bien_portes","nb_masques_non_portes"], axis = 1)

    def leftArrow(self):
        self.ui.chart1.setVisible(True)
        self.ui.chart2.setVisible(False)
        self.ui.SArrowRight.setVisible(True)
        self.ui.SArrowRight.setEnabled(True)
        self.ui.SArrowLeft.setVisible(False)
        self.ui.SArrowLeft.setEnabled(False)

    def rightArrow(self):
        self.ui.chart1.setVisible(False)
        self.ui.chart2.setVisible(True)
        self.ui.SArrowLeft.setVisible(True)
        self.ui.SArrowLeft.setEnabled(True)
        self.ui.SArrowRight.setVisible(False)
        self.ui.SArrowRight.setEnabled(False)

    
    def revealDesc(self):
        self.ui.description.setVisible(True)
        self.ui.arrow.setVisible(True)
        self.ui.arrow.setEnabled(True)
        self.ui.start_button.setVisible(False)
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setVisible(False)
        self.ui.stop_button.setEnabled(False)
        self.ui.SArrowLeft.setVisible(False)
        self.ui.SArrowLeft.setEnabled(False)
        self.ui.SArrowRight.setVisible(False)
        self.ui.SArrowRight.setEnabled(False)
        self.ui.chart1.setVisible(False)
        self.ui.chart2.setVisible(False)      

    def revealArrow(self):
        self.ui.arrow.setVisible(True)
        self.ui.arrow.setEnabled(True)

    def cam(self):
        mainMenu.start_cameras()
        mainMenu.change_cam(0)
        self.ui.image_label.setVisible(True)
        #self.ui.mask_count_label.setVisible(False)
        #self.ui.no_mask_count_label.setVisible(False)
        self.ui.status_type_label.setVisible(False)
    
    def camCancel(self):
        #mainMenu.change_cam(1)
        mainMenu.stop_cameras()
        self.ui.image_label.setVisible(False)
        #os.execv(sys.executable, ['python3'] + sys.argv)
        #mainMenu.close_app()
        #self.ui.mask_count_label.setVisible(False)
        #self.ui.no_mask_count_label.setVisible(False)
        #self.ui.status_type_label.setVisible(False)

    def timer(self):
        mainMenu.cam()
        import time

        max_time = 10
        start_time = time.time()
        while (time.time() - start_time) < max_time:
            Camera.camera_run()
    
        mainMenu.camCancel()
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = MainMenu()
    mainMenu.get_camera_list()
    mainMenu.showFullScreen()
    #mainMenu.start_cameras()

    sys.exit(app.exec_())