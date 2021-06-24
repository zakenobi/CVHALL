# Projet Challenge EPF : FMDE (Face Mask Detection EPF)

  - [Project description and Context](#project-description-and-context)
  - [How to install](#how-to-install)
  - [User manual](#user-manual)
  - [A word on data collection](#a-word-on-data-collection)

-------
## Project description and Context
In the context of the COVID pandemy of 2020, public places have become sensitive spots where it is important to apply health measures, including wearing a mask. This project aims to provide a Python application able to detect if people wear their mask or not using AI and measure their body temperature using a thermal camera.
The application uses OpenCV and the Yolov4 algorithm for the detection and PyQt5 for the interface, it is designed to run on a Jetson Nano.
Here are the different functionalities supported by the application : 

* Face mask detection and display of a green square around the user if the mask is worn, a red one if it isn't
* Display of body temperature
* Collecting data (number and date of the different activations) and display of statistic charts 
* Display of the project description and user manual
* Sending emails in case of detection (functional but not implemented)
---------
## How to install 

To install the application please run the `install_dependencies_jetson_nano.sh` file, with these commands : 

```console
foo@bar:~$ sudo chmod +x install_dependencies_jetson_nano.sh`

foo@bar:~$ sudo ./install_dependencies_jetson_nano.sh`
```

 The following libraries will be installed : 

* PyQt5 
* OpenCV
* Pandas
* matplotlib
* numpy 
* adafruit
* pathlib
* mailer
* busio
  
---------

## User manual

To run the application, open the terminal and enter 
```console
python3 face_mask_detection.py
```

The interface is fairly easy to use, each button has a functionality : 
* The green camera button runs the camera and starts the mask detection
* The red button shuts down the camera
* The button titled 'Afficher température' displays a blue square on the screen where the maximum temperature is detected
* The button 'Statistiques' displays a bar plot generated in function of the data collected by the application, the proportion between the two types of detection (the mask is worn or not) is also displayed.
* The button 'Description du projet' displays the project description and a QR Code linked to a graphic user manual

The interface is made to fit a 1280 x 720 screen and is displayed in full screen by default. To exit the app, just press `alt+f4`.

-------
## A word on data collection

To display the statistic charts, the app is recording the different detections in a text file. This file is available at `app\resources\data.csv` and is pre-filled with data collected during the development phase. 

The syntax of the CSV file is the following **(positive detections** means **mask worn correcly**, **negative detection** means **mask not worn)** : 

Date ; Time ; number of positive detection ; number of negative detections ; Sum of positive detections ; Sum of negative detections

14/06/2000  ; 08 ; 13 ; 82 ; 1594 ; 1603

14/06/2000 ; 09 ; 9 ; 8 ;;

A functionality was designed to allow the application to take screenshots in case of negative detection but was deleted from the code for confidentiality reasons.