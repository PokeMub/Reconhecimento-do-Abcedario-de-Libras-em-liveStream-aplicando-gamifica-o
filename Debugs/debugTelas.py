from concurrent.futures import thread
from configparser import ConverterMapping
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow,QLabel, QApplication, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import mediapipe as mp
from tkinter import *
from dis import dis
import numpy as np
import time
from threading import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from PIL import Image 
from datetime import datetime
import os
import pandas as pd
import random
# https://www.youtube.com/watch?v=2RVVC9rrDco&ab_channel=Andr%C3%A9LuizFran%C3%A7aBatista
nomeJogador = 0
visualizarLetra = 1
letra = 'vazio'
menu_opc1 = 0
menu_opc2 = 0
entrar_opc = 0
troca_opc = 0
dentro_menu_opc2 = 0
menu_opc2_soletra = 0
voltarMenu = 'continuar'
class MyWindow(QWidget):
    
    def initUI(self):
        if True:
            root = Tk()
            monitor_height = root.winfo_screenheight()
            monitor_width = root.winfo_screenwidth()
            self.x = monitor_width - 100
            self.y = monitor_height - 100
            self.setMinimumSize(QSize(self.x, self.y))
            self.setWindowTitle("Tela Inicial")


            self.nomeJogo = QLabel("Soletrando em Libras", self)
            self.largura = self.nomeJogo.frameGeometry().width()
            self.altura = self.nomeJogo.frameGeometry().height()
            self.nomeJogo.setFont(QFont('Arial Black', 50))
            self.nomeJogo.adjustSize()
            self.nomeJogo.move(int(self.x/3), 50)
            ##################################################
    
    def __init__(self):
        super(MyWindow, self).__init__()
    ## Abrir Web Cam
        
        self.VBL = QVBoxLayout()
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.initUI()
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands
        self.ThreadActive = True
        cap = cv2.VideoCapture(0)
        while self.ThreadActive:
            with mp_hands.Hands(
                    max_num_hands=1,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
                while cap.isOpened():
                    success, image = cap.read()
                    if not success:
                        print("Ignoring empty camera frame.")
                        continue
                    image.flags.writeable = False
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    results = hands.process(image)
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    if results.multi_hand_landmarks:
                        image_height, image_width, _ = image.shape
                        annotated_image = image.copy()
                        for hand_landmarks in results.multi_hand_landmarks:
                            if True:
                        
                                pass
                            mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style())
                    FlippedImage = cv2.flip(image, 1)
                    ConvertToQtFormat = QImage(
                        FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(
                        540, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                    if cv2.waitKey(5) & 0xFF == 27:
                        break
            cap.release()

    def stop(self):
        self.ThreadActive = False
        self.quit()


def window():  
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
# Abrindo A janaela do Windos
window()
########################################################