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

            if True:
                pass
                # Imagem Tela Menu
                # self.imgFaseInicial = QLabel(self)
                # self.enderecoimgFaseInicial = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseInicial.setPixmap(self.enderecoimgFaseInicial)
                # self.imgFaseInicial.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseInicial.adjustSize()

                ## Imagem Chefão
                self.imgTelaChefao = QLabel(self)
                self.enderecoimgTelaChefao = QPixmap('imagens_Telas/chefao.jpg')
                self.imgTelaChefao.setPixmap(self.enderecoimgTelaChefao)
                self.imgTelaChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaChefao.adjustSize()

                ## Imagem Fim Armamento
                self.imgTelaFimArmamento = QLabel(self)
                self.enderecoimgTelaFimArmamento = QPixmap('imagens_Telas/fim_armamento.jpg')
                self.imgTelaFimArmamento.setPixmap(self.enderecoimgTelaFimArmamento)
                self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimArmamento.adjustSize()
                
                # ## Imagem Fim Dragão
                self.imgTelaFimDragao = QLabel(self)
                self.enderecoimgTelaFimDragao = QPixmap('imagens_Telas/fim_dragao.jpg')
                self.imgTelaFimDragao.setPixmap(self.enderecoimgTelaFimDragao)
                self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimDragao.adjustSize()

                # ## Imagem Fim Princesa
                self.imgTelaFimPrincesa = QLabel(self)
                self.enderecoimgTelaFimPrincesa = QPixmap('imagens_Telas/fim_princesa.jpg')
                self.imgTelaFimPrincesa.setPixmap(self.enderecoimgTelaFimPrincesa)
                self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimPrincesa.adjustSize()
                trs = QTransform().rotate(180)
                self.imgTelaFimPrincesa.setPixmap(QPixmap(self.enderecoimgTelaFimPrincesa).transformed(trs))

                # ## Imagem Inicio 
                # self.imgFaseDificilChefao = QLabel(self)
                # self.enderecoimgDificilChefao = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseDificilChefao.setPixmap(self.enderecoimgDificilChefao)
                # self.imgFaseDificilChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseDificilChefao.adjustSize()

                # ## Imagem Meio Sala Estar
                # self.imgFaseDificilChefao = QLabel(self)
                # self.enderecoimgDificilChefao = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseDificilChefao.setPixmap(self.enderecoimgDificilChefao)
                # self.imgFaseDificilChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseDificilChefao.adjustSize()

                # ## Imagem Meio Sala Jantar
                # self.imgFaseDificilChefao = QLabel(self)
                # self.enderecoimgDificilChefao = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseDificilChefao.setPixmap(self.enderecoimgDificilChefao)
                # self.imgFaseDificilChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseDificilChefao.adjustSize()

                # ## Imagem Meio Sala Rei
                # self.imgFaseDificilChefao = QLabel(self)
                # self.enderecoimgDificilChefao = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseDificilChefao.setPixmap(self.enderecoimgDificilChefao)
                # self.imgFaseDificilChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseDificilChefao.adjustSize()


            self.nomeJogo = QLabel("Soletrando em Libras", self)
            self.largura = self.nomeJogo.frameGeometry().width()
            self.altura = self.nomeJogo.frameGeometry().height()
            self.nomeJogo.setFont(QFont('Arial Black', 50))
            self.nomeJogo.adjustSize()
            self.nomeJogo.move(int(self.x/3), 50)
            ##################################################
        ## leitura arquivos + ordenação
        if True:
            nRepetir = 1
            fases = []
            meio = []
            fim = []
            vetInicio = []
            vetMeio = []
            vetFim = []
            vetChefao = []
            arquivo = pd.read_csv('./planilha/palavras.csv')
            tamanho = len(arquivo.index)
            variavel1 = 0
            contador10 = 0
            variavel2 = 0
            variavel3 = 0
            tamanhoInicio = 0
            faseMeio = 0
            faseFim = 0
            # Definindo a tela do estagio
            ###########################################################################################
            for variavel3 in range(0, 2):
                if variavel3 == 0:
                    estagio = 'Meio'
                else:
                    estagio = 'Fim'
                for variavel1 in range(0, tamanho):
                    if arquivo.iloc[variavel1]['Estacao'] == estagio:
                        if estagio == 'Meio':
                            tamanhoInicio = len(meio)
                        if estagio == 'Fim':
                            tamanhoInicio = len(fim)

                        if tamanhoInicio == 0:
                            if estagio == 'Meio':
                                meio.append(arquivo.iloc[variavel1]['imagem'])
                            if estagio == 'Fim':
                                fim.append(arquivo.iloc[variavel1]['imagem'])
                        else:
                            for variavel2 in range(0, tamanhoInicio):
                                if estagio == 'Meio':
                                    if meio[variavel2] == arquivo.iloc[variavel1]['imagem']:
                                        contador10 = 1 + contador10
                                if estagio == 'Fim':
                                    if fim[variavel2] == arquivo.iloc[variavel1]['imagem']:
                                        contador10 = 1 + contador10

                            if contador10 == 0:
                                if estagio == 'Meio':
                                    meio.append(arquivo.iloc[variavel1]['imagem'])
                                if estagio == 'Fim':
                                    fim.append(arquivo.iloc[variavel1]['imagem'])
                            contador10 = 0
            #############################################################################################
            ############################################################################################
            # Sorteio das Telas
            faseMeio = random.randint(0, (len(meio) - 1))
            faseFim = random.randint(0, (len(fim) - 1))
            faseMeio = meio[faseMeio]
            faseFim = fim[faseFim]
            faseInicio = 'chegada_castelo'
            faseChefao = 'luta_contra_dragao'
            ###########################################################################################
            ###########################################################################################
            # Colocando as Palavras no Vetor
            for variavel1 in range(0, tamanho):
                if arquivo.iloc[variavel1]['imagem'] == faseInicio:
                    vetInicio.append(arquivo.iloc[variavel1]['Nome'])
                if arquivo.iloc[variavel1]['imagem'] == faseMeio:
                    vetMeio.append(arquivo.iloc[variavel1]['Nome'])
                if arquivo.iloc[variavel1]['imagem'] == faseFim:
                    vetFim.append(arquivo.iloc[variavel1]['Nome'])
                if arquivo.iloc[variavel1]['imagem'] == faseChefao:
                    vetChefao.append(arquivo.iloc[variavel1]['Nome'])
            ##########################################################################################
            #########################################################################################
            # Sorteando as Plavras Nivel Facil
            palavraNivelFacilInicio = []
            palavraNivelFacilMeio = []
            palavraNivelFacilFim = []
            sortTemporario = ''
            for faseFacil in range(0, 5):
                if faseFacil == 0:
                    palavraNivelFacilInicio.append(random.choice(vetInicio))
                elif faseFacil > 0 and faseFacil < 3:
                    if len(palavraNivelFacilMeio) == 0:
                        palavraNivelFacilMeio.append(random.choice(vetMeio))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetMeio)
                            if palavraNivelFacilMeio[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                palavraNivelFacilMeio.append(sortTemporario)
                                nRepetir = 0
                    nRepetir = 1

                else:
                    if len(palavraNivelFacilFim) == 0:
                        palavraNivelFacilFim.append(random.choice(vetFim))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetFim)
                            if palavraNivelFacilFim[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                palavraNivelFacilFim.append(sortTemporario)
                                nRepetir = 0
                    nRepetir = 1
            print('')
            print('Inicio - Facil: ')
            print(palavraNivelFacilInicio)
            print('')

            print('')
            print('Meio - Facil: ')
            print(palavraNivelFacilMeio)
            print('')

            print('')
            print('Fim - Facil: ')
            print(palavraNivelFacilFim)
            print('')
            ##########################################################################################
            #########################################################################################
            # Sorteando as Plavras Nivel Medio

            palavraNivelMedioInicio = []
            palavraNivelMedioMeio = []
            palavraNivelMedioFim = []
            ent = 0
            sortTemporario = ''

            for faseMedio in range(0, 6):
                if faseMedio > -1 and faseMedio < 2:

                    if len(palavraNivelMedioInicio) == 0:
                        palavraNivelMedioInicio.append(random.choice(vetInicio))
                    else:

                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetInicio)
                            if palavraNivelMedioInicio[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelMedioInicio) == 1:
                                    palavraNivelMedioInicio.append(sortTemporario)
                                else:
                                    if palavraNivelMedioInicio[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelMedioInicio) == 2:
                                            palavraNivelMedioInicio.append(sortTemporario)
                                        else:
                                            if palavraNivelMedioInicio[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                if len(palavraNivelMedioInicio) == 3:
                                                    palavraNivelMedioInicio.append(
                                                        sortTemporario)
                                                    nRepetir = 0
                                                else:
                                                    if palavraNivelMedioInicio[3] == sortTemporario:
                                                        nRepetir = 1
                                                    else:
                                                        palavraNivelMedioInicio.append(
                                                            sortTemporario)
                                                        nRepetir = 0
                    nRepetir = 1
                elif faseMedio > 2 and faseMedio < 5:
                    if len(palavraNivelMedioMeio) == 0:
                        palavraNivelMedioMeio.append(random.choice(vetMeio))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetMeio)
                            if palavraNivelMedioMeio[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelMedioMeio) == 1:
                                    palavraNivelMedioMeio.append(sortTemporario)
                                else:
                                    if palavraNivelMedioMeio[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelMedioMeio) == 2:
                                            palavraNivelMedioMeio.append(sortTemporario)
                                            nRepetir = 0
                                        else:
                                            if palavraNivelMedioMeio[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                palavraNivelMedioMeio.append(
                                                    sortTemporario)
                                                nRepetir = 0
                    nRepetir = 1
                else:
                    if len(palavraNivelMedioFim) == 0:
                        palavraNivelMedioFim.append(random.choice(vetFim))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetFim)
                            if palavraNivelMedioFim[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelMedioFim) == 1:
                                    palavraNivelMedioFim.append(sortTemporario)
                                else:
                                    if palavraNivelMedioFim[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelMedioFim) == 2:
                                            palavraNivelMedioFim.append(sortTemporario)
                                            nRepetir = 0
                                        else:
                                            if palavraNivelMedioFim[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                palavraNivelMedioFim.append(sortTemporario)
                                                nRepetir = 0
                    nRepetir = 1
            print('')
            print('Inicio - Medio: ')
            print(palavraNivelMedioInicio)
            print('')

            print('')
            print('Meio - Medio: ')
            print(palavraNivelMedioMeio)
            print('')

            print('')
            print('Fim - Medio: ')
            print(palavraNivelMedioFim)
            print('')
            ##########################################################################################
            #########################################################################################
            # Sorteando as Plavras Nivel Dificil
            palavraNivelDificilInicio = []
            palavraNivelDificilMeio = []
            palavraNivelDificilFim = []

            for fasedificil in range(0, 6):
                if fasedificil > -1 and fasedificil < 2:

                    if len(palavraNivelDificilFim) == 0:
                        palavraNivelDificilFim.append(random.choice(vetFim))
                    else:

                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetFim)
                            if palavraNivelDificilFim[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelDificilFim) == 1:
                                    palavraNivelDificilFim.append(sortTemporario)
                                else:
                                    if palavraNivelDificilFim[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelDificilFim) == 2:
                                            palavraNivelDificilFim.append(sortTemporario)
                                        else:
                                            if palavraNivelDificilFim[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                if len(palavraNivelDificilFim) == 3:
                                                    palavraNivelDificilFim.append(
                                                        sortTemporario)
                                                    nRepetir = 0
                                                else:
                                                    if palavraNivelDificilFim[3] == sortTemporario:
                                                        nRepetir = 1
                                                    else:
                                                        palavraNivelDificilFim.append(
                                                            sortTemporario)
                                                        nRepetir = 0
                    nRepetir = 1
                elif fasedificil > 2 and fasedificil < 5:
                    if len(palavraNivelDificilMeio) == 0:
                        palavraNivelDificilMeio.append(random.choice(vetMeio))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetMeio)
                            if palavraNivelDificilMeio[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelDificilMeio) == 1:
                                    palavraNivelDificilMeio.append(sortTemporario)
                                else:
                                    if palavraNivelDificilMeio[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelDificilMeio) == 2:
                                            palavraNivelDificilMeio.append(sortTemporario)
                                            nRepetir = 0
                                        else:
                                            if palavraNivelDificilMeio[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                palavraNivelDificilMeio.append(
                                                    sortTemporario)
                                                nRepetir = 0
                    nRepetir = 1
                else:
                    if len(palavraNivelDificilInicio) == 0:
                        palavraNivelDificilInicio.append(random.choice(vetInicio))
                    else:
                        while (nRepetir == 1):
                            sortTemporario = random.choice(vetInicio)
                            if palavraNivelDificilInicio[0] == sortTemporario:
                                nRepetir = 1
                            else:
                                if len(palavraNivelDificilInicio) == 1:
                                    palavraNivelDificilInicio.append(sortTemporario)
                                else:
                                    if palavraNivelDificilInicio[1] == sortTemporario:
                                        nRepetir = 1
                                    else:
                                        if len(palavraNivelDificilInicio) == 2:
                                            palavraNivelDificilInicio.append(
                                                sortTemporario)
                                            nRepetir = 0
                                        else:
                                            if palavraNivelDificilInicio[2] == sortTemporario:
                                                nRepetir = 1
                                            else:
                                                palavraNivelDificilInicio.append(
                                                    sortTemporario)
                                                nRepetir = 0
                    nRepetir = 1
            print('')
            print('Inicio - Dificil: ')
            print(palavraNivelDificilInicio)
            print('')

            print('')
            print('Meio - Dificil: ')
            print(palavraNivelDificilMeio)
            print('')

            print('')
            print('Fim - Dificil: ')
            print(palavraNivelDificilFim)
            print('')

            print('')
            print('Chefão - Dificil: ')
            print(vetChefao)
            print('')
        

            
        self.nomeJogo = QLabel(palavraNivelFacilInicio[0], self)
        self.largura = self.nomeJogo.frameGeometry().width()
        self.altura = self.nomeJogo.frameGeometry().height()
        self.nomeJogo.setFont(QFont('Arial Black', 50))
        self.nomeJogo.adjustSize()
        self.nomeJogo.move(int(self.x/1.6), int(self.y/7))
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
                            if letra_Momento != letra:
                                letra_Momento = letra
                                vira = 0
                                virar = 0
                                subir = 0
                                con = 0
                                ladinho = 0
                                contar = 0
                                x = 0
                
                                QApplication.processEvents()
                                time.sleep(0.5)
                                troca_opc = 0
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