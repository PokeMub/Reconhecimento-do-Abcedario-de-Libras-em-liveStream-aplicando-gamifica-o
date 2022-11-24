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
import unidecode
# import _thread
import threading 
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
menu_opc3 = 0
voltarMenu = 'continuar'
confirmacaoMenuOpcNivel = 0
trocaLetra = 0
palavraNivelFacilInicio = []
palavraNivelFacilMeio = []
palavraNivelFacilFim = []
palavraNivelMedioInicio = []
palavraNivelMedioMeio = []
palavraNivelMedioFim = []
palavraNivelDificilInicio = []
palavraNivelDificilMeio = []
palavraNivelDificilFim = []
vetChefao = []
faseMeio = 0
faseFim = 0
faseInicio = 0
faseChefao = 0
contadorPonto = 0
def contadorPontuacao():
    p = False
    global contadorPonto
    #print("dentro tread") 
    while(p == False):
        contadorPonto = contadorPonto + 1
        #print(contadorPonto)
        time.sleep(1)

 
class MyWindow(QWidget):
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
     
    def initUI(self):
        ##_thread.start_new_thread(contadorPontuacao,())
        
        # ti.start()
        ## criando componentes da interface grafica
        if True:
            # Pegar o tamanho do monitor
            root = Tk()
            monitor_height = root.winfo_screenheight()
            monitor_width = root.winfo_screenwidth()
            self.x = monitor_width - 100
            self.y = monitor_height - 100
            ##################################################

            # Tamanho Minimo da tela
            self.setMinimumSize(QSize(self.x, self.y))
            ####################################################
            
            ###################################################
            # Label com o Nome do Jogo
            ## detectar fontes do pc https://flippingtypical.com/  

            # Titulo da janela
            self.setWindowTitle("Tela Inicial")  
        ## Instanciando as telas
        if True:
                # Imagem Tela Menu
                # self.imgFaseInicial = QLabel(self)
                # self.enderecoimgFaseInicial = QPixmap('imagens_Telas/chefao.jpg')
                # self.imgFaseInicial.setPixmap(self.enderecoimgFaseInicial)
                # self.imgFaseInicial.setGeometry(-10000,-10000,-10000, -10000)
                # # self.imgFaseInicial.setGeometry(int(self.x/3.3), 0,0, 0)
                # self.imgFaseInicial.adjustSize()

                ## Imagem Chefão
                self.imgTelaChefao = QLabel(self)
                self.enderecoimgTelaChefao = QPixmap('imagens_Telas/chefao.jpg')
                self.imgTelaChefao.setPixmap(self.enderecoimgTelaChefao)
                self.imgTelaChefao.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaChefao.adjustSize()

                

                ## Imagem Fim Armamento
                self.imgTelaFimArmamento = QLabel(self)
                self.enderecoimgTelaFimArmamento = QPixmap('imagens_Telas/fim_armamento.jpg')
                self.imgTelaFimArmamento.setPixmap(self.enderecoimgTelaFimArmamento)
                self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimArmamento.adjustSize()
                
                

                # ## Imagem Fim Dragão
                self.imgTelaFimDragao = QLabel(self)
                self.enderecoimgTelaFimDragao = QPixmap('imagens_Telas/fim_dragao.jpg')
                self.imgTelaFimDragao.setPixmap(self.enderecoimgTelaFimDragao)
                self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimDragao.adjustSize()

                

                # ## Imagem Fim Princesa
                self.imgTelaFimPrincesa = QLabel(self)
                self.enderecoimgTelaFimPrincesa = QPixmap('imagens_Telas/fim_princesa.jpg')
                self.imgTelaFimPrincesa.setPixmap(self.enderecoimgTelaFimPrincesa)
                self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaFimPrincesa.adjustSize()
                trs = QTransform().rotate(180)
                self.imgTelaFimPrincesa.setPixmap(QPixmap(self.enderecoimgTelaFimPrincesa).transformed(trs))

                

                # ## Imagem Inicio 
                self.imgTelaInicio = QLabel(self)
                self.enderecoimgTelaInicio = QPixmap('imagens_Telas/inicio.jpg')
                self.imgTelaInicio.setPixmap(self.enderecoimgTelaInicio)
                self.imgTelaInicio.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaInicio.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaInicio.adjustSize()
                trs = QTransform().rotate(180)
                self.imgTelaInicio.setPixmap(QPixmap(self.enderecoimgTelaInicio).transformed(trs))

                

                # ## Imagem Meio Sala Estar
                self.imgTelaMeioSalaEstar = QLabel(self)
                self.enderecoimgTelaMeioSalaEstar = QPixmap('imagens_Telas/meio_sala_estar.jpg')
                self.imgTelaMeioSalaEstar.setPixmap(self.enderecoimgTelaMeioSalaEstar)
                self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaMeioSalaEstar.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaMeioSalaEstar.adjustSize()

                

                # ## Imagem Meio Sala Jantar
                self.imgTelaMeioSalaJantar = QLabel(self)
                self.enderecoimgTelaMeioSalaJantar  = QPixmap('imagens_Telas/meio_sala_jantar.jpg')
                self.imgTelaMeioSalaJantar.setPixmap(self.enderecoimgTelaMeioSalaJantar )
                self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaMeioSalaJantar.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaMeioSalaJantar.adjustSize()

               

                # ## Imagem Meio Sala Rei
                self.imgTelaMeioSalaRei= QLabel(self)
                self.enderecoimgTelaMeioSalaRei = QPixmap('imagens_Telas/meio_sala_rei.jpg')
                self.imgTelaMeioSalaRei.setPixmap(self.enderecoimgTelaMeioSalaRei)
                self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                ##self.imgTelaMeioSalaRei.setGeometry(int(self.x/3.3), 0,0, 0)
                self.imgTelaMeioSalaRei.adjustSize()
                trs = QTransform().rotate(180)
                self.imgTelaMeioSalaRei.setPixmap(QPixmap(self.enderecoimgTelaMeioSalaRei).transformed(trs))
        ## leitura arquivos + ordenação
        if True:
            nRepetir = 1
            fases = []
            meio = []
            fim = []
            vetInicio = []
            vetMeio = []
            vetFim = []
            arquivo = pd.read_csv('./planilha/palavras.csv')
            tamanho = len(arquivo.index)
            variavel1 = 0
            contador10 = 0
            variavel2 = 0
            variavel3 = 0
            tamanhoInicio = 0
            
            global palavraNivelFacilInicio ,palavraNivelFacilMeio,palavraNivelFacilFim ,palavraNivelMedioInicio ,palavraNivelMedioMeio ,palavraNivelMedioFim,palavraNivelDificilInicio, palavraNivelDificilMeio ,palavraNivelDificilFim, vetChefao , faseInicio ,faseMeio , faseFim , faseChefao
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
            
            sortTemporario = ''
            for faseFacil in range(0, 5):
                if faseFacil == 0:
                    palavraNivelFacilInicio = random.choice(vetInicio)
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
        ## Botões tela Jogar
        if True: 
            self.menuNivelDificuldadeFacil = QPushButton(self)
            self.menuNivelDificuldadeFacil.setText("Nivel Facil")
            self.menuNivelDificuldadeFacil.setFont(QFont('Arial Black', 20))
            self.menuNivelDificuldadeFacil.setStyleSheet("border :6px solid black;") 
            self.menuNivelDificuldadeFacil.setStyleSheet("background-color:yellow") 
            self.menuNivelDificuldadeFacil.resize(150, 40) 
            self.menuNivelDificuldadeFacil.adjustSize()
            self.menuNivelDificuldadeFacil.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.menuNivelDificuldadeFacil.move(-500, -500)

            self.menuNivelDificuldadeMedio = QPushButton(self)
            self.menuNivelDificuldadeMedio.setText("Nivel Medio")
            self.menuNivelDificuldadeMedio.setFont(QFont('Arial Black', 20))
            self.menuNivelDificuldadeMedio.setStyleSheet("border :6px solid black;") 
            self.menuNivelDificuldadeMedio.setStyleSheet("background-color:yellow")
            self.menuNivelDificuldadeMedio.resize(150, 40) 
            self.menuNivelDificuldadeMedio.adjustSize()
            self.menuNivelDificuldadeMedio.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.menuNivelDificuldadeMedio.move(-500, -500)
            
            self.menuNivelDificuldadeDificil = QPushButton(self)
            self.menuNivelDificuldadeDificil.setText("Nivel Dificil")
            self.menuNivelDificuldadeDificil.setFont(QFont('Arial Black', 20))
            self.menuNivelDificuldadeDificil.setStyleSheet("border :6px solid black;") 
            self.menuNivelDificuldadeDificil.setStyleSheet("background-color:yellow")
            self.menuNivelDificuldadeDificil.resize(150, 40) 
            self.menuNivelDificuldadeDificil.adjustSize()
            self.menuNivelDificuldadeDificil.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.menuNivelDificuldadeDificil.move(-500, -500)
        ## Botoes das frases soletradas
        if True:
            ## Inicialização labels Modalidade Facil
            if True:
                ## Traço
                self.traco = QLabel('_', self)
                self.largura = self.traco.frameGeometry().width()
                self.altura = self.traco.frameGeometry().height()
                self.traco.setFont(QFont('Arial Black', 90))
                self.traco.adjustSize()
                self.traco.move(-1000,-1000)
                #self.traco.move(int(self.x/2), int(self.y/7))

                ## Facil - Inicio    
                self.nivelFacilPalavra1 = QLabel(palavraNivelFacilInicio, self)
                self.largura = self.nivelFacilPalavra1.frameGeometry().width()
                self.altura = self.nivelFacilPalavra1.frameGeometry().height()
                self.nivelFacilPalavra1.setFont(QFont('Arial Black', 90))
                self.nivelFacilPalavra1.adjustSize()
                self.nivelFacilPalavra1.move(-1000,-1000)
                #self.nivelFacilPalavra1.move(int(self.x/2), int(self.y/7))

                ## Facil - Meio 0
                self.nivelFacilPalavra2 = QLabel(palavraNivelFacilMeio[0], self)
                self.largura = self.nivelFacilPalavra2.frameGeometry().width()
                self.altura = self.nivelFacilPalavra2.frameGeometry().height()
                self.nivelFacilPalavra2.setFont(QFont('Arial Black', 90))
                self.nivelFacilPalavra2.adjustSize()
                #self.nivelFacilPalavra2.move(int(self.x/2), int(self.y/7))
                self.nivelFacilPalavra2.move(-1000,-1000)

                ## Facil - Meio 1
                self.nivelFacilPalavra3 = QLabel(palavraNivelFacilMeio[1], self)
                self.largura = self.nivelFacilPalavra3.frameGeometry().width()
                self.altura = self.nivelFacilPalavra3.frameGeometry().height()
                self.nivelFacilPalavra3.setFont(QFont('Arial Black', 90))
                self.nivelFacilPalavra3.adjustSize()
                #self.nivelFacilPalavra3.move(int(self.x/2), int(self.y/7))
                self.nivelFacilPalavra3.move(-1000,-1000)

                ##Facil - Fim 0 

                self.nivelFacilPalavra4 = QLabel(palavraNivelFacilFim[0], self)
                self.largura = self.nivelFacilPalavra4.frameGeometry().width()
                self.altura = self.nivelFacilPalavra4.frameGeometry().height()
                self.nivelFacilPalavra4.setFont(QFont('Arial Black', 90))
                self.nivelFacilPalavra4.adjustSize()
                #self.nivelFacilPalavra4.move(int(self.x/2), int(self.y/7))
                self.nivelFacilPalavra4.move(-1000,-1000)

                ##Facil - Fim 1

                self.nivelFacilPalavra5 = QLabel(palavraNivelFacilFim[1], self)
                self.largura = self.nivelFacilPalavra5.frameGeometry().width()
                self.altura = self.nivelFacilPalavra5.frameGeometry().height()
                self.nivelFacilPalavra5.setFont(QFont('Arial Black', 90))
                self.nivelFacilPalavra5.adjustSize()
                #self.nivelFacilPalavra5.move(int(self.x/2), int(self.y/7))
                self.nivelFacilPalavra5.move(-1000,-1000)
            ## Inicialização Labels Modadelide Medio
            if True:
                ## Medio - Inicio - 0
                self.nivelMedioPalavra1 = QLabel(palavraNivelMedioInicio[0], self)
                self.largura = self.nivelMedioPalavra1.frameGeometry().width()
                self.altura = self.nivelMedioPalavra1.frameGeometry().height()
                self.nivelMedioPalavra1.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra1.adjustSize()
                self.nivelMedioPalavra1.move(-1000,-1000)
                #self.nivelMedioPalavra1.move(int(self.x/2), int(self.y/7))

                ## Medio - Inicio - 1
                self.nivelMedioPalavra2 = QLabel(palavraNivelMedioInicio[1], self)
                self.largura = self.nivelMedioPalavra2.frameGeometry().width()
                self.altura = self.nivelMedioPalavra2.frameGeometry().height()
                self.nivelMedioPalavra2.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra2.adjustSize()
                self.nivelMedioPalavra2.move(-1000,-1000)
                #self.nivelMedioPalavra2.move(int(self.x/2), int(self.y/7))

                ## Medio - Inicio - 2
                self.nivelMedioPalavra3 = QLabel(palavraNivelMedioInicio[2], self)
                self.largura = self.nivelMedioPalavra3.frameGeometry().width()
                self.altura = self.nivelMedioPalavra3.frameGeometry().height()
                self.nivelMedioPalavra3.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra3.adjustSize()
                self.nivelMedioPalavra3.move(-1000,-1000)
                #self.nivelMedioPalavra2.move(int(self.x/2), int(self.y/7))

                ## Medio - Inicio - 3
                self.nivelMedioPalavra4 = QLabel(palavraNivelMedioInicio[3], self)
                self.largura = self.nivelMedioPalavra4.frameGeometry().width()
                self.altura = self.nivelMedioPalavra4.frameGeometry().height()
                self.nivelMedioPalavra4.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra4.adjustSize()
                self.nivelMedioPalavra4.move(-1000,-1000)
                #self.nivelMedioPalavra4.move(int(self.x/2), int(self.y/7))


                ## Medio - Meio - 0
                self.nivelMedioPalavra5 = QLabel(palavraNivelMedioMeio[0], self)
                self.largura = self.nivelMedioPalavra5.frameGeometry().width()
                self.altura = self.nivelMedioPalavra5.frameGeometry().height()
                self.nivelMedioPalavra5.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra5.adjustSize()
                self.nivelMedioPalavra5.move(-1000,-1000)
                #self.nivelMedioPalavra5.move(int(self.x/2), int(self.y/7))

                ## Medio - Meio - 1
                self.nivelMedioPalavra6 = QLabel(palavraNivelMedioMeio[1], self)
                self.largura = self.nivelMedioPalavra6.frameGeometry().width()
                self.altura = self.nivelMedioPalavra6.frameGeometry().height()
                self.nivelMedioPalavra6.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra6.adjustSize()
                self.nivelMedioPalavra6.move(-1000,-1000)
                #self.nivelMedioPalavra6.move(int(self.x/2), int(self.y/7))

                ## Medio - Meio - 2
                self.nivelMedioPalavra7 = QLabel(palavraNivelMedioMeio[2], self)
                self.largura = self.nivelMedioPalavra7.frameGeometry().width()
                self.altura = self.nivelMedioPalavra7.frameGeometry().height()
                self.nivelMedioPalavra7.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra7.adjustSize()
                self.nivelMedioPalavra7.move(-1000,-1000)
                #self.nivelMedioPalavra7.move(int(self.x/2), int(self.y/7))


                ## Medio - Fim - 0
                self.nivelMedioPalavra8 = QLabel(palavraNivelMedioFim[0], self)
                self.largura = self.nivelMedioPalavra8.frameGeometry().width()
                self.altura = self.nivelMedioPalavra8.frameGeometry().height()
                self.nivelMedioPalavra8.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra8.adjustSize()
                self.nivelMedioPalavra8.move(-1000,-1000)
                #self.nivelMedioPalavra8.move(int(self.x/2), int(self.y/7))
                
                ## Medio - Fim - 1
                self.nivelMedioPalavra9 = QLabel(palavraNivelMedioFim[1], self)
                self.largura = self.nivelMedioPalavra9.frameGeometry().width()
                self.altura = self.nivelMedioPalavra9.frameGeometry().height()
                self.nivelMedioPalavra9.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra9.adjustSize()
                self.nivelMedioPalavra9.move(-1000,-1000)
                #self.nivelMedioPalavra9.move(int(self.x/2), int(self.y/7))

                ## Medio - Fim - 2
                self.nivelMedioPalavra10 = QLabel(palavraNivelMedioFim[2], self)
                self.largura = self.nivelMedioPalavra10.frameGeometry().width()
                self.altura = self.nivelMedioPalavra10.frameGeometry().height()
                self.nivelMedioPalavra10.setFont(QFont('Arial Black', 90))
                self.nivelMedioPalavra10.adjustSize()
                #self.nivelMedioPalavra10.move(int(self.x/2), int(self.y/7))
                self.nivelMedioPalavra10.move(-1000,-1000)
            ##Inicialização Labels Modalidade Dificil
            if True:
                ## Dificil - Inicio - 0
                self.nivelDificilPalavra1 = QLabel(palavraNivelDificilInicio[0], self)
                self.largura = self.nivelDificilPalavra1.frameGeometry().width()
                self.altura = self.nivelDificilPalavra1.frameGeometry().height()
                self.nivelDificilPalavra1.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra1.adjustSize()
                self.nivelDificilPalavra1.move(-1000,-1000)
                #self.nivelDificilPalavra1.move(int(self.x/2), int(self.y/7))

                ## Dificil - Inicio - 1
                self.nivelDificilPalavra2 = QLabel(palavraNivelDificilInicio[1], self)
                self.largura = self.nivelDificilPalavra2.frameGeometry().width()
                self.altura = self.nivelDificilPalavra2.frameGeometry().height()
                self.nivelDificilPalavra2.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra2.adjustSize()
                self.nivelDificilPalavra2.move(-1000,-1000)
                #self.nivelDificilPalavra2.move(int(self.x/2), int(self.y/7))

                ## Dificil - Inicio - 2
                self.nivelDificilPalavra3 = QLabel(palavraNivelDificilInicio[2], self)
                self.largura = self.nivelDificilPalavra3.frameGeometry().width()
                self.altura = self.nivelDificilPalavra3.frameGeometry().height()
                self.nivelDificilPalavra3.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra3.adjustSize()
                self.nivelDificilPalavra3.move(-1000,-1000)
                #self.nivelDificilPalavra3.move(int(self.x/2), int(self.y/7))

            
            ## Dificil - Meio - 0
                self.nivelDificilPalavra4 = QLabel(palavraNivelDificilMeio[0], self)
                self.largura = self.nivelDificilPalavra4.frameGeometry().width()
                self.altura = self.nivelDificilPalavra4.frameGeometry().height()
                self.nivelDificilPalavra4.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra4.adjustSize()
                self.nivelDificilPalavra4.move(-1000,-1000)
                #self.nivelDificilPalavra4.move(int(self.x/2), int(self.y/7))

                ## Dificil - Meio - 1
                self.nivelDificilPalavra5 = QLabel(palavraNivelDificilMeio[1], self)
                self.largura = self.nivelDificilPalavra5.frameGeometry().width()
                self.altura = self.nivelDificilPalavra5.frameGeometry().height()
                self.nivelDificilPalavra5.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra5.adjustSize()
                self.nivelDificilPalavra5.move(-1000,-1000)
                #self.nivelDificilPalavra5.move(int(self.x/2), int(self.y/7))

                ## Dificil - Meio - 2
                self.nivelDificilPalavra6 = QLabel(palavraNivelDificilMeio[2], self)
                self.largura = self.nivelDificilPalavra6.frameGeometry().width()
                self.altura = self.nivelDificilPalavra6.frameGeometry().height()
                self.nivelDificilPalavra6.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra6.adjustSize()
                self.nivelDificilPalavra6.move(-1000,-1000)
                #self.nivelDificilPalavra6.move(int(self.x/2), int(self.y/7))


                ## Dificil - Fim - 0
                self.nivelDificilPalavra7 = QLabel(palavraNivelDificilFim[0], self)
                self.largura = self.nivelDificilPalavra7.frameGeometry().width()
                self.altura = self.nivelDificilPalavra7.frameGeometry().height()
                self.nivelDificilPalavra7.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra7.adjustSize()
                self.nivelDificilPalavra7.move(-1000,-1000)
                #self.nivelDificilPalavra7.move(int(self.x/2), int(self.y/7))

                ## Dificil - Fim - 1
                self.nivelDificilPalavra8 = QLabel(palavraNivelDificilFim[1], self)
                self.largura = self.nivelDificilPalavra8.frameGeometry().width()
                self.altura = self.nivelDificilPalavra8.frameGeometry().height()
                self.nivelDificilPalavra8.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra8.adjustSize()
                self.nivelDificilPalavra8.move(-1000,-1000)
                #self.nivelDificilPalavra8.move(int(self.x/2), int(self.y/7))

                ## Dificil - Fim - 2
                self.nivelDificilPalavra9 = QLabel(palavraNivelDificilFim[2], self)
                self.largura = self.nivelDificilPalavra9.frameGeometry().width()
                self.altura = self.nivelDificilPalavra9.frameGeometry().height()
                self.nivelDificilPalavra9.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra9.adjustSize()
                self.nivelDificilPalavra9.move(-1000,-1000)
                #self.nivelDificilPalavra9.move(int(self.x/2), int(self.y/7))

                ## Dificil - Fim - 3
                self.nivelDificilPalavra10 = QLabel(palavraNivelDificilFim[3], self)
                self.largura = self.nivelDificilPalavra10.frameGeometry().width()
                self.altura = self.nivelDificilPalavra10.frameGeometry().height()
                self.nivelDificilPalavra10.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra10.adjustSize()
                self.nivelDificilPalavra10.move(-1000,-1000)
                #self.nivelDificilPalavra10.move(int(self.x/2), int(self.y/7))


                ## Dificil - Chefão - 0
                self.nivelDificilPalavra11 = QLabel(vetChefao[0], self)
                self.largura = self.nivelDificilPalavra11.frameGeometry().width()
                self.altura = self.nivelDificilPalavra11.frameGeometry().height()
                self.nivelDificilPalavra11.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra11.adjustSize()
                self.nivelDificilPalavra11.move(-1000,-1000)
                #self.nivelDificilPalavra11.move(int(self.x/2), int(self.y/7))

                ## Dificil - Chefão - 1
                self.nivelDificilPalavra12 = QLabel(vetChefao[1], self)
                self.largura = self.nivelDificilPalavra12.frameGeometry().width()
                self.altura = self.nivelDificilPalavra12.frameGeometry().height()
                self.nivelDificilPalavra12.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra12.adjustSize()
                self.nivelDificilPalavra12.move(-1000,-1000)
                #self.nivelDificilPalavra12.move(int(self.x/2), int(self.y/7))

                ## Dificil - Chefão - 2
                self.nivelDificilPalavra13 = QLabel(vetChefao[2], self)
                self.largura = self.nivelDificilPalavra13.frameGeometry().width()
                self.altura = self.nivelDificilPalavra13.frameGeometry().height()
                self.nivelDificilPalavra13.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra13.adjustSize()
                self.nivelDificilPalavra13.move(-1000,-1000)
                #self.nivelDificilPalavra13.move(int(self.x/2), int(self.y/7))

                ## Dificil - Chefão - 3
                self.nivelDificilPalavra14 = QLabel(vetChefao[3], self)
                self.largura = self.nivelDificilPalavra14.frameGeometry().width()
                self.altura = self.nivelDificilPalavra14.frameGeometry().height()
                self.nivelDificilPalavra14.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra14.adjustSize()
                self.nivelDificilPalavra14.move(-1000,-1000)
                #self.nivelDificilPalavra14.move(int(self.x/2), int(self.y/7))

                ## Dificil - Chefão - 4
                self.nivelDificilPalavra15 = QLabel(vetChefao[4], self)
                self.largura = self.nivelDificilPalavra15.frameGeometry().width()
                self.altura = self.nivelDificilPalavra15.frameGeometry().height()
                self.nivelDificilPalavra15.setFont(QFont('Arial Black', 90))
                self.nivelDificilPalavra15.adjustSize()
                #self.nivelDificilPalavra15.move(int(self.x/2), int(self.y/7))
                self.nivelDificilPalavra15.move(-1000,-1000)              
        ## Botoes Gerais
        if True:
            ## Imagem Tela Menu
            self.imgMenu = QLabel(self)
            self.enderecoImMenu = QPixmap('imagens_Telas/chefao.jpg')
            self.imgMenu.setPixmap(self.enderecoImMenu)
            self.imgMenu.setGeometry(0, 0,0, 0)
            #self.imgMenu.adjustSize()
 
            
    
            self.nomeJogo = QLabel("Soletrando em Libras", self)
            self.largura = self.nomeJogo.frameGeometry().width()
            self.altura = self.nomeJogo.frameGeometry().height()
            self.nomeJogo.setFont(QFont('Arial Black', 50))
            self.nomeJogo.adjustSize()
            self.nomeJogo.move(int(self.x/3), 50)
            ##################################################
            self.btLogar = QPushButton(self)
            self.btLogar.setText("Logar")
            self.btLogar.setFont(QFont('Arial Black', 20))
            self.btLogar.setStyleSheet("border :6px solid black;") 
            self.btLogar.resize(150, 40) 
            self.btLogar.adjustSize()
            self.btLogar.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.btLogar.move(int(self.x/3), int(self.y/1.7))

            ## vincular o botao a acao
            self.btLogar.clicked.connect(self.btLogar_presionado) 

            ##############################################################
            
            ## Adicionando Campo de Texto
            self.nomeJogador =QLineEdit(self)
            self.nomeJogador.setFont(QFont('Arial Black', 20))
            self.nomeJogador.adjustSize()
            self.nomeJogador.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.nomeJogador.move(int(self.x/3), int(self.y/2.5))


            ############################################################################################################################
            ## ranks
            df = pd.read_csv("ranks.txt", sep=",", header=None)
            df.rename(columns={0: ' ', 1: ' ', 2: ' ',
                    3: '  ', 4: ' '}, inplace=True, )
            df_ordenado = df.sort_values(by='  ')
            string_ordenada = str(df_ordenado)
            print(string_ordenada)
            
            self.tabelaRanks = QLabel(string_ordenada, self)
            self.tabelaRanks.setFont(QFont('Arial Black', 14))
            self.tabelaRanks.adjustSize()
            self.tabelaRanks.move(-5000, -5000)
            ###########################################################################################################################
            ## Segunda tela

            ## Label Principal Explicando pra que serve os sinais
            self.labelPricipalMovimentaoBotes = QLabel("Sinais para Movimentação dos Botões", self)
            self.labelPricipalMovimentaoBotes.setFont(QFont('Arial Black', 40))
            self.labelPricipalMovimentaoBotes.adjustSize()
            self.labelPricipalMovimentaoBotes.move(-500, -500)


            ### Adicionando uma imagem
            ## Label da Imagem Proximo
            self.labelImagProximo = QLabel("Avançar", self)
            self.labelImagProximo.setFont(QFont('Arial Black', 20))
            self.labelImagProximo.adjustSize()
            self.labelImagProximo.move(-500, -500)
            

            ## Label da Imagem Selecionar
            self.labelImagSelecionar = QLabel("Confirmar", self)
            self.labelImagSelecionar.setFont(QFont('Arial Black', 20))
            self.labelImagSelecionar.adjustSize()
            self.labelImagSelecionar.move(-500, -500)
            ## Imagem Selecionar




            # self.labelA = QLabel(self)
            # self.movieA = QMovie('gif/a.gif')
            # self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            # self.labelA.setMovie(self.movieA)

            self.imgSelecionar = QLabel(self)
            self.enderecoImgSel = QMovie('gif/c.gif')
            #self.imgSelecionar.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.imgSelecionar.setGeometry(QtCore.QRect(-1000, -1000, -1000, -1000))
            self.imgSelecionar.setMovie(self.enderecoImgSel)

            ## Imagem Proximo
            self.imgProximo = QLabel(self)
            self.enderecoImgProx = QMovie('gif/a.gif')
            self.imgProximo.setGeometry(QtCore.QRect(-1000, -1000, -1000, -1000))
            self.imgProximo.setMovie(self.enderecoImgProx)
            #self.imgProximo.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))




            # ## Label da Imagem Voltar
            # self.labelImagVoltar = QLabel("Voltar", self)
            # self.labelImagVoltar.setFont(QFont('Arial Black', 20))
            # self.labelImagVoltar.adjustSize()
            # self.labelImagVoltar.move(-500, -500)
            # ## Imagem Voltar
            # self.imgVoltar = QLabel(self)
            # self.enderecoImVolt = QPixmap('imagens/voltar.jpg')
            # self.imgVoltar.setPixmap(self.enderecoImVolt)
            # self.imgVoltar.setGeometry(0, 0,0, 0)
            
            self.op1MenuVisualizarAlfabeto = QPushButton(self)
            self.op1MenuVisualizarAlfabeto.setText("Visualizar Alfabeto")
            self.op1MenuVisualizarAlfabeto.setFont(QFont('Arial Black', 20))
            self.op1MenuVisualizarAlfabeto.setStyleSheet("border :6px solid black;")
            self.op1MenuVisualizarAlfabeto.setStyleSheet("background-color:yellow") 
            self.op1MenuVisualizarAlfabeto.resize(150, 40) 
            self.op1MenuVisualizarAlfabeto.adjustSize()
            self.op1MenuVisualizarAlfabeto.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.op1MenuVisualizarAlfabeto.move(-500, -500)

            self.op1MenuPraticarAlfabeto = QPushButton(self)
            self.op1MenuPraticarAlfabeto.setText("Praticar Alfabeto")
            self.op1MenuPraticarAlfabeto.setFont(QFont('Arial Black', 20))
            self.op1MenuPraticarAlfabeto.setStyleSheet("border :6px solid black;") 
            self.op1MenuPraticarAlfabeto.setStyleSheet("background-color:yellow") 
            self.op1MenuPraticarAlfabeto.resize(150, 40) 
            self.op1MenuPraticarAlfabeto.adjustSize()
            self.op1MenuPraticarAlfabeto.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.op1MenuPraticarAlfabeto.move(-500, -500)
            
            self.op1MenuJogar = QPushButton(self)
            self.op1MenuJogar.setText("Jogar")
            self.op1MenuJogar.setFont(QFont('Arial Black', 20))
            self.op1MenuJogar.setStyleSheet("border :6px solid black;") 
            self.op1MenuJogar.setStyleSheet("background-color:yellow") 
            self.op1MenuJogar.resize(150, 40) 
            self.op1MenuJogar.adjustSize()
            self.op1MenuJogar.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.op1MenuJogar.move(-500, -500)

            self.op1MenuRecompensas = QPushButton(self)
            self.op1MenuRecompensas.setText("Ranks")
            self.op1MenuRecompensas.setFont(QFont('Arial Black', 20))
            self.op1MenuRecompensas.setStyleSheet("border :6px solid black;") 
            self.op1MenuRecompensas.setStyleSheet("background-color:yellow") 
            self.op1MenuRecompensas.resize(150, 40) 
            self.op1MenuRecompensas.adjustSize()
            self.op1MenuRecompensas.setGeometry(1000, 1000, int(self.x/1.5), 100) 
            self.op1MenuRecompensas.move(-500, -500)

            ## Imagem Seta
            self.imgSeta = QLabel(self)
            self.enderecoImSeta = QPixmap('imagens/seta.png')
            self.imgSeta.setPixmap(self.enderecoImSeta)
            self.imgSeta.setGeometry(0, 0,0, 0)

            ## Botao Proximo Das letras Alfabeto
            self.botaoProx = QPushButton(self)
            self.botaoProx.setText("Proximo")
            self.botaoProx.setFont(QFont('Arial Black', 20))
            self.botaoProx.setStyleSheet("border :6px solid black;") 
            self.botaoProx.resize(150, 40) 
            self.botaoProx.adjustSize()
            self.botaoProx.setGeometry(100, 100, int(self.x/1.7), 50) 
            self.botaoProx.move(-500, -500)
            ####################################################################################################################################

            self.ranks = QLabel("Ranks", self)
            self.largura = self.nomeJogo.frameGeometry().width()
            self.altura = self.nomeJogo.frameGeometry().height()
            self.ranks.setFont(QFont('Arial Black', 50))
            self.ranks.adjustSize()
            self.ranks.move(-500, -500)  
        ## Instanciando Letras Modalidade Dificil
        if True:
            ## A
            self.letraModalidadeDificilA = QLabel("A", self)
            self.largura = self.letraModalidadeDificilA.frameGeometry().width()
            self.altura = self.letraModalidadeDificilA.frameGeometry().height()
            self.letraModalidadeDificilA.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilA.adjustSize()
            #self.letraModalidadeDificilA.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilA.move(int(self.x/2), int(-1000))

            ## B
            self.letraModalidadeDificilB = QLabel("B", self)
            self.largura = self.letraModalidadeDificilB.frameGeometry().width()
            self.altura = self.letraModalidadeDificilB.frameGeometry().height()
            self.letraModalidadeDificilB.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilB.adjustSize()
            #self.letraModalidadeDificilB.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilB.move(int(self.x/2), int(-1000))

            ## C
            self.letraModalidadeDificilC = QLabel("C", self)
            self.largura = self.letraModalidadeDificilC.frameGeometry().width()
            self.altura = self.letraModalidadeDificilC.frameGeometry().height()
            self.letraModalidadeDificilC.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilC.adjustSize()
            #self.letraModalidadeDificilC.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilC.move(int(self.x/2), int(-1000))

            ## D
            self.letraModalidadeDificilD = QLabel("D", self)
            self.largura = self.letraModalidadeDificilD.frameGeometry().width()
            self.altura = self.letraModalidadeDificilD.frameGeometry().height()
            self.letraModalidadeDificilD.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilD.adjustSize()
            #self.letraModalidadeDificilD.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilD.move(int(self.x/2), int(-1000))

            ## E
            self.letraModalidadeDificilE = QLabel("E", self)
            self.largura = self.letraModalidadeDificilE.frameGeometry().width()
            self.altura = self.letraModalidadeDificilE.frameGeometry().height()
            self.letraModalidadeDificilE.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilE.adjustSize()
            #self.letraModalidadeDificilE.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilE.move(int(self.x/2), int(-1000))
            
            ## F
            self.letraModalidadeDificilF = QLabel("F", self)
            self.largura = self.letraModalidadeDificilF.frameGeometry().width()
            self.altura = self.letraModalidadeDificilF.frameGeometry().height()
            self.letraModalidadeDificilF.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilF.adjustSize()
            #self.letraModalidadeDificilF.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilF.move(int(self.x/2), int(-1000))

            ## G
            self.letraModalidadeDificilG = QLabel("G", self)
            self.largura = self.letraModalidadeDificilG.frameGeometry().width()
            self.altura = self.letraModalidadeDificilG.frameGeometry().height()
            self.letraModalidadeDificilG.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilG.adjustSize()
            #self.letraModalidadeDificilG.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilG.move(int(self.x/2), int(-1000))

            ## H
            self.letraModalidadeDificilH = QLabel("H", self)
            self.largura = self.letraModalidadeDificilH.frameGeometry().width()
            self.altura = self.letraModalidadeDificilH.frameGeometry().height()
            self.letraModalidadeDificilH.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilH.adjustSize()
            #self.letraModalidadeDificilH.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilH.move(int(self.x/2), int(-1000))

            ## I
            self.letraModalidadeDificilI = QLabel("I", self)
            self.largura = self.letraModalidadeDificilI.frameGeometry().width()
            self.altura = self.letraModalidadeDificilI.frameGeometry().height()
            self.letraModalidadeDificilI.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilI.adjustSize()
            #self.letraModalidadeDificilI.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilI.move(int(self.x/2), int(-1000))

            ## J
            self.letraModalidadeDificilJ = QLabel("J", self)
            self.largura = self.letraModalidadeDificilJ.frameGeometry().width()
            self.altura = self.letraModalidadeDificilJ.frameGeometry().height()
            self.letraModalidadeDificilJ.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilJ.adjustSize()
            #self.letraModalidadeDificilJ.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilJ.move(int(self.x/2), int(-1000))

            ## K
            self.letraModalidadeDificilK = QLabel("K", self)
            self.largura = self.letraModalidadeDificilK.frameGeometry().width()
            self.altura = self.letraModalidadeDificilK.frameGeometry().height()
            self.letraModalidadeDificilK.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilK.adjustSize()
            #self.letraModalidadeDificilK.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilK.move(int(self.x/2), int(-1000))

            ## L
            self.letraModalidadeDificilL = QLabel("L", self)
            self.largura = self.letraModalidadeDificilL.frameGeometry().width()
            self.altura = self.letraModalidadeDificilL.frameGeometry().height()
            self.letraModalidadeDificilL.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilL.adjustSize()
            #self.letraModalidadeDificilL.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilL.move(int(self.x/2), int(-1000))

            ## M
            self.letraModalidadeDificilM = QLabel("M", self)
            self.largura = self.letraModalidadeDificilM.frameGeometry().width()
            self.altura = self.letraModalidadeDificilM.frameGeometry().height()
            self.letraModalidadeDificilM.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilM.adjustSize()
            #self.letraModalidadeDificilM.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilM.move(int(self.x/2), int(-1000))

            ## N
            self.letraModalidadeDificilN = QLabel("N", self)
            self.largura = self.letraModalidadeDificilN.frameGeometry().width()
            self.altura = self.letraModalidadeDificilN.frameGeometry().height()
            self.letraModalidadeDificilN.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilN.adjustSize()
            #self.letraModalidadeDificilN.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilN.move(int(self.x/2), int(-1000))

            ## O
            self.letraModalidadeDificilO = QLabel("O", self)
            self.largura = self.letraModalidadeDificilO.frameGeometry().width()
            self.altura = self.letraModalidadeDificilO.frameGeometry().height()
            self.letraModalidadeDificilO.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilO.adjustSize()
            #self.letraModalidadeDificilO.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilO.move(int(self.x/2), int(-1000))

            ## P
            self.letraModalidadeDificilP = QLabel("P", self)
            self.largura = self.letraModalidadeDificilP.frameGeometry().width()
            self.altura = self.letraModalidadeDificilP.frameGeometry().height()
            self.letraModalidadeDificilP.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilP.adjustSize()
            #self.letraModalidadeDificilP.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilP.move(int(self.x/2), int(-1000))

            ## Q
            self.letraModalidadeDificilQ = QLabel("Q", self)
            self.largura = self.letraModalidadeDificilQ.frameGeometry().width()
            self.altura = self.letraModalidadeDificilQ.frameGeometry().height()
            self.letraModalidadeDificilQ.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilQ.adjustSize()
            #self.letraModalidadeDificilQ.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilQ.move(int(self.x/2), int(-1000))

            ## R
            self.letraModalidadeDificilR = QLabel("R", self)
            self.largura = self.letraModalidadeDificilR.frameGeometry().width()
            self.altura = self.letraModalidadeDificilR.frameGeometry().height()
            self.letraModalidadeDificilR.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilR.adjustSize()
            #self.letraModalidadeDificilR.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilR.move(int(self.x/2), int(-1000))

            ## S
            self.letraModalidadeDificilS = QLabel("S", self)
            self.largura = self.letraModalidadeDificilS.frameGeometry().width()
            self.altura = self.letraModalidadeDificilS.frameGeometry().height()
            self.letraModalidadeDificilS.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilS.adjustSize()
            #self.letraModalidadeDificilS.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilS.move(int(self.x/2), int(-1000))

            ## T
            self.letraModalidadeDificilT = QLabel("T", self)
            self.largura = self.letraModalidadeDificilT.frameGeometry().width()
            self.altura = self.letraModalidadeDificilT.frameGeometry().height()
            self.letraModalidadeDificilT.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilT.adjustSize()
            #self.letraModalidadeDificilT.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilT.move(int(self.x/2), int(-1000))

            ## U
            self.letraModalidadeDificilU = QLabel("U", self)
            self.largura = self.letraModalidadeDificilU.frameGeometry().width()
            self.altura = self.letraModalidadeDificilU.frameGeometry().height()
            self.letraModalidadeDificilU.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilU.adjustSize()
            #self.letraModalidadeDificilU.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilU.move(int(self.x/2), int(-1000))

            ## V
            self.letraModalidadeDificilV = QLabel("V", self)
            self.largura = self.letraModalidadeDificilV.frameGeometry().width()
            self.altura = self.letraModalidadeDificilV.frameGeometry().height()
            self.letraModalidadeDificilV.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilV.adjustSize()
            #self.letraModalidadeDificilV.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilV.move(int(self.x/2), int(-1000))

            ## W
            self.letraModalidadeDificilW = QLabel("W", self)
            self.largura = self.letraModalidadeDificilW.frameGeometry().width()
            self.altura = self.letraModalidadeDificilW.frameGeometry().height()
            self.letraModalidadeDificilW.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilW.adjustSize()
            #self.letraModalidadeDificilW.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilW.move(int(self.x/2), int(-1000))

            ## X
            self.letraModalidadeDificilX = QLabel("X", self)
            self.largura = self.letraModalidadeDificilX.frameGeometry().width()
            self.altura = self.letraModalidadeDificilX.frameGeometry().height()
            self.letraModalidadeDificilX.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilX.adjustSize()
            #self.letraModalidadeDificilX.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilX.move(int(self.x/2), int(-1000))

            ## Y
            self.letraModalidadeDificilY = QLabel("Y", self)
            self.largura = self.letraModalidadeDificilY.frameGeometry().width()
            self.altura = self.letraModalidadeDificilY.frameGeometry().height()
            self.letraModalidadeDificilY.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilY.adjustSize()
            #self.letraModalidadeDificilY.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilY.move(int(self.x/2), int(-1000))

            ## Z
            self.letraModalidadeDificilZ = QLabel("Z", self)
            self.largura = self.letraModalidadeDificilZ.frameGeometry().width()
            self.altura = self.letraModalidadeDificilZ.frameGeometry().height()
            self.letraModalidadeDificilZ.setFont(QFont('Arial Black', 150))
            self.letraModalidadeDificilZ.adjustSize()
            #self.letraModalidadeDificilZ.move(int(self.x/1.6), int(self.y/3.5))
            self.letraModalidadeDificilZ.move(int(self.x/2), int(-1000))
        ## Instanciando as Imagens das Letras do Alfabeto
        if True:
            #Gif Letra A
            self.labelA = QLabel(self)
            self.movieA = QMovie('gif/a.gif')
            self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelA.setMovie(self.movieA)

            ## Label da Execução da Letra A
            self.labelExcLetA = QLabel("Execução Letra A", self)
            self.labelExcLetA.setFont(QFont('Arial Black', 20))
            self.labelExcLetA.adjustSize()
            self.labelExcLetA.move(-500, -500)

            ## Imagem Letra A
            self.image = QImage('letras/a.jpg') 
            self.imgA = QLabel(self)
            self.enderecoA = QPixmap('letras/a.jpg')
            self.imgA.setPixmap(self.enderecoA)  
            self.imgA.setGeometry(0, 0,0, 0)
            trs = QTransform().rotate(90)
            self.imgA.setPixmap(QPixmap(self.image).transformed(trs))
            
            ## Label Letra A        
            self.labelLetA = QLabel("Letra A", self)
            self.labelLetA.setFont(QFont('Arial Black', 20))
            self.labelLetA.adjustSize()
            self.labelLetA.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra B
            self.labelB = QLabel(self)
            self.movieB = QMovie('gif/b.gif')
            self.labelB.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelB.setMovie(self.movieB)

            ## Label da Execução da Letra B
            self.labelExcLetB = QLabel("Execução Letra B", self)
            self.labelExcLetB.setFont(QFont('Arial Black', 20))
            self.labelExcLetB.adjustSize()
            self.labelExcLetB.move(-500, -500)

            ## Imagem Letra B
            self.imageB = QImage('letras/b.jpg') 
            self.imgB = QLabel(self)
            self.enderecoB = QPixmap('letras/B.jpg')
            self.imgB.setPixmap(self.enderecoB)  
            self.imgB.setGeometry(0, 0,0, 0)
            trsB = QTransform().rotate(90)
            self.imgB.setPixmap(QPixmap(self.imageB).transformed(trsB))
            
            ## Label Letra B        
            self.labelLetB = QLabel("Letra B", self)
            self.labelLetB.setFont(QFont('Arial Black', 20))
            self.labelLetB.adjustSize()
            self.labelLetB.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra C
            self.labelC = QLabel(self)
            self.movieC = QMovie('gif/c.gif')
            self.labelC.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelC.setMovie(self.movieC)

            ## Label da Execução da Letra C
            self.labelExcLetC = QLabel("Execução Letra C", self)
            self.labelExcLetC.setFont(QFont('Arial Black', 20))
            self.labelExcLetC.adjustSize()
            self.labelExcLetC.move(-500, -500)

            ## Imagem Letra C
            self.imageC = QImage('letras/c.jpg') 
            self.imgC = QLabel(self)
            self.enderecoC = QPixmap('letras/c.jpg')
            self.imgC.setPixmap(self.enderecoC)  
            self.imgC.setGeometry(0, 0,0, 0)
            trsC = QTransform().rotate(90)
            self.imgC.setPixmap(QPixmap(self.imageC).transformed(trsC))
            
            ## Label Letra C       
            self.labelLetC = QLabel("Letra C", self)
            self.labelLetC.setFont(QFont('Arial Black', 20))
            self.labelLetC.adjustSize()
            self.labelLetC.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra D
            self.labelD = QLabel(self)
            self.movieD = QMovie('gif/d.gif')
            self.labelD.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelD.setMovie(self.movieD)

            ## Label da Execução da Letra D
            self.labelExcLetD = QLabel("Execução Letra D", self)
            self.labelExcLetD.setFont(QFont('Arial Black', 20))
            self.labelExcLetD.adjustSize()
            self.labelExcLetD.move(-500, -500)

            ## Imagem Letra D
            self.imageD = QImage('letras/d.jpg') 
            self.imgD = QLabel(self)
            self.enderecoD = QPixmap('letras/D.jpg')
            self.imgD.setPixmap(self.enderecoD)  
            self.imgD.setGeometry(0, 0,0, 0)
            trsD = QTransform().rotate(90)
            self.imgD.setPixmap(QPixmap(self.imageD).transformed(trsD))
            
            ## Label Letra D       
            self.labelLetD = QLabel("Letra D", self)
            self.labelLetD.setFont(QFont('Arial Black', 20))
            self.labelLetD.adjustSize()
            self.labelLetD.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra E
            self.labelE = QLabel(self)
            self.movieE = QMovie('gif/e.gif')
            self.labelE.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelE.setMovie(self.movieE)

            ## Label da Execução da Letra E
            self.labelExcLetE = QLabel("Execução Letra E", self)
            self.labelExcLetE.setFont(QFont('Arial Black', 20))
            self.labelExcLetE.adjustSize()
            self.labelExcLetE.move(-500, -500)

            ## Imagem Letra E
            self.imageE = QImage('letras/e.jpg') 
            self.imgE = QLabel(self)
            self.enderecoE = QPixmap('letras/e.jpg')
            self.imgE.setPixmap(self.enderecoE)  
            self.imgE.setGeometry(0, 0,0, 0)
            trsE = QTransform().rotate(90)
            self.imgE.setPixmap(QPixmap(self.imageE).transformed(trsE))
            
            ## Label Letra E        
            self.labelLetE = QLabel("Letra E", self)
            self.labelLetE.setFont(QFont('Arial Black', 20))
            self.labelLetE.adjustSize()
            self.labelLetE.move(-500, -500)
            ############################################################################################################################
            
            ###################################################################################################################################    
            #Gif Letra F
            self.labelF = QLabel(self)
            self.movieF = QMovie('gif/f.gif')
            self.labelF.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelF.setMovie(self.movieF)

            ## Label da Execução da Letra F
            self.labelExcLetF = QLabel("Execução Letra F", self)
            self.labelExcLetF.setFont(QFont('Arial Black', 20))
            self.labelExcLetF.adjustSize()
            self.labelExcLetF.move(-500, -500)

            ## Imagem Letra F
            self.imageF = QImage('letras/f.jpg') 
            self.imgF = QLabel(self)
            self.enderecoF = QPixmap('letras/f.jpg')
            self.imgF.setPixmap(self.enderecoF)  
            self.imgF.setGeometry(0, 0,0, 0)
            trsF = QTransform().rotate(90)
            self.imgF.setPixmap(QPixmap(self.imageF).transformed(trsF))
            
            ## Label Letra F   
            self.labelLetF = QLabel("Letra F", self)
            self.labelLetF.setFont(QFont('Arial Black', 20))
            self.labelLetF.adjustSize()
            self.labelLetF.move(-500, -500)
            ############################################################################################################################

                    ###################################################################################################################################    
            #Gif Letra G
            self.labelG = QLabel(self)
            self.movieG = QMovie('gif/g.gif')
            self.labelG.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelG.setMovie(self.movieG)

            ## Label da Execução da Letra G
            self.labelExcLetG = QLabel("Execução Letra G", self)
            self.labelExcLetG.setFont(QFont('Arial Black', 20))
            self.labelExcLetG.adjustSize()
            self.labelExcLetG.move(-500, -500)

            ## Imagem Letra G
            self.imageG = QImage('letras/g.jpg') 
            self.imgG = QLabel(self)
            self.enderecoG = QPixmap('letras/g.jpg')
            self.imgG.setPixmap(self.enderecoG)  
            self.imgG.setGeometry(0, 0,0, 0)
    
            ## Label Letra G       
            self.labelLetG = QLabel("Letra G", self)
            self.labelLetG.setFont(QFont('Arial Black', 20))
            self.labelLetG.adjustSize()
            self.labelLetG.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra L
            self.labelL = QLabel(self)
            self.movieL = QMovie('gif/l.gif')
            self.labelL.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelL.setMovie(self.movieL)

            ## Label da Execução da Letra L
            self.labelExcLetL = QLabel("Execução Letra L", self)
            self.labelExcLetL.setFont(QFont('Arial Black', 20))
            self.labelExcLetL.adjustSize()
            self.labelExcLetL.move(-500, -500)

            ## Imagem Letra L
            self.imageL = QImage('letras/l.jpg') 
            self.imgL = QLabel(self)
            self.enderecoL = QPixmap('letras/l.jpg')
            self.imgL.setPixmap(self.enderecoL)  
            self.imgL.setGeometry(0, 0,0, 0)
            trsL = QTransform().rotate(90)
            self.imgL.setPixmap(QPixmap(self.imageL).transformed(trsL))
            
            ## Label Letra L       
            self.labelLetL = QLabel("Letra L", self)
            self.labelLetL.setFont(QFont('Arial Black', 20))
            self.labelLetL.adjustSize()
            self.labelLetL.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra M
            self.labelM = QLabel(self)
            self.movieM = QMovie('gif/m.gif')
            self.labelM.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelM.setMovie(self.movieM)

            ## Label da Execução da Letra M
            self.labelExcLetM = QLabel("Execução Letra M", self)
            self.labelExcLetM.setFont(QFont('Arial Black', 20))
            self.labelExcLetM.adjustSize()
            self.labelExcLetM.move(-500, -500)

            ## Imagem Letra M
            self.imageM = QImage('letras/M.jpg') 
            self.imgM = QLabel(self)
            self.enderecoM = QPixmap('letras/M.jpg')
            self.imgM.setPixmap(self.enderecoM)  
            self.imgM.setGeometry(0, 0,0, 0)
            trsM = QTransform().rotate(90)
            self.imgM.setPixmap(QPixmap(self.imageM).transformed(trsM))
            
            ## Label Letra M       
            self.labelLetM = QLabel("Letra M", self)
            self.labelLetM.setFont(QFont('Arial Black', 20))
            self.labelLetM.adjustSize()
            self.labelLetM.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra N
            self.labelN = QLabel(self)
            self.movieN = QMovie('gif/N.gif')
            self.labelN.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelN.setMovie(self.movieN)

            ## Label da Execução da Letra N
            self.labelExcLetN = QLabel("Execução Letra N", self)
            self.labelExcLetN.setFont(QFont('Arial Black', 20))
            self.labelExcLetN.adjustSize()
            self.labelExcLetN.move(-500, -500)

            ## Imagem Letra N
            self.imageN = QImage('letras/N.jpg') 
            self.imgN = QLabel(self)
            self.enderecoN = QPixmap('letras/N.jpg')
            self.imgN.setPixmap(self.enderecoN)  
            self.imgN.setGeometry(0, 0,0, 0)
            trsN = QTransform().rotate(90)
            self.imgN.setPixmap(QPixmap(self.imageN).transformed(trsN))
            
            ## Label Letra N   
            self.labelLetN = QLabel("Letra N", self)
            self.labelLetN.setFont(QFont('Arial Black', 20))
            self.labelLetN.adjustSize()
            self.labelLetN.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra O
            self.labelO = QLabel(self)
            self.movieO = QMovie('gif/O.gif')
            self.labelO.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelO.setMovie(self.movieO)

            ## Label da Execução da Letra O
            self.labelExcLetO = QLabel("Execução Letra O", self)
            self.labelExcLetO.setFont(QFont('Arial Black', 20))
            self.labelExcLetO.adjustSize()
            self.labelExcLetO.move(-500, -500)

            ## Imagem Letra O
            self.imageO = QImage('letras/O.jpg') 
            self.imgO = QLabel(self)
            self.enderecoO = QPixmap('letras/O.jpg')
            self.imgO.setPixmap(self.enderecoO)  
            self.imgO.setGeometry(0, 0,0, 0)
            trsO = QTransform().rotate(90)
            self.imgO.setPixmap(QPixmap(self.imageO).transformed(trsO))
            
            ## Label Letra O  
            self.labelLetO = QLabel("Letra O", self)
            self.labelLetO.setFont(QFont('Arial Black', 20))
            self.labelLetO.adjustSize()
            self.labelLetO.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra P
            self.labelP = QLabel(self)
            self.movieP = QMovie('gif/P.gif')
            self.labelP.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelP.setMovie(self.movieP)

            ## Label da Execução da Letra P
            self.labelExcLetP = QLabel("Execução Letra P", self)
            self.labelExcLetP.setFont(QFont('Arial Black', 20))
            self.labelExcLetP.adjustSize()
            self.labelExcLetP.move(-500, -500)

            ## Imagem Letra P
            self.imageP = QImage('letras/P.jpg') 
            self.imgP = QLabel(self)
            self.enderecoP = QPixmap('letras/P.jpg')
            self.imgP.setPixmap(self.enderecoP)  
            self.imgP.setGeometry(0, 0,0, 0)
            trsP = QTransform().rotate(90)
            self.imgP.setPixmap(QPixmap(self.imageP).transformed(trsP))
            
            ## Label Letra P       
            self.labelLetP = QLabel("Letra P", self)
            self.labelLetP.setFont(QFont('Arial Black', 20))
            self.labelLetP.adjustSize()
            self.labelLetP.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra Q
            self.labelQ = QLabel(self)
            self.movieQ = QMovie('gif/Q.gif')
            self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelQ.setMovie(self.movieQ)

            ## Label da Execução da Letra Q
            self.labelExcLetQ = QLabel("Execução Letra Q", self)
            self.labelExcLetQ.setFont(QFont('Arial Black', 20))
            self.labelExcLetQ.adjustSize()
            self.labelExcLetQ.move(-500, -500)

            ## Imagem Letra Q
            self.imageQ = QImage('letras/Q.jpg') 
            self.imgQ = QLabel(self)
            self.enderecoQ = QPixmap('letras/O.jpg')
            self.imgQ.setPixmap(self.enderecoQ)  
            self.imgQ.setGeometry(0, 0,0, 0)
            trsQ = QTransform().rotate(90)
            self.imgQ.setPixmap(QPixmap(self.imageQ).transformed(trsQ))
            
            ## Label Letra Q       
            self.labelLetQ = QLabel("Letra Q", self)
            self.labelLetQ.setFont(QFont('Arial Black', 20))
            self.labelLetQ.adjustSize()
            self.labelLetQ.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra R
            self.labelR = QLabel(self)
            self.movieR = QMovie('gif/R.gif')
            self.labelR.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelR.setMovie(self.movieR)

            ## Label da Execução da Letra R
            self.labelExcLetR = QLabel("Execução Letra R", self)
            self.labelExcLetR.setFont(QFont('Arial Black', 20))
            self.labelExcLetR.adjustSize()
            self.labelExcLetR.move(-500, -500)

            ## Imagem Letra R
            self.imageR = QImage('letras/R.jpg') 
            self.imgR = QLabel(self)
            self.enderecoR = QPixmap('letras/R.jpg')
            self.imgR.setPixmap(self.enderecoR)  
            self.imgR.setGeometry(0, 0,0, 0)
            trsR = QTransform().rotate(90)
            self.imgR.setPixmap(QPixmap(self.imageR).transformed(trsR))
            
            ## Label Letra R 
            self.labelLetR = QLabel("Letra R", self)
            self.labelLetR.setFont(QFont('Arial Black', 20))
            self.labelLetR.adjustSize()
            self.labelLetR.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra S
            self.labelS = QLabel(self)
            self.movieS = QMovie('gif/S.gif')
            self.labelS.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelS.setMovie(self.movieS)

            ## Label da Execução da Letra S
            self.labelExcLetS = QLabel("Execução Letra S", self)
            self.labelExcLetS.setFont(QFont('Arial Black', 20))
            self.labelExcLetS.adjustSize()
            self.labelExcLetS.move(-500, -500)

            ## Imagem Letra S
            self.imageS = QImage('letras/S.jpg') 
            self.imgS = QLabel(self)
            self.enderecoS = QPixmap('letras/S.jpg')
            self.imgS.setPixmap(self.enderecoS)  
            self.imgS.setGeometry(0, 0,0, 0)
            trsS = QTransform().rotate(90)
            self.imgS.setPixmap(QPixmap(self.imageS).transformed(trsS))
            
            ## Label Letra S     
            self.labelLetS = QLabel("Letra S", self)
            self.labelLetS.setFont(QFont('Arial Black', 20))
            self.labelLetS.adjustSize()
            self.labelLetS.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra T
            self.labelT = QLabel(self)
            self.movieT = QMovie('gif/T.gif')
            self.labelT.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelT.setMovie(self.movieT)

            ## Label da Execução da Letra T
            self.labelExcLetT = QLabel("Execução Letra T", self)
            self.labelExcLetT.setFont(QFont('Arial Black', 20))
            self.labelExcLetT.adjustSize()
            self.labelExcLetT.move(-500, -500)

            ## Imagem Letra T
            self.imageT = QImage('letras/T.jpg') 
            self.imgT = QLabel(self)
            self.enderecoT = QPixmap('letras/T.jpg')
            self.imgT.setPixmap(self.enderecoT)  
            self.imgT.setGeometry(0, 0,0, 0)
            trsT = QTransform().rotate(90)
            self.imgT.setPixmap(QPixmap(self.imageT).transformed(trsT))
            
            ## Label Letra T  
            self.labelLetT = QLabel("Letra T", self)
            self.labelLetT.setFont(QFont('Arial Black', 20))
            self.labelLetT.adjustSize()
            self.labelLetT.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra U
            self.labelU = QLabel(self)
            self.movieU = QMovie('gif/U.gif')
            self.labelU.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelU.setMovie(self.movieU)

            ## Label da Execução da Letra U
            self.labelExcLetU = QLabel("Execução Letra U", self)
            self.labelExcLetU.setFont(QFont('Arial Black', 20))
            self.labelExcLetU.adjustSize()
            self.labelExcLetU.move(-500, -500)

            ## Imagem Letra U
            self.imageU = QImage('letras/U.jpg') 
            self.imgU = QLabel(self)
            self.enderecoU = QPixmap('letras/U.jpg')
            self.imgU.setPixmap(self.enderecoU)  
            self.imgU.setGeometry(0, 0,0, 0)
            trsU = QTransform().rotate(90)
            self.imgU.setPixmap(QPixmap(self.imageU).transformed(trsU))
            
            ## Label Letra U
            
            self.labelLetU = QLabel("Letra U", self)
            self.labelLetU.setFont(QFont('Arial Black', 20))
            self.labelLetU.adjustSize()
            self.labelLetU.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra V
            self.labelV = QLabel(self)
            self.movieV = QMovie('gif/V.gif')
            self.labelV.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelV.setMovie(self.movieV)

            ## Label da Execução da Letra V
            self.labelExcLetV = QLabel("Execução Letra V", self)
            self.labelExcLetV.setFont(QFont('Arial Black', 20))
            self.labelExcLetV.adjustSize()
            self.labelExcLetV.move(-500, -500)

            ## Imagem Letra V
            self.imageV = QImage('letras/V.jpg') 
            self.imgV = QLabel(self)
            self.enderecoV = QPixmap('letras/V.jpg')
            self.imgV.setPixmap(self.enderecoV)  
            self.imgV.setGeometry(0, 0,0, 0)
            trsV = QTransform().rotate(90)
            self.imgV.setPixmap(QPixmap(self.imageV).transformed(trsV))
            
            ## Label Letra V
            
            self.labelLetV = QLabel("Letra V", self)
            self.labelLetV.setFont(QFont('Arial Black', 20))
            self.labelLetV.adjustSize()
            self.labelLetV.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra h
            self.labelH = QLabel(self)
            self.movieH = QMovie('gif/H.gif')
            self.labelH.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelH.setMovie(self.movieH)

            ## Label da Execução da Letra H
            self.labelExcLetH = QLabel("Execução Letra H", self)
            self.labelExcLetH.setFont(QFont('Arial Black', 20))
            self.labelExcLetH.adjustSize()
            self.labelExcLetH.move(-500, -500)

            ## Imagem Letra H1
            self.imageH1 = QImage('letras/H1.jpg') 
            self.imgH1 = QLabel(self)
            self.enderecoH1 = QPixmap('letras/H1.jpg')
            self.imgH1.setPixmap(self.enderecoH1)  
            self.imgH1.setGeometry(0, 0,0, 0)
    
            ## Imagem Letra H2
            self.imageH2 = QImage('letras/H2.jpg') 
            self.imgH2 = QLabel(self)
            self.enderecoH2 = QPixmap('letras/H2.jpg')
            self.imgH2.setPixmap(self.enderecoH2)  
            self.imgH2.setGeometry(0, 0,0, 0)

            ## Imagem Letra H3
            self.imageH3 = QImage('letras/H3.jpg') 
            self.imgH3 = QLabel(self)
            self.enderecoH3 = QPixmap('letras/H3.jpg')
            self.imgH3.setPixmap(self.enderecoH3)  
            self.imgH3.setGeometry(0, 0,0, 0)

            ## Label Letra H
            self.labelLetH = QLabel("Letra H", self)
            self.labelLetH.setFont(QFont('Arial Black', 20))
            self.labelLetH.adjustSize()
            self.labelLetH.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra J
            self.labelJ = QLabel(self)
            self.movieJ = QMovie('gif/J.gif')
            self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelJ.setMovie(self.movieJ)

            ## Label da Execução da Letra J
            self.labelExcLetJ = QLabel("Execução Letra J", self)
            self.labelExcLetJ.setFont(QFont('Arial Black', 20))
            self.labelExcLetJ.adjustSize()
            self.labelExcLetJ.move(-500, -500)

            ## Imagem Letra J1
            self.imageJ1 = QImage('letras/J1.jpg') 
            self.imgJ1 = QLabel(self)
            self.enderecoJ1 = QPixmap('letras/J1.jpg')
            self.imgJ1.setPixmap(self.enderecoJ1)  
            self.imgJ1.setGeometry(0, 0,0, 0)

            ## Imagem Letra J2
            self.imageJ2 = QImage('letras/J2.jpg') 
            self.imgJ2 = QLabel(self)
            self.enderecoJ2 = QPixmap('letras/J2.jpg')
            self.imgJ2.setPixmap(self.enderecoJ2)  
            self.imgJ2.setGeometry(0, 0,0, 0)

            ## Imagem Letra J3
            self.imageJ3 = QImage('letras/J3.jpg') 
            self.imgJ3 = QLabel(self)
            self.enderecoJ3 = QPixmap('letras/J3.jpg')
            self.imgJ3.setPixmap(self.enderecoJ3)  
            self.imgJ3.setGeometry(0, 0,0, 0)

            ## Label Letra H    
            self.labelLetJ = QLabel("Letra J", self)
            self.labelLetJ.setFont(QFont('Arial Black', 20))
            self.labelLetJ.adjustSize()
            self.labelLetJ.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra X
            self.labelX = QLabel(self)
            self.movieX = QMovie('gif/X.gif')
            self.labelX.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelX.setMovie(self.movieX)

            ## Label da Execução da Letra X
            self.labelExcLetX = QLabel("Execução Letra X", self)
            self.labelExcLetX.setFont(QFont('Arial Black', 20))
            self.labelExcLetX.adjustSize()
            self.labelExcLetX.move(-500, -500)

            ## Imagem Letra X1
            self.imageX1 = QImage('letras/X1.jpg') 
            self.imgX1 = QLabel(self)
            self.enderecoX1 = QPixmap('letras/X1.jpg')
            self.imgX1.setPixmap(self.enderecoX1)  
            self.imgX1.setGeometry(0, 0,0, 0)

            ## Imagem Letra X2
            self.imageX2 = QImage('letras/X2.jpg') 
            self.imgX2 = QLabel(self)
            self.enderecoX2 = QPixmap('letras/X2.jpg')
            self.imgX2.setPixmap(self.enderecoX2)  
            self.imgX2.setGeometry(0, 0,0, 0)

            ## Imagem Letra X3
            self.imageX3 = QImage('letras/X3.jpg') 
            self.imgX3 = QLabel(self)
            self.enderecoX3 = QPixmap('letras/X3.jpg')
            self.imgX3.setPixmap(self.enderecoX3)  
            self.imgX3.setGeometry(0, 0,0, 0)

            ## Label Letra H 
            self.labelLetX = QLabel("Letra X", self)
            self.labelLetX.setFont(QFont('Arial Black', 20))
            self.labelLetX.adjustSize()
            self.labelLetX.move(-500, -500)
            ############################################################################################################################


            ###################################################################################################################################    
            #Gif Letra Y
            self.labelY = QLabel(self)
            self.movieY = QMovie('gif/Y.gif')
            self.labelY.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelY.setMovie(self.movieY)

            ## Label da Execução da Letra Y
            self.labelExcLetY = QLabel("Execução Letra Y", self)
            self.labelExcLetY.setFont(QFont('Arial Black', 20))
            self.labelExcLetY.adjustSize()
            self.labelExcLetY.move(-500, -500)

            ## Imagem Letra y1
            self.imageY1 = QImage('letras/Y1.jpg') 
            self.imgY1 = QLabel(self)
            self.enderecoY1 = QPixmap('letras/Y1.jpg')
            self.imgY1.setPixmap(self.enderecoY1)  
            self.imgY1.setGeometry(0, 0,0, 0)
    
            ## Imagem Letra Y2
            self.imageY2 = QImage('letras/Y2.jpg') 
            self.imgY2 = QLabel(self)
            self.enderecoY2 = QPixmap('letras/Y2.jpg')
            self.imgY2.setPixmap(self.enderecoY2)  
            self.imgY2.setGeometry(0, 0,0, 0)

            ## Imagem Letra Y3
            self.imageY3 = QImage('letras/Y3.jpg') 
            self.imgY3 = QLabel(self)
            self.enderecoY3 = QPixmap('letras/Y3.jpg')
            self.imgY3.setPixmap(self.enderecoY3)  
            self.imgY3.setGeometry(0, 0,0, 0)

            ## Label Letra H
            self.labelLetY = QLabel("Letra Y", self)
            self.labelLetY.setFont(QFont('Arial Black', 20))
            self.labelLetY.adjustSize()
            self.labelLetY.move(-500, -500)
            ############################################################################################################################


            ###################################################################################################################################    
            #Gif Letra W
            self.labelW = QLabel(self)
            self.movieW = QMovie('gif/W.gif')
            self.labelW.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelW.setMovie(self.movieW)

            ## Label da Execução da Letra W
            self.labelExcLetW = QLabel("Execução Letra W", self)
            self.labelExcLetW.setFont(QFont('Arial Black', 20))
            self.labelExcLetW.adjustSize()
            self.labelExcLetW.move(-500, -500)

            ## Imagem Letra W1
            self.imageW1 = QImage('letras/W1.jpg') 
            self.imgW1 = QLabel(self)
            self.enderecoW1 = QPixmap('letras/W1.jpg')
            self.imgW1.setPixmap(self.enderecoW1)  
            self.imgW1.setGeometry(0, 0,0, 0)
        
            ## Imagem Letra W2
            self.imageW2 = QImage('letras/W2.jpg') 
            self.imgW2 = QLabel(self)
            self.enderecoW2 = QPixmap('letras/W2.jpg')
            self.imgW2.setPixmap(self.enderecoW2)  
            self.imgW2.setGeometry(0, 0,0, 0)

            ## Imagem Letra W3
            self.imageW3 = QImage('letras/W3.jpg') 
            self.imgW3 = QLabel(self)
            self.enderecoW3 = QPixmap('letras/W3.jpg')
            self.imgW3.setPixmap(self.enderecoW3)  
            self.imgW3.setGeometry(0, 0,0, 0)

            ## Label Letra W
            self.labelLetW = QLabel("Letra W", self)
            self.labelLetW.setFont(QFont('Arial Black', 20))
            self.labelLetW.adjustSize()
            self.labelLetW.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra I
            self.labelI = QLabel(self)
            self.movieI = QMovie('gif/I.gif')
            self.labelI.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelI.setMovie(self.movieI)

            ## Label da Execução da Letra I
            self.labelExcLetI = QLabel("Execução Letra I", self)
            self.labelExcLetI.setFont(QFont('Arial Black', 20))
            self.labelExcLetI.adjustSize()
            self.labelExcLetI.move(-500, -500)

            ## Imagem Letra I1
            self.imageI1 = QImage('letras/I1.jpg') 
            self.imgI1 = QLabel(self)
            self.enderecoI1 = QPixmap('letras/I1.jpg')
            self.imgI1.setPixmap(self.enderecoI1)  
            self.imgI1.setGeometry(0, 0,0, 0)

            ## Imagem Letra I2
            self.imageI2 = QImage('letras/I2.jpg') 
            self.imgI2 = QLabel(self)
            self.enderecoI2 = QPixmap('letras/I2.jpg')
            self.imgI2.setPixmap(self.enderecoI2)  
            self.imgI2.setGeometry(0, 0,0, 0)

            ## Imagem Letra I3
            self.imageI3 = QImage('letras/I3.jpg') 
            self.imgI3 = QLabel(self)
            self.enderecoI3 = QPixmap('letras/I3.jpg')
            self.imgI3.setPixmap(self.enderecoI3)  
            self.imgI3.setGeometry(0, 0,0, 0)

            ## Imagem Letra I4
            self.imageI4 = QImage('letras/I4.jpg') 
            self.imgI4 = QLabel(self)
            self.enderecoI4 = QPixmap('letras/I4.jpg')
            self.imgI4.setPixmap(self.enderecoI4)  
            self.imgI4.setGeometry(0, 0,0, 0)

            ## Label Letra I
            self.labelLetI = QLabel("Letra I", self)
            self.labelLetI.setFont(QFont('Arial Black', 20))
            self.labelLetI.adjustSize()
            self.labelLetI.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra Z
            self.labelZ = QLabel(self)
            self.movieZ = QMovie('gif/Z.gif')
            self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelZ.setMovie(self.movieZ)

            ## Label da Execução da Letra Z
            self.labelExcLetZ = QLabel("Execução Letra Z", self)
            self.labelExcLetZ.setFont(QFont('Arial Black', 20))
            self.labelExcLetZ.adjustSize()
            self.labelExcLetZ.move(-500, -500)

            ## Imagem Letra Z1
            self.imageZ1 = QImage('letras/Z1.jpg') 
            self.imgZ1 = QLabel(self)
            self.enderecoZ1 = QPixmap('letras/Z1.jpg')
            self.imgZ1.setPixmap(self.enderecoZ1)  
            self.imgZ1.setGeometry(0, 0,0, 0)

            ## Imagem Letra Z2
            self.imageZ2 = QImage('letras/Z2.jpg') 
            self.imgZ2 = QLabel(self)
            self.enderecoZ2 = QPixmap('letras/Z2.jpg')
            self.imgZ2.setPixmap(self.enderecoZ2)  
            self.imgZ2.setGeometry(0, 0,0, 0)

            ## Imagem Letra Z3
            self.imageZ3 = QImage('letras/Z3.jpg') 
            self.imgZ3 = QLabel(self)
            self.enderecoZ3 = QPixmap('letras/Z3.jpg')
            self.imgZ3.setPixmap(self.enderecoZ3)  
            self.imgZ3.setGeometry(0, 0,0, 0)

            ## Imagem Letra Z4
            self.imageZ4 = QImage('letras/Z4.jpg') 
            self.imgZ4 = QLabel(self)
            self.enderecoZ4 = QPixmap('letras/Z4.jpg')
            self.imgZ4.setPixmap(self.enderecoZ4)  
            self.imgZ4.setGeometry(0, 0,0, 0)

            ## Label Letra Z
            self.labelLetZ = QLabel("Letra Z", self)
            self.labelLetZ.setFont(QFont('Arial Black', 20))
            self.labelLetZ.adjustSize()
            self.labelLetZ.move(-500, -500)
            ############################################################################################################################

            ###################################################################################################################################    
            #Gif Letra K
            self.labelK = QLabel(self)
            self.movieK = QMovie('gif/K.gif')
            self.labelK.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
            self.labelK.setMovie(self.movieK)

            ## Label da Execução da Letra K
            self.labelExcLetK = QLabel("Execução Letra K", self)
            self.labelExcLetK.setFont(QFont('Arial Black', 20))
            self.labelExcLetK.adjustSize()
            self.labelExcLetK.move(-500, -500)

            ## Imagem Letra K1
            self.imageK1 = QImage('letras/K1.jpg') 
            self.imgK1 = QLabel(self)
            self.enderecoK1 = QPixmap('letras/K1.jpg')
            self.imgK1.setPixmap(self.enderecoK1)  
            self.imgK1.setGeometry(0, 0,0, 0)

            ## Imagem Letra K2
            self.imageK2 = QImage('letras/K2.jpg') 
            self.imgK2 = QLabel(self)
            self.enderecoK2 = QPixmap('letras/K2.jpg')
            self.imgK2.setPixmap(self.enderecoK2)  
            self.imgK2.setGeometry(0, 0,0, 0)

            ## Imagem Letra K3
            self.imageK3 = QImage('letras/K3.jpg') 
            self.imgK3 = QLabel(self)
            self.enderecoK3 = QPixmap('letras/K3.jpg')
            self.imgK3.setPixmap(self.enderecoK3)  
            self.imgK3.setGeometry(0, 0,0, 0)

            ## Label Letra K
            self.labelLetK = QLabel("Letra K", self)
            self.labelLetK.setFont(QFont('Arial Black', 20))
            self.labelLetK.adjustSize()
            self.labelLetK.move(-500, -500)
    #Metodo para ação do botão
    def btLogar_presionado(self):
        
        global letra , dentro_menu_opc2, entrar_opc, menu_opc2, troca_opc, visualizarLetra, menu_opc2_soletra, voltarMenu, menu_opc3,confirmacaoMenuOpcNivel,palavraNivelFacilInicio,trocaLetra, faseInicio ,faseMeio , faseFim , faseChefao,contadorPonto, nomeJogador
        nomeJogador = self.nomeJogador.text()
        print(nomeJogador)
        trav = 0
        cont1 = 0
        entr1vez = 0
        entrar_1_vez =0
        letraPrintar = ''
        letraRemover = ''
        estagio = 1
        estagio2 = 1   
        estagio3 = 1
        estagio4 = 1
        estagio1 = 1
        contAux = 0
        tamanhoPalavra = -1
        somatorioPontos = 0
        resetePontos = 1
        self.nomeJogo.adjustSize()
        self.nomeJogo.move(-10000, -10000)
        while True:
            #print ('Pontução geral: ' ,  somatorioPontos)
            #print('Pontuação Unica: ', contadorPonto)
            if menu_opc1 == 0 :
                if menu_opc1 == 0 and menu_opc2 == 0:
                    QApplication.processEvents()
                    
                    self.nomeJogador.hide()
                    self.btLogar.hide()

                    ## Label Principal Explicando pra que serve os sinais
                    self.labelPricipalMovimentaoBotes.adjustSize()
                    self.labelPricipalMovimentaoBotes.move(int(self.x/5), 50)

                    ### Adicionando uma imagem
                    ## Label da Imagem Proximo
                    self.labelImagProximo.adjustSize()
                    self.labelImagProximo.move(int(self.x/2.3), int(self.y/4.2))

                    self.imgProximo.setGeometry(QtCore.QRect(int(self.x/2.8), int(self.y/3.5), 600, 600))
                    self.enderecoImgProx.start()
                    ## Imagem Proximo
                    #self.imgProximo.setGeometry(int(self.x/3), int(self.y/1.7),400,300)
                    # self.imgProximo.adjustSize()
                    # self.imgProximo.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
                    

                    
                    ## Label da Imagem Selecionar
                    self.labelImagSelecionar.adjustSize()
                    self.labelImagSelecionar.move(int(self.x/1.4), int(self.y/4.2))
                    self.imgSelecionar.setGeometry(QtCore.QRect(int(self.x/1.5), int(self.y/3.5), 600, 600))
                    self.enderecoImgSel.start()
                    ## Imagem Selecionar
                    #self.imgSelecionar.setGeometry(int(self.x/1.8), int(self.y/1.7),400,300)
                    # self.imgSelecionar.adjustSize()
                    # self.imgSelecionar.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))

                    ## Label da Imagem Voltar
                    # self.labelImagVoltar.adjustSize()
                    # self.labelImagVoltar.move(int(self.x/1.284 + 135), int(self.y/1.9))
                    ## Imagem Voltar
                    # self.imgVoltar.setGeometry(int(self.x/1.284), int(self.y/1.7),400,300)
                if(troca_opc == 0):
                    letra = 'proximo'
                if troca_opc == 1:
                    letra = 'selecionar'
                if troca_opc == 2:
                    pass
                if menu_opc2 == 1:
                    QApplication.processEvents()
                    # self.labelImagVoltar.adjustSize()
                    # self.labelImagVoltar.move(-500, -500)
                    # self.imgVoltar.setGeometry(int(-500), int(self.y/1.7),400,300)

                    self.labelImagSelecionar.adjustSize()
                    self.labelImagSelecionar.move(-500, -500)
                    #self.imgSelecionar.setGeometry(int(-500), int(self.y/1.7),400,300)

                    self.labelImagProximo.adjustSize()
                    self.labelImagProximo.move(-500, -500)
                    #self.imgProximo.setGeometry(int(-500), int(self.y/1.7),400,300)

                    self.enderecoImgProx.stop()
                    self.imgProximo.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                    self.enderecoImgSel.stop()
                    self.imgSelecionar.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                    self.labelPricipalMovimentaoBotes.move(-500, -500)
                    

                    self.op1MenuVisualizarAlfabeto.adjustSize()
                    self.op1MenuVisualizarAlfabeto.setGeometry(900, 900, int(self.x/1.7), 90) 
                    self.op1MenuVisualizarAlfabeto.move(int(self.x/2.5), int(self.y/4))

                    self.op1MenuPraticarAlfabeto.adjustSize()
                    self.op1MenuPraticarAlfabeto.setGeometry(900, 900, int(self.x/1.7), 90) 
                    self.op1MenuPraticarAlfabeto.move(int(self.x/2.5), int(self.y/2.8))

                    self.op1MenuJogar.adjustSize()
                    self.op1MenuJogar.setGeometry(900, 900, int(self.x/1.7), 90) 
                    self.op1MenuJogar.move(int(self.x/2.5), int(self.y/2.15))

                    self.op1MenuRecompensas.adjustSize()
                    self.op1MenuRecompensas.setGeometry(900, 900, int(self.x/1.7), 90) 
                    self.op1MenuRecompensas.move(int(self.x/2.5), int(self.y/1.74))
                    
                    self.imgMenu.adjustSize()
                    self.imgMenu.move(int(self.x /3.3), 0)
                    dentro_menu_opc2 = 1
                if menu_opc2 == 2 and entrar_opc == 1:
                    QApplication.processEvents()
                    letra = 'proximo2'
                    troca_opc = 2
                    self.imgSeta.move(int(-100), int(-100))

                    self.op1MenuVisualizarAlfabeto.adjustSize()
                    self.op1MenuVisualizarAlfabeto.move(int(-100), int(-100))

                    self.op1MenuPraticarAlfabeto.adjustSize()
                    self.op1MenuPraticarAlfabeto.move(int(-100), int(-100))

                    self.op1MenuJogar.adjustSize()
                    self.op1MenuJogar.move(int(-100), int(-100))

                    self.op1MenuRecompensas.adjustSize()
                    self.op1MenuRecompensas.move(int(-100), int(-100))

                    self.imgMenu.adjustSize()
                    self.imgMenu.move(int(self.x /3.3), int(-2000))
                    if(trav == 1):
                        visualizarLetra = 1
                        trav = 0                 
                    if(visualizarLetra == 1):

                        self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
                        self.movieA.start()

                        self.labelExcLetA.adjustSize()
                        self.labelExcLetA.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgA.adjustSize()
                        self.imgA.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetA.adjustSize()
                        self.labelLetA.move(int(self.x/1.8), int(self.y/4.2))

                        self.botaoProx.adjustSize()
                        self.botaoProx.setGeometry(20, 20, int(200), 40) 
                        self.botaoProx.move(int(self.x/1.07), int(self.y/1.03))
                    elif visualizarLetra == 2:
                        
                        self.labelExcLetA.adjustSize()
                        self.labelExcLetA.move(int(self.x/1.15), int(-1000))

                        self.imgA.adjustSize()
                        self.imgA.move(int(self.x/2), int(-1000))

                        self.labelLetA.adjustSize()
                        self.labelLetA.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelB.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieB.start()

                        self.labelExcLetB.adjustSize()
                        self.labelExcLetB.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgB.adjustSize()
                        self.imgB.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetB.adjustSize()
                        self.labelLetB.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 3:
                        self.movieB.stop()
                        self.labelB.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetB.adjustSize()
                        self.labelExcLetB.move(int(self.x/1.15), int(-1000))

                        self.imgB.adjustSize()
                        self.imgB.move(int(self.x/2), int(-1000))

                        self.labelLetB.adjustSize()
                        self.labelLetB.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelC.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieC.start()

                        self.labelExcLetC.adjustSize()
                        self.labelExcLetC.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgC.adjustSize()
                        self.imgC.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetC.adjustSize()
                        self.labelLetC.move(int(self.x/1.8), int(self.y/4.2))                    
                    elif visualizarLetra == 4:
                        self.movieC.stop()
                        self.labelC.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetC.adjustSize()
                        self.labelExcLetC.move(int(self.x/1.15), int(-1000))

                        self.imgC.adjustSize()
                        self.imgC.move(int(self.x/2), int(-1000))

                        self.labelLetC.adjustSize()
                        self.labelLetC.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelD.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieD.start()

                        self.labelExcLetD.adjustSize()
                        self.labelExcLetD.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgD.adjustSize()
                        self.imgD.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetD.adjustSize()
                        self.labelLetD.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 5:
                        self.movieD.stop()
                        self.labelD.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetD.adjustSize()
                        self.labelExcLetD.move(int(self.x/1.15), int(-1000))

                        self.imgD.adjustSize()
                        self.imgD.move(int(self.x/2), int(-1000))

                        self.labelLetD.adjustSize()
                        self.labelLetD.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelE.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieE.start()

                        self.labelExcLetE.adjustSize()
                        self.labelExcLetE.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgE.adjustSize()
                        self.imgE.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetE.adjustSize()
                        self.labelLetE.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 6:
                        self.movieE.stop()
                        self.labelE.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetE.adjustSize()
                        self.labelExcLetE.move(int(self.x/1.15), int(-1000))

                        self.imgE.adjustSize()
                        self.imgE.move(int(self.x/2), int(-1000))

                        self.labelLetE.adjustSize()
                        self.labelLetE.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelF.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieF.start()

                        self.labelExcLetF.adjustSize()
                        self.labelExcLetF.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgF.adjustSize()
                        self.imgF.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetF.adjustSize()
                        self.labelLetF.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 7:
                        self.movieF.stop()
                        self.labelF.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetF.adjustSize()
                        self.labelExcLetF.move(int(self.x/1.15), int(-1000))

                        self.imgF.adjustSize()
                        self.imgF.move(int(self.x/2), int(-1000))

                        self.labelLetF.adjustSize()
                        self.labelLetF.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelG.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieG.start()

                        self.labelExcLetG.adjustSize()
                        self.labelExcLetG.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgG.adjustSize()
                        self.imgG.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetG.adjustSize()
                        self.labelLetG.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 8:
                        self.movieG.stop()
                        self.labelG.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetG.adjustSize()
                        self.labelExcLetG.move(int(self.x/1.15), int(-1000))

                        self.imgG.adjustSize()
                        self.imgG.move(int(self.x/2), int(-1000))

                        self.labelLetG.adjustSize()
                        self.labelLetG.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelH.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieH.start()

                        self.labelExcLetH.adjustSize()
                        self.labelExcLetH.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgH1.adjustSize()
                        self.imgH1.move(int(self.x/3), int(self.y/3.5))

                        self.imgH2.adjustSize()
                        self.imgH2.move(int(self.x/2), int(self.y/3.5))

                        self.imgH3.adjustSize()
                        self.imgH3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetH.adjustSize()
                        self.labelLetH.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 9:
                        self.movieH.stop()
                        self.labelH.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetH.adjustSize()
                        self.labelExcLetH.move(int(self.x/1.15), int(-1000))

                        self.imgH1.adjustSize()
                        self.imgH1.move(int(self.x/2), int(-1000))

                        self.imgH2.adjustSize()
                        self.imgH2.move(int(self.x/2), int(-1000))

                        self.imgH3.adjustSize()
                        self.imgH3.move(int(self.x/2), int(-1000))

                        self.labelLetH.adjustSize()
                        self.labelLetH.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelI.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieI.start()

                        self.labelExcLetI.adjustSize()
                        self.labelExcLetI.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgI1.adjustSize()
                        self.imgI1.move(int(self.x/3.2), int(self.y/3.5))

                        self.imgI2.adjustSize()
                        self.imgI2.move(int(self.x/2.25), int(self.y/3.5))

                        self.imgI3.adjustSize()
                        self.imgI3.move(int(self.x/1.74), int(self.y/3.5))

                        self.imgI4.adjustSize()
                        self.imgI4.move(int(self.x/1.42), int(self.y/3.5))

                        self.labelLetI.adjustSize()
                        self.labelLetI.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 10:
                        self.movieI.stop()
                        self.labelI.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetI.adjustSize()
                        self.labelExcLetI.move(int(self.x/1.15), int(-1000))

                        self.imgI1.adjustSize()
                        self.imgI1.move(int(self.x/2), int(-1000))

                        self.imgI2.adjustSize()
                        self.imgI2.move(int(self.x/2), int(-1000))

                        self.imgI3.adjustSize()
                        self.imgI3.move(int(self.x/2), int(-1000))

                        self.imgI4.adjustSize()
                        self.imgI4.move(int(self.x/2), int(-1000))

                        self.labelLetI.adjustSize()
                        self.labelLetI.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieJ.start()

                        self.labelExcLetJ.adjustSize()
                        self.labelExcLetJ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgJ1.adjustSize()
                        self.imgJ1.move(int(self.x/3), int(self.y/3.5))

                        self.imgJ2.adjustSize()
                        self.imgJ2.move(int(self.x/2), int(self.y/3.5))

                        self.imgJ3.adjustSize()
                        self.imgJ3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetJ.adjustSize()
                        self.labelLetJ.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 11:
                        self.movieJ.stop()
                        self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetJ.adjustSize()
                        self.labelExcLetJ.move(int(self.x/1.15), int(-1000))

                        self.imgJ1.adjustSize()
                        self.imgJ1.move(int(self.x/2), int(-1000))

                        self.imgJ2.adjustSize()
                        self.imgJ2.move(int(self.x/2), int(-1000))

                        self.imgJ3.adjustSize()
                        self.imgJ3.move(int(self.x/2), int(-1000))

                        self.labelLetJ.adjustSize()
                        self.labelLetJ.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelK.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieK.start()

                        self.labelExcLetK.adjustSize()
                        self.labelExcLetK.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgK1.adjustSize()
                        self.imgK1.move(int(self.x/3), int(self.y/3.5))

                        self.imgK2.adjustSize()
                        self.imgK2.move(int(self.x/2), int(self.y/3.5))

                        self.imgK3.adjustSize()
                        self.imgK3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetK.adjustSize()
                        self.labelLetK.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 12:
                        self.movieK.stop()
                        self.labelK.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetK.adjustSize()
                        self.labelExcLetK.move(int(self.x/1.15), int(-1000))

                        self.imgK1.adjustSize()
                        self.imgK1.move(int(self.x/2), int(-1000))

                        self.imgK2.adjustSize()
                        self.imgK2.move(int(self.x/2), int(-1000))

                        self.imgK3.adjustSize()
                        self.imgK3.move(int(self.x/2), int(-1000))

                        self.labelLetK.adjustSize()
                        self.labelLetK.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelL.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieL.start()

                        self.labelExcLetL.adjustSize()
                        self.labelExcLetL.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgL.adjustSize()
                        self.imgL.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetL.adjustSize()
                        self.labelLetL.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 13:
                        self.movieL.stop()
                        self.labelL.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetL.adjustSize()
                        self.labelExcLetL.move(int(self.x/1.15), int(-1000))

                        self.imgL.adjustSize()
                        self.imgL.move(int(self.x/2), int(-1000))

                        self.labelLetL.adjustSize()
                        self.labelLetL.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelM.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieM.start()

                        self.labelExcLetM.adjustSize()
                        self.labelExcLetM.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgM.adjustSize()
                        self.imgM.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetM.adjustSize()
                        self.labelLetM.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 14:
                        self.movieM.stop()
                        self.labelM.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetM.adjustSize()
                        self.labelExcLetM.move(int(self.x/1.15), int(-1000))

                        self.imgM.adjustSize()
                        self.imgM.move(int(self.x/2), int(-1000))

                        self.labelLetM.adjustSize()
                        self.labelLetM.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelN.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieN.start()

                        self.labelExcLetN.adjustSize()
                        self.labelExcLetN.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgN.adjustSize()
                        self.imgN.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetN.adjustSize()
                        self.labelLetN.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 15:
                        self.movieN.stop()
                        self.labelN.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetN.adjustSize()
                        self.labelExcLetN.move(int(self.x/1.15), int(-1000))

                        self.imgN.adjustSize()
                        self.imgN.move(int(self.x/2), int(-1000))

                        self.labelLetN.adjustSize()
                        self.labelLetN.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelO.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieO.start()

                        self.labelExcLetO.adjustSize()
                        self.labelExcLetO.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgO.adjustSize()
                        self.imgO.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetO.adjustSize()
                        self.labelLetO.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 16:
                        self.movieO.stop()
                        self.labelO.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetO.adjustSize()
                        self.labelExcLetO.move(int(self.x/1.15), int(-1000))

                        self.imgO.adjustSize()
                        self.imgO.move(int(self.x/2), int(-1000))

                        self.labelLetO.adjustSize()
                        self.labelLetO.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelP.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieP.start()

                        self.labelExcLetP.adjustSize()
                        self.labelExcLetP.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgP.adjustSize()
                        self.imgP.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetP.adjustSize()
                        self.labelLetP.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 17:
                        self.movieP.stop()
                        self.labelP.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetP.adjustSize()
                        self.labelExcLetP.move(int(self.x/1.15), int(-1000))

                        self.imgP.adjustSize()
                        self.imgP.move(int(self.x/2), int(-1000))

                        self.labelLetP.adjustSize()
                        self.labelLetP.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieQ.start()

                        self.labelExcLetQ.adjustSize()
                        self.labelExcLetQ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgQ.adjustSize()
                        self.imgQ.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetQ.adjustSize()
                        self.labelLetQ.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 18:
                        self.movieQ.stop()
                        self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetQ.adjustSize()
                        self.labelExcLetQ.move(int(self.x/1.15), int(-1000))

                        self.imgQ.adjustSize()
                        self.imgQ.move(int(self.x/2), int(-1000))

                        self.labelLetQ.adjustSize()
                        self.labelLetQ.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelR.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieR.start()

                        self.labelExcLetR.adjustSize()
                        self.labelExcLetR.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgR.adjustSize()
                        self.imgR.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetR.adjustSize()
                        self.labelLetR.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 19:
                        self.movieR.stop()
                        self.labelR.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetR.adjustSize()
                        self.labelExcLetR.move(int(self.x/1.15), int(-1000))

                        self.imgR.adjustSize()
                        self.imgR.move(int(self.x/2), int(-1000))

                        self.labelLetR.adjustSize()
                        self.labelLetR.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelS.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieS.start()

                        self.labelExcLetS.adjustSize()
                        self.labelExcLetS.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgS.adjustSize()
                        self.imgS.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetS.adjustSize()
                        self.labelLetS.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 20:
                        self.movieS.stop()
                        self.labelS.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetS.adjustSize()
                        self.labelExcLetS.move(int(self.x/1.15), int(-1000))

                        self.imgS.adjustSize()
                        self.imgS.move(int(self.x/2), int(-1000))

                        self.labelLetS.adjustSize()
                        self.labelLetS.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelT.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieT.start()

                        self.labelExcLetT.adjustSize()
                        self.labelExcLetT.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgT.adjustSize()
                        self.imgT.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetT.adjustSize()
                        self.labelLetT.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 21:
                        self.movieT.stop()
                        self.labelT.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetT.adjustSize()
                        self.labelExcLetT.move(int(self.x/1.15), int(-1000))

                        self.imgT.adjustSize()
                        self.imgT.move(int(self.x/2), int(-1000))

                        self.labelLetT.adjustSize()
                        self.labelLetT.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelU.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieU.start()

                        self.labelExcLetU.adjustSize()
                        self.labelExcLetU.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgU.adjustSize()
                        self.imgU.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetU.adjustSize()
                        self.labelLetU.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 22:
                        self.movieU.stop()
                        self.labelU.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetU.adjustSize()
                        self.labelExcLetU.move(int(self.x/1.15), int(-1000))

                        self.imgU.adjustSize()
                        self.imgU.move(int(self.x/2), int(-1000))

                        self.labelLetU.adjustSize()
                        self.labelLetU.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelV.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieV.start()

                        self.labelExcLetV.adjustSize()
                        self.labelExcLetV.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgV.adjustSize()
                        self.imgV.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetV.adjustSize()
                        self.labelLetV.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 23:
                        self.movieV.stop()
                        self.labelV.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetV.adjustSize()
                        self.labelExcLetV.move(int(self.x/1.15), int(-1000))

                        self.imgV.adjustSize()
                        self.imgV.move(int(self.x/2), int(-1000))

                        self.labelLetV.adjustSize()
                        self.labelLetV.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelW.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieW.start()

                        self.labelExcLetW.adjustSize()
                        self.labelExcLetW.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgW1.adjustSize()
                        self.imgW1.move(int(self.x/3), int(self.y/3.5))

                        self.imgW2.adjustSize()
                        self.imgW2.move(int(self.x/2), int(self.y/3.5))

                        self.imgW3.adjustSize()
                        self.imgW3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetW.adjustSize()
                        self.labelLetW.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 24:
                        self.movieW.stop()
                        self.labelW.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetW.adjustSize()
                        self.labelExcLetW.move(int(self.x/1.15), int(-1000))

                        self.imgW1.adjustSize()
                        self.imgW1.move(int(self.x/2), int(-1000))

                        self.imgW2.adjustSize()
                        self.imgW2.move(int(self.x/2), int(-1000))

                        self.imgW3.adjustSize()
                        self.imgW3.move(int(self.x/2), int(-1000))

                        self.labelLetW.adjustSize()
                        self.labelLetW.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################
                        ###################################################################################################

                        self.labelX.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieX.start()

                        self.labelExcLetX.adjustSize()
                        self.labelExcLetX.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgX3.adjustSize()
                        self.imgX3.move(int(self.x/3), int(self.y/3.5))

                        self.imgX2.adjustSize()
                        self.imgX2.move(int(self.x/2), int(self.y/3.5))

                        self.imgX1.adjustSize()
                        self.imgX1.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetX.adjustSize()
                        self.labelLetX.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 25:
                        self.movieX.stop()
                        self.labelX.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetX.adjustSize()
                        self.labelExcLetX.move(int(self.x/1.15), int(-1000))

                        self.imgX1.adjustSize()
                        self.imgX1.move(int(self.x/2), int(-1000))

                        self.imgX2.adjustSize()
                        self.imgX2.move(int(self.x/2), int(-1000))

                        self.imgX3.adjustSize()
                        self.imgX3.move(int(self.x/2), int(-1000))

                        self.labelLetX.adjustSize()
                        self.labelLetX.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelY.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieY.start()

                        self.labelExcLetY.adjustSize()
                        self.labelExcLetY.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgY1.adjustSize()
                        self.imgY1.move(int(self.x/3), int(self.y/3.5))

                        self.imgY2.adjustSize()
                        self.imgY2.move(int(self.x/2), int(self.y/3.5))

                        self.imgY3.adjustSize()
                        self.imgY3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetY.adjustSize()
                        self.labelLetY.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 26:
                        self.movieY.stop()
                        self.labelY.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetY.adjustSize()
                        self.labelExcLetY.move(int(self.x/1.15), int(-1000))

                        self.imgY1.adjustSize()
                        self.imgY1.move(int(self.x/2), int(-1000))

                        self.imgY2.adjustSize()
                        self.imgY2.move(int(self.x/2), int(-1000))

                        self.imgY3.adjustSize()
                        self.imgY3.move(int(self.x/2), int(-1000))

                        self.labelLetY.adjustSize()
                        self.labelLetY.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieZ.start()

                        self.labelExcLetZ.adjustSize()
                        self.labelExcLetZ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgZ1.adjustSize()
                        self.imgZ1.move(int(self.x/1.7), int(self.y/3.5))

                        self.imgZ2.adjustSize()
                        self.imgZ2.move(int(self.x/2.25), int(self.y/3.5))

                        self.imgZ4.adjustSize()
                        self.imgZ4.move(int(self.x/2.25), int(self.y/1.65))

                        self.imgZ3.adjustSize()
                        self.imgZ3.move(int(self.x/1.7), int(self.y/1.65))

                        self.labelLetZ.adjustSize()
                        self.labelLetZ.move(int(self.x/1.8), int(self.y/4.2))
                    elif visualizarLetra == 27:
                        self.movieZ.stop()
                        self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetZ.adjustSize()
                        self.labelExcLetZ.move(int(self.x/1.15), int(-1000))

                        self.imgZ1.adjustSize()
                        self.imgZ1.move(int(self.x/2), int(-1000))

                        self.imgZ2.adjustSize()
                        self.imgZ2.move(int(self.x/2), int(-1000))

                        self.imgZ3.adjustSize()
                        self.imgZ3.move(int(self.x/2), int(-1000))

                        self.imgZ4.adjustSize()
                        self.imgZ4.move(int(self.x/2), int(-1000))

                        self.labelLetZ.adjustSize()
                        self.labelLetZ.move(int(self.x/1.8), int(-1000))
                        menu_opc2 = 1
                        entrar_opc = 0
                        letra = 'proximo'
                        trav = 1
                if menu_opc2 == 2 and entrar_opc != 1:   
                    QApplication.processEvents()
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/4))
                if menu_opc2 == 3 and entrar_opc != 1:   
                    QApplication.processEvents()                 
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/2.8))                
                if menu_opc2 == 3 and entrar_opc == 1:
                    QApplication.processEvents()
                    self.imgSeta.move(int(-100), int(-100))
                    if cont1 == 0:
                        letra = 'a'
                        cont1 = 1
                        self.op1MenuVisualizarAlfabeto.adjustSize()
                        self.op1MenuVisualizarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuPraticarAlfabeto.adjustSize()
                        self.op1MenuPraticarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuJogar.adjustSize()
                        self.op1MenuJogar.move(int(-100), int(-100))

                        self.op1MenuRecompensas.adjustSize()
                        self.op1MenuRecompensas.move(int(-100), int(-100))

                        self.imgMenu.adjustSize()
                        self.imgMenu.move(int(self.x /3.3), int(-2000))

                        ######################################################################################
                        self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
                        self.movieA.start()

                        self.labelExcLetA.adjustSize()
                        self.labelExcLetA.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgA.adjustSize()
                        self.imgA.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetA.adjustSize()
                        self.labelLetA.move(int(self.x/1.8), int(self.y/4.2))

                        self.botaoProx.adjustSize()
                        self.botaoProx.setGeometry(20, 20, int(200), 40) 
                        self.botaoProx.move(int(self.x/1.07), int(self.y/1.03))
                    troca_opc = 2
                    if menu_opc2_soletra == 2:
                        print('entrou b')
                        letra = 'b'
                        self.movieA.stop()
                        self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetA.adjustSize()
                        self.labelExcLetA.move(int(self.x/1.15), int(-1000))

                        self.imgA.adjustSize()
                        self.imgA.move(int(self.x/2), int(-1000))

                        self.labelLetA.adjustSize()
                        self.labelLetA.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelB.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieB.start()

                        self.labelExcLetB.adjustSize()
                        self.labelExcLetB.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgB.adjustSize()
                        self.imgB.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetB.adjustSize()
                        self.labelLetB.move(int(self.x/1.8), int(self.y/4.2))              
                    if menu_opc2_soletra == 3:
                        print('entrou c')                  
                        letra = 'c'
                        self.movieB.stop()
                        self.labelB.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetB.adjustSize()
                        self.labelExcLetB.move(int(self.x/1.15), int(-1000))

                        self.imgB.adjustSize()
                        self.imgB.move(int(self.x/2), int(-1000))

                        self.labelLetB.adjustSize()
                        self.labelLetB.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelC.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieC.start()

                        self.labelExcLetC.adjustSize()
                        self.labelExcLetC.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgC.adjustSize()
                        self.imgC.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetC.adjustSize()
                        self.labelLetC.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 4:
                        print('entrou d')                  
                        letra = 'd'
                        self.movieC.stop()
                        self.labelC.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetC.adjustSize()
                        self.labelExcLetC.move(int(self.x/1.15), int(-1000))

                        self.imgC.adjustSize()
                        self.imgC.move(int(self.x/2), int(-1000))

                        self.labelLetC.adjustSize()
                        self.labelLetC.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelD.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieD.start()

                        self.labelExcLetD.adjustSize()
                        self.labelExcLetD.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgD.adjustSize()
                        self.imgD.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetD.adjustSize()
                        self.labelLetD.move(int(self.x/1.8), int(self.y/4.2))
                    if menu_opc2_soletra == 5:
                        print('entrou e')                  
                        letra = 'e'
                        self.movieD.stop()
                        self.labelD.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetD.adjustSize()
                        self.labelExcLetD.move(int(self.x/1.15), int(-1000))

                        self.imgD.adjustSize()
                        self.imgD.move(int(self.x/2), int(-1000))

                        self.labelLetD.adjustSize()
                        self.labelLetD.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelE.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieE.start()

                        self.labelExcLetE.adjustSize()
                        self.labelExcLetE.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgE.adjustSize()
                        self.imgE.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetE.adjustSize()
                        self.labelLetE.move(int(self.x/1.8), int(self.y/4.2))
                    if menu_opc2_soletra == 6:
                        print('entrou f')                  
                        letra = 'f'
                        self.movieE.stop()
                        self.labelE.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetE.adjustSize()
                        self.labelExcLetE.move(int(self.x/1.15), int(-1000))

                        self.imgE.adjustSize()
                        self.imgE.move(int(self.x/2), int(-1000))

                        self.labelLetE.adjustSize()
                        self.labelLetE.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelF.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieF.start()

                        self.labelExcLetF.adjustSize()
                        self.labelExcLetF.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgF.adjustSize()
                        self.imgF.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetF.adjustSize()
                        self.labelLetF.move(int(self.x/1.8), int(self.y/4.2))
                    if menu_opc2_soletra == 7:
                        print('entrou g')                  
                        letra = 'g'
                        self.movieF.stop()
                        self.labelF.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetF.adjustSize()
                        self.labelExcLetF.move(int(self.x/1.15), int(-1000))

                        self.imgF.adjustSize()
                        self.imgF.move(int(self.x/2), int(-1000))

                        self.labelLetF.adjustSize()
                        self.labelLetF.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelG.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieG.start()

                        self.labelExcLetG.adjustSize()
                        self.labelExcLetG.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgG.adjustSize()
                        self.imgG.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetG.adjustSize()
                        self.labelLetG.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 8:
                        print('entrou h')                  
                        letra = 'h'
                        self.movieG.stop()
                        self.labelG.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetG.adjustSize()
                        self.labelExcLetG.move(int(self.x/1.15), int(-1000))

                        self.imgG.adjustSize()
                        self.imgG.move(int(self.x/2), int(-1000))

                        self.labelLetG.adjustSize()
                        self.labelLetG.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelH.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieH.start()

                        self.labelExcLetH.adjustSize()
                        self.labelExcLetH.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgH1.adjustSize()
                        self.imgH1.move(int(self.x/3), int(self.y/3.5))

                        self.imgH2.adjustSize()
                        self.imgH2.move(int(self.x/2), int(self.y/3.5))

                        self.imgH3.adjustSize()
                        self.imgH3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetH.adjustSize()
                        self.labelLetH.move(int(self.x/1.8), int(self.y/4.2))                  
                    if menu_opc2_soletra == 9:
                        print('entrou i')                  
                        letra = 'i'
                        self.movieH.stop()
                        self.labelH.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetH.adjustSize()
                        self.labelExcLetH.move(int(self.x/1.15), int(-1000))

                        self.imgH1.adjustSize()
                        self.imgH1.move(int(self.x/2), int(-1000))

                        self.imgH2.adjustSize()
                        self.imgH2.move(int(self.x/2), int(-1000))

                        self.imgH3.adjustSize()
                        self.imgH3.move(int(self.x/2), int(-1000))

                        self.labelLetH.adjustSize()
                        self.labelLetH.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelI.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieI.start()

                        self.labelExcLetI.adjustSize()
                        self.labelExcLetI.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgI1.adjustSize()
                        self.imgI1.move(int(self.x/3.2), int(self.y/3.5))

                        self.imgI2.adjustSize()
                        self.imgI2.move(int(self.x/2.25), int(self.y/3.5))

                        self.imgI3.adjustSize()
                        self.imgI3.move(int(self.x/1.74), int(self.y/3.5))

                        self.imgI4.adjustSize()
                        self.imgI4.move(int(self.x/1.42), int(self.y/3.5))

                        self.labelLetI.adjustSize()
                        self.labelLetI.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 10:
                        print('entrou j')                  
                        letra = 'j'
                        self.movieI.stop()
                        self.labelI.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetI.adjustSize()
                        self.labelExcLetI.move(int(self.x/1.15), int(-1000))

                        self.imgI1.adjustSize()
                        self.imgI1.move(int(self.x/2), int(-1000))

                        self.imgI2.adjustSize()
                        self.imgI2.move(int(self.x/2), int(-1000))

                        self.imgI3.adjustSize()
                        self.imgI3.move(int(self.x/2), int(-1000))

                        self.imgI4.adjustSize()
                        self.imgI4.move(int(self.x/2), int(-1000))

                        self.labelLetI.adjustSize()
                        self.labelLetI.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieJ.start()

                        self.labelExcLetJ.adjustSize()
                        self.labelExcLetJ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgJ1.adjustSize()
                        self.imgJ1.move(int(self.x/3), int(self.y/3.5))

                        self.imgJ2.adjustSize()
                        self.imgJ2.move(int(self.x/2), int(self.y/3.5))

                        self.imgJ3.adjustSize()
                        self.imgJ3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetJ.adjustSize()
                        self.labelLetJ.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 11:
                        print('entrou k')                  
                        letra = 'k'
                        self.movieJ.stop()
                        self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetJ.adjustSize()
                        self.labelExcLetJ.move(int(self.x/1.15), int(-1000))

                        self.imgJ1.adjustSize()
                        self.imgJ1.move(int(self.x/2), int(-1000))

                        self.imgJ2.adjustSize()
                        self.imgJ2.move(int(self.x/2), int(-1000))

                        self.imgJ3.adjustSize()
                        self.imgJ3.move(int(self.x/2), int(-1000))

                        self.labelLetJ.adjustSize()
                        self.labelLetJ.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelK.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieK.start()

                        self.labelExcLetK.adjustSize()
                        self.labelExcLetK.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgK1.adjustSize()
                        self.imgK1.move(int(self.x/3), int(self.y/3.5))

                        self.imgK2.adjustSize()
                        self.imgK2.move(int(self.x/2), int(self.y/3.5))

                        self.imgK3.adjustSize()
                        self.imgK3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetK.adjustSize()
                        self.labelLetK.move(int(self.x/1.8), int(self.y/4.2))                
                    if menu_opc2_soletra == 12:
                        print('entrou l')                  
                        letra = 'l'
                        self.movieK.stop()
                        self.labelK.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetK.adjustSize()
                        self.labelExcLetK.move(int(self.x/1.15), int(-1000))

                        self.imgK1.adjustSize()
                        self.imgK1.move(int(self.x/2), int(-1000))

                        self.imgK2.adjustSize()
                        self.imgK2.move(int(self.x/2), int(-1000))

                        self.imgK3.adjustSize()
                        self.imgK3.move(int(self.x/2), int(-1000))

                        self.labelLetK.adjustSize()
                        self.labelLetK.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelL.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieL.start()

                        self.labelExcLetL.adjustSize()
                        self.labelExcLetL.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgL.adjustSize()
                        self.imgL.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetL.adjustSize()
                        self.labelLetL.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 13:
                        print('entrou m')                  
                        letra = 'm'
                        self.movieL.stop()
                        self.labelL.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetL.adjustSize()
                        self.labelExcLetL.move(int(self.x/1.15), int(-1000))

                        self.imgL.adjustSize()
                        self.imgL.move(int(self.x/2), int(-1000))

                        self.labelLetL.adjustSize()
                        self.labelLetL.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelM.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieM.start()

                        self.labelExcLetM.adjustSize()
                        self.labelExcLetM.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgM.adjustSize()
                        self.imgM.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetM.adjustSize()
                        self.labelLetM.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 14:
                        print('entrou n')                  
                        letra = 'n'
                        self.movieM.stop()
                        self.labelM.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetM.adjustSize()
                        self.labelExcLetM.move(int(self.x/1.15), int(-1000))

                        self.imgM.adjustSize()
                        self.imgM.move(int(self.x/2), int(-1000))

                        self.labelLetM.adjustSize()
                        self.labelLetM.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelN.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieN.start()

                        self.labelExcLetN.adjustSize()
                        self.labelExcLetN.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgN.adjustSize()
                        self.imgN.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetN.adjustSize()
                        self.labelLetN.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 15:
                        print('entrou o')                  
                        letra = 'o'
                        self.movieN.stop()
                        self.labelN.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetN.adjustSize()
                        self.labelExcLetN.move(int(self.x/1.15), int(-1000))

                        self.imgN.adjustSize()
                        self.imgN.move(int(self.x/2), int(-1000))

                        self.labelLetN.adjustSize()
                        self.labelLetN.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelO.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieO.start()

                        self.labelExcLetO.adjustSize()
                        self.labelExcLetO.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgO.adjustSize()
                        self.imgO.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetO.adjustSize()
                        self.labelLetO.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 16:
                        print('entrou p')                  
                        letra = 'p'
                        self.movieO.stop()
                        self.labelO.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetO.adjustSize()
                        self.labelExcLetO.move(int(self.x/1.15), int(-1000))

                        self.imgO.adjustSize()
                        self.imgO.move(int(self.x/2), int(-1000))

                        self.labelLetO.adjustSize()
                        self.labelLetO.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelP.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieP.start()

                        self.labelExcLetP.adjustSize()
                        self.labelExcLetP.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgP.adjustSize()
                        self.imgP.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetP.adjustSize()
                        self.labelLetP.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 17:
                        print('entrou q')                  
                        letra = 'q'
                        self.movieP.stop()
                        self.labelP.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetP.adjustSize()
                        self.labelExcLetP.move(int(self.x/1.15), int(-1000))

                        self.imgP.adjustSize()
                        self.imgP.move(int(self.x/2), int(-1000))

                        self.labelLetP.adjustSize()
                        self.labelLetP.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieQ.start()

                        self.labelExcLetQ.adjustSize()
                        self.labelExcLetQ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgQ.adjustSize()
                        self.imgQ.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetQ.adjustSize()
                        self.labelLetQ.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 18:
                        print('entrou r')                  
                        letra = 'r'
                        self.movieQ.stop()
                        self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetQ.adjustSize()
                        self.labelExcLetQ.move(int(self.x/1.15), int(-1000))

                        self.imgQ.adjustSize()
                        self.imgQ.move(int(self.x/2), int(-1000))

                        self.labelLetQ.adjustSize()
                        self.labelLetQ.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelR.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieR.start()

                        self.labelExcLetR.adjustSize()
                        self.labelExcLetR.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgR.adjustSize()
                        self.imgR.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetR.adjustSize()
                        self.labelLetR.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 19:
                        print('entrou s')                  
                        letra = 's'
                        self.movieR.stop()
                        self.labelR.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetR.adjustSize()
                        self.labelExcLetR.move(int(self.x/1.15), int(-1000))

                        self.imgR.adjustSize()
                        self.imgR.move(int(self.x/2), int(-1000))

                        self.labelLetR.adjustSize()
                        self.labelLetR.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelS.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieS.start()

                        self.labelExcLetS.adjustSize()
                        self.labelExcLetS.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgS.adjustSize()
                        self.imgS.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetS.adjustSize()
                        self.labelLetS.move(int(self.x/1.8), int(self.y/4.2))
                    if menu_opc2_soletra == 20:
                        print('entrou t')                  
                        letra = 't'
                        self.movieS.stop()
                        self.labelS.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetS.adjustSize()
                        self.labelExcLetS.move(int(self.x/1.15), int(-1000))

                        self.imgS.adjustSize()
                        self.imgS.move(int(self.x/2), int(-1000))

                        self.labelLetS.adjustSize()
                        self.labelLetS.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelT.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieT.start()

                        self.labelExcLetT.adjustSize()
                        self.labelExcLetT.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgT.adjustSize()
                        self.imgT.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetT.adjustSize()
                        self.labelLetT.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 21:
                        print('entrou u')                  
                        letra = 'u'
                        self.movieT.stop()
                        self.labelT.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetT.adjustSize()
                        self.labelExcLetT.move(int(self.x/1.15), int(-1000))

                        self.imgT.adjustSize()
                        self.imgT.move(int(self.x/2), int(-1000))

                        self.labelLetT.adjustSize()
                        self.labelLetT.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelU.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieU.start()

                        self.labelExcLetU.adjustSize()
                        self.labelExcLetU.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgU.adjustSize()
                        self.imgU.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetU.adjustSize()
                        self.labelLetU.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 22:
                        print('entrou v')                  
                        letra = 'v'
                        self.movieU.stop()
                        self.labelU.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetU.adjustSize()
                        self.labelExcLetU.move(int(self.x/1.15), int(-1000))

                        self.imgU.adjustSize()
                        self.imgU.move(int(self.x/2), int(-1000))

                        self.labelLetU.adjustSize()
                        self.labelLetU.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelV.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieV.start()

                        self.labelExcLetV.adjustSize()
                        self.labelExcLetV.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgV.adjustSize()
                        self.imgV.move(int(self.x/2), int(self.y/3.5))

                        self.labelLetV.adjustSize()
                        self.labelLetV.move(int(self.x/1.8), int(self.y/4.2))                 
                    if menu_opc2_soletra == 23:
                        print('entrou w')                  
                        letra = 'w'
                        self.movieV.stop()
                        self.labelV.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetV.adjustSize()
                        self.labelExcLetV.move(int(self.x/1.15), int(-1000))

                        self.imgV.adjustSize()
                        self.imgV.move(int(self.x/2), int(-1000))

                        self.labelLetV.adjustSize()
                        self.labelLetV.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelW.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieW.start()

                        self.labelExcLetW.adjustSize()
                        self.labelExcLetW.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgW1.adjustSize()
                        self.imgW1.move(int(self.x/3), int(self.y/3.5))

                        self.imgW2.adjustSize()
                        self.imgW2.move(int(self.x/2), int(self.y/3.5))

                        self.imgW3.adjustSize()
                        self.imgW3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetW.adjustSize()
                        self.labelLetW.move(int(self.x/1.8), int(self.y/4.2))                    
                    if menu_opc2_soletra == 24:
                        print('entrou x')                  
                        letra = 'x'
                        self.movieW.stop()
                        self.labelW.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetW.adjustSize()
                        self.labelExcLetW.move(int(self.x/1.15), int(-1000))

                        self.imgW1.adjustSize()
                        self.imgW1.move(int(self.x/2), int(-1000))

                        self.imgW2.adjustSize()
                        self.imgW2.move(int(self.x/2), int(-1000))

                        self.imgW3.adjustSize()
                        self.imgW3.move(int(self.x/2), int(-1000))

                        self.labelLetW.adjustSize()
                        self.labelLetW.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################
                        ###################################################################################################

                        self.labelX.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieX.start()

                        self.labelExcLetX.adjustSize()
                        self.labelExcLetX.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgX3.adjustSize()
                        self.imgX3.move(int(self.x/3), int(self.y/3.5))

                        self.imgX2.adjustSize()
                        self.imgX2.move(int(self.x/2), int(self.y/3.5))

                        self.imgX1.adjustSize()
                        self.imgX1.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetX.adjustSize()
                        self.labelLetX.move(int(self.x/1.8), int(self.y/4.2))                   
                    if menu_opc2_soletra == 25:
                        print('entrou y')                  
                        letra = 'y'
                        self.movieX.stop()
                        self.labelX.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetX.adjustSize()
                        self.labelExcLetX.move(int(self.x/1.15), int(-1000))

                        self.imgX1.adjustSize()
                        self.imgX1.move(int(self.x/2), int(-1000))

                        self.imgX2.adjustSize()
                        self.imgX2.move(int(self.x/2), int(-1000))

                        self.imgX3.adjustSize()
                        self.imgX3.move(int(self.x/2), int(-1000))

                        self.labelLetX.adjustSize()
                        self.labelLetX.move(int(self.x/1.8), int(-1000))
                        ###################################################################################################

                        self.labelY.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieY.start()

                        self.labelExcLetY.adjustSize()
                        self.labelExcLetY.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgY1.adjustSize()
                        self.imgY1.move(int(self.x/3), int(self.y/3.5))

                        self.imgY2.adjustSize()
                        self.imgY2.move(int(self.x/2), int(self.y/3.5))

                        self.imgY3.adjustSize()
                        self.imgY3.move(int(self.x/1.5), int(self.y/3.5))

                        self.labelLetY.adjustSize()
                        self.labelLetY.move(int(self.x/1.8), int(self.y/4.2))         
                    if menu_opc2_soletra == 26:
                        print('entrou z')                  
                        letra = 'z'
                        self.movieY.stop()
                        self.labelY.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetY.adjustSize()
                        self.labelExcLetY.move(int(self.x/1.15), int(-1000))

                        self.imgY1.adjustSize()
                        self.imgY1.move(int(self.x/2), int(-1000))

                        self.imgY2.adjustSize()
                        self.imgY2.move(int(self.x/2), int(-1000))

                        self.imgY3.adjustSize()
                        self.imgY3.move(int(self.x/2), int(-1000))

                        self.labelLetY.adjustSize()
                        self.labelLetY.move(int(self.x/1.8), int(-1000))

                        ###################################################################################################

                        self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                        self.movieZ.start()

                        self.labelExcLetZ.adjustSize()
                        self.labelExcLetZ.move(int(self.x/1.15), int(self.y/4.2))

                        self.imgZ1.adjustSize()
                        self.imgZ1.move(int(self.x/1.7), int(self.y/3.5))

                        self.imgZ2.adjustSize()
                        self.imgZ2.move(int(self.x/2.25), int(self.y/3.5))

                        self.imgZ4.adjustSize()
                        self.imgZ4.move(int(self.x/2.25), int(self.y/1.65))

                        self.imgZ3.adjustSize()
                        self.imgZ3.move(int(self.x/1.7), int(self.y/1.65))

                        self.labelLetZ.adjustSize()
                        self.labelLetZ.move(int(self.x/1.8), int(self.y/4.2))
                    if menu_opc2_soletra == 27:
                        self.movieZ.stop()
                        self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetZ.adjustSize()
                        self.labelExcLetZ.move(int(self.x/1.15), int(-1000))

                        self.imgZ1.adjustSize()
                        self.imgZ1.move(int(self.x/2), int(-1000))

                        self.imgZ2.adjustSize()
                        self.imgZ2.move(int(self.x/2), int(-1000))

                        self.imgZ3.adjustSize()
                        self.imgZ3.move(int(self.x/2), int(-1000))

                        self.imgZ4.adjustSize()
                        self.imgZ4.move(int(self.x/2), int(-1000))

                        self.labelLetZ.adjustSize()
                        self.labelLetZ.move(int(self.x/1.8), int(-1000))
                        print('entrou sair')                  
                        menu_opc2 = 1
                        entrar_opc = 0
                        letra = 'proximo'
                        menu_opc2_soletra = 0
                        cont1 = 0             
                if menu_opc2 == 4 and entrar_opc != 1:   
                    QApplication.processEvents()
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/2.15))
                if menu_opc2 == 4 and entrar_opc == 1:
                    troca_opc = 2
                    QApplication.processEvents()
                    if confirmacaoMenuOpcNivel == 0:
                        if entr1vez  == 0:
                            letra = 'proximo3'
                            entr1vez = 1
                        troca_opc = 2
                        #print("entrei opc 4") 

                        ## Limpando tela anterior
                        self.imgSeta.move(int(-100), int(-100))

                        self.op1MenuVisualizarAlfabeto.adjustSize()
                        self.op1MenuVisualizarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuPraticarAlfabeto.adjustSize()
                        self.op1MenuPraticarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuJogar.adjustSize()
                        self.op1MenuJogar.move(int(-100), int(-100))

                        self.op1MenuRecompensas.adjustSize()
                        self.op1MenuRecompensas.move(int(-100), int(-100))

                        self.imgMenu.adjustSize()
                        self.imgMenu.move(int(self.x /3.3), int(-2000))
                        

                        ## Chamando os Botoes do menu
                        self.menuNivelDificuldadeFacil.adjustSize()
                        self.menuNivelDificuldadeFacil.setGeometry(900, 900, int(self.x/1.7), 90) 
                        self.menuNivelDificuldadeFacil.move(int(self.x/2.5), int(self.y/4))

                        self.menuNivelDificuldadeMedio.adjustSize()
                        self.menuNivelDificuldadeMedio.setGeometry(900, 900, int(self.x/1.7), 90) 
                        self.menuNivelDificuldadeMedio.move(int(self.x/2.5), int(self.y/2.8))

                        self.menuNivelDificuldadeDificil.adjustSize()
                        self.menuNivelDificuldadeDificil.setGeometry(900, 900, int(self.x/1.7), 90) 
                        self.menuNivelDificuldadeDificil.move(int(self.x/2.5), int(self.y/2.15))

                        ##Abrindo Imagem da tela Jogar
                        self.imgTelaInicio.setGeometry(int(self.x/3.3), 0,0, 0)
                        self.imgTelaInicio.adjustSize()
                    if confirmacaoMenuOpcNivel == 1:
                            ## limpando tela
                            self.menuNivelDificuldadeFacil.adjustSize()
                            self.menuNivelDificuldadeFacil.setGeometry(900, 900, int(self.x/1.7), 90) 
                            self.menuNivelDificuldadeFacil.move(-1000, -1000)

                            self.menuNivelDificuldadeMedio.adjustSize()
                            self.menuNivelDificuldadeMedio.setGeometry(900, 900, int(self.x/1.7), 90) 
                            self.menuNivelDificuldadeMedio.move(-1000, -1000)

                            self.menuNivelDificuldadeDificil.adjustSize()
                            self.menuNivelDificuldadeDificil.setGeometry(900, 900, int(self.x/1.7), 90) 
                            self.menuNivelDificuldadeDificil.move(-1000, -1000)

                            self.imgTelaInicio.setGeometry(-10000, -10000,-10000, -10000)
                            self.imgTelaInicio.adjustSize()
                    if menu_opc3 == 1 :
                        
                        ## Sobre a tela
                        if True:
                            #print('Menu op3 == 1')
                            if confirmacaoMenuOpcNivel == 0:
                                #QApplication.processEvents()
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(int(self.x/3), int(self.y/4))
                            if confirmacaoMenuOpcNivel == 1:
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(-1000, -1000)
                                
                                if estagio == 1:                                   
                                    self.imgTelaInicio.setGeometry(int(self.x/3.3), 0,0, 0)
                                    self.imgTelaInicio.adjustSize()
                                    if resetePontos == 1:
                                        contadorPonto = 0
                                        resetePontos = 0
                                    if contadorPonto > 60:
                                        letra = 'next'
                                        trocaLetra = 1                                        
                                    if letra  == 'next':
                                        if contadorPonto <= 3:
                                            somatorioPontos = somatorioPontos + 10
                                        elif contadorPonto <= 6:
                                            somatorioPontos = somatorioPontos + 8
                                        elif contadorPonto <= 9:
                                            somatorioPontos = somatorioPontos + 6
                                        elif contadorPonto <= 15:
                                            somatorioPontos = somatorioPontos + 4
                                        elif contadorPonto <= 60:
                                            somatorioPontos = somatorioPontos + 2
                                        elif contadorPonto > 60:
                                            somatorioPontos = somatorioPontos + 1
                                            contadorPonto = 0                                       
                                    if trocaLetra == 1 and estagio == 1:
                                        letraRemover = letraPrintar
                                        trocaLetra = 0
                                        contAux = contAux + 1
                                    if contAux == tamanhoPalavra:
                                        estagio = 2
                                        tamanhoPalavra = (len(palavraNivelFacilInicio))
                                        palavraSub = str(palavraNivelFacilInicio)
                                        result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                        
                                        letraRemover = unidecode.unidecode(result.lower()) 
                                        letraPrintar = ''
                                        self.nivelFacilPalavra1.move(-10000, -10000)
                                        contAux = 0
                                    else:    
                                        self.nivelFacilPalavra1.move(int(self.x/2), int(self.y/50))
                                        tamanhoPalavra = (len(palavraNivelFacilInicio))
                                        palavraSub = str(palavraNivelFacilInicio)
                                        result = palavraSub[-(tamanhoPalavra - contAux)]
                                        #print(result)
                                        letra = unidecode.unidecode(result.lower())
                                        letraPrintar = unidecode.unidecode(result.lower())
                                        #print('entrou')
                                elif estagio == 2:
                                    self.imgTelaInicio.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaInicio.adjustSize()
                                    ## faseInicio ,faseMeio , faseFim , faseChefao
                                    trs = QTransform().rotate(180)
                                    self.imgTelaMeioSalaRei.setPixmap(QPixmap(self.enderecoimgTelaMeioSalaRei).transformed(trs))
                                    if faseMeio == 'sala_principal':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_jantar':
                                        self.imgTelaMeioSalaJantar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_rei':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
          
                                    if resetePontos == 1:
                                        contadorPonto = 0
                                        resetePontos = 0
                                    if contadorPonto > 60:
                                        letra = 'next'
                                        trocaLetra = 1                                        
                                    if letra  == 'next':
                                        if contadorPonto <= 3:
                                            somatorioPontos = somatorioPontos + 10
                                        elif contadorPonto <= 6:
                                            somatorioPontos = somatorioPontos + 8
                                        elif contadorPonto <= 9:
                                            somatorioPontos = somatorioPontos + 6
                                        elif contadorPonto <= 15:
                                            somatorioPontos = somatorioPontos + 4
                                        elif contadorPonto <= 60:
                                            somatorioPontos = somatorioPontos + 2
                                        elif contadorPonto > 60:
                                            somatorioPontos = somatorioPontos + 1
                                            contadorPonto = 0
                                    
                                    if estagio2 == 1:
                                        
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio2 = 2
                                            tamanhoPalavra = (len(palavraNivelFacilMeio[0]))
                                            palavraSub = str(palavraNivelFacilMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelFacilPalavra2.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelFacilPalavra2.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelFacilMeio[0]))
                                            palavraSub = str(palavraNivelFacilMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio2 == 2:
                                       
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 3
                                            tamanhoPalavra = (len(palavraNivelFacilMeio[1]))
                                            palavraSub = str(palavraNivelFacilMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelFacilPalavra3.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelFacilPalavra3.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelFacilMeio[1]))
                                            palavraSub = str(palavraNivelFacilMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                elif estagio == 3:
                                    self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaJantar.adjustSize()

                                    self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaRei.adjustSize()

                                    self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaEstar.adjustSize()


                                    if faseFim == 'torre_com_armamento':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()


                                        self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_princesa':
                                        self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_dragao':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()
                                    if resetePontos == 1:
                                        contadorPonto = 0
                                        resetePontos = 0
                                    if contadorPonto > 60:
                                        letra = 'next'
                                        trocaLetra = 1                                        
                                    if letra  == 'next':
                                        if contadorPonto <= 3:
                                            somatorioPontos = somatorioPontos + 10
                                        elif contadorPonto <= 6:
                                            somatorioPontos = somatorioPontos + 8
                                        elif contadorPonto <= 9:
                                            somatorioPontos = somatorioPontos + 6
                                        elif contadorPonto <= 15:
                                            somatorioPontos = somatorioPontos + 4
                                        elif contadorPonto <= 60:
                                            somatorioPontos = somatorioPontos + 2
                                        elif contadorPonto > 60:
                                            somatorioPontos = somatorioPontos + 1
                                            contadorPonto = 0
                                    if estagio3 == 1:
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 2
                                            tamanhoPalavra = (len(palavraNivelFacilFim[0]))
                                            palavraSub = str(palavraNivelFacilFim[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelFacilPalavra4.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelFacilPalavra4.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelFacilFim[0]))
                                            palavraSub = str(palavraNivelFacilFim[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio3 == 2:
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 1
                                            menu_opc2 = 1
                                            entrar_opc = 0
                                            letra = 'proximo'
                                            trav = 1
                                            confirmacaoMenuOpcNivel = 0
                                            entr1vez  = 0
                                            menu_opc3 = 0
                                            tamanhoPalavra = (len(palavraNivelFacilFim[1]))
                                            palavraSub = str(palavraNivelFacilFim[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelFacilPalavra5.move(-10000, -10000)
                                            contAux = 0
                                            resetePontos = 1


                                            data_e_hora_atuais = datetime.now()
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                            arquivo = 'ranks.txt'
                                            teste_arquivo_exist = os.path.exists(arquivo)
                                            if teste_arquivo_exist == False:
                                                arquivo = open('ranks.txt', 'w')
                                                arquivo.close()
                                            conteudo = ('Nome: '+ nomeJogador + ' , Fase: Princesa , Modalidade: Facil , Pontos: ' + str(somatorioPontos) + ' , Dia: ' +
                                                        data_e_hora_em_texto)   # insira seu conteúdo
                                            arquivo = open("ranks.txt", "a")
                                            arquivo.write('\n' + conteudo)
                                            arquivo.close()
                                            
                                            somatorioPontos = 0

                                        else:    
                                            self.nivelFacilPalavra5.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelFacilFim[1]))
                                            palavraSub = str(palavraNivelFacilFim[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')

                        ## Limpar a letra anteriror
                        if True:
                            
                            if letraRemover == 'a':
                                self.movieA.stop()
                                self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetA.adjustSize()
                                self.labelExcLetA.move(int(self.x/1.15), int(-1000))

                                self.imgA.adjustSize()
                                self.imgA.move(int(self.x/2), int(-1000))

                                self.labelLetA.adjustSize()
                                self.labelLetA.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'b':
                                self.movieB.stop()
                                self.labelB.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetB.adjustSize()
                                self.labelExcLetB.move(int(self.x/1.15), int(-1000))

                                self.imgB.adjustSize()
                                self.imgB.move(int(self.x/2), int(-1000))

                                self.labelLetB.adjustSize()
                                self.labelLetB.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'c':
                                self.movieC.stop()
                                self.labelC.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetC.adjustSize()
                                self.labelExcLetC.move(int(self.x/1.15), int(-1000))

                                self.imgC.adjustSize()
                                self.imgC.move(int(self.x/2), int(-1000))

                                self.labelLetC.adjustSize()
                                self.labelLetC.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'd':
                                self.movieD.stop()
                                self.labelD.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetD.adjustSize()
                                self.labelExcLetD.move(int(self.x/1.15), int(-1000))

                                self.imgD.adjustSize()
                                self.imgD.move(int(self.x/2), int(-1000))

                                self.labelLetD.adjustSize()
                                self.labelLetD.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'e':
                                self.movieE.stop()
                                self.labelE.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetE.adjustSize()
                                self.labelExcLetE.move(int(self.x/1.15), int(-1000))

                                self.imgE.adjustSize()
                                self.imgE.move(int(self.x/2), int(-1000))

                                self.labelLetE.adjustSize()
                                self.labelLetE.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'f':
                                self.movieF.stop()
                                self.labelF.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetF.adjustSize()
                                self.labelExcLetF.move(int(self.x/1.15), int(-1000))

                                self.imgF.adjustSize()
                                self.imgF.move(int(self.x/2), int(-1000))

                                self.labelLetF.adjustSize()
                                self.labelLetF.move(int(self.x/1.8), int(-1000)) 
                            elif letraRemover == 'g':
                                self.movieG.stop()
                                self.labelG.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetG.adjustSize()
                                self.labelExcLetG.move(int(self.x/1.15), int(-1000))

                                self.imgG.adjustSize()
                                self.imgG.move(int(self.x/2), int(-1000))

                                self.labelLetG.adjustSize()
                                self.labelLetG.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'h':
                                self.movieH.stop()
                                self.labelH.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetH.adjustSize()
                                self.labelExcLetH.move(int(self.x/1.15), int(-1000))

                                self.imgH1.adjustSize()
                                self.imgH1.move(int(self.x/2), int(-1000))

                                self.imgH2.adjustSize()
                                self.imgH2.move(int(self.x/2), int(-1000))

                                self.imgH3.adjustSize()
                                self.imgH3.move(int(self.x/2), int(-1000))

                                self.labelLetH.adjustSize()
                                self.labelLetH.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'i':
                                self.movieI.stop()
                                self.labelI.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetI.adjustSize()
                                self.labelExcLetI.move(int(self.x/1.15), int(-1000))

                                self.imgI1.adjustSize()
                                self.imgI1.move(int(self.x/2), int(-1000))

                                self.imgI2.adjustSize()
                                self.imgI2.move(int(self.x/2), int(-1000))

                                self.imgI3.adjustSize()
                                self.imgI3.move(int(self.x/2), int(-1000))

                                self.imgI4.adjustSize()
                                self.imgI4.move(int(self.x/2), int(-1000))

                                self.labelLetI.adjustSize()
                                self.labelLetI.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'j':
                                self.movieJ.stop()
                                self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetJ.adjustSize()
                                self.labelExcLetJ.move(int(self.x/1.15), int(-1000))

                                self.imgJ1.adjustSize()
                                self.imgJ1.move(int(self.x/2), int(-1000))

                                self.imgJ2.adjustSize()
                                self.imgJ2.move(int(self.x/2), int(-1000))

                                self.imgJ3.adjustSize()
                                self.imgJ3.move(int(self.x/2), int(-1000))

                                self.labelLetJ.adjustSize()
                                self.labelLetJ.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'k':
                                self.movieK.stop()
                                self.labelK.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetK.adjustSize()
                                self.labelExcLetK.move(int(self.x/1.15), int(-1000))

                                self.imgK1.adjustSize()
                                self.imgK1.move(int(self.x/2), int(-1000))

                                self.imgK2.adjustSize()
                                self.imgK2.move(int(self.x/2), int(-1000))

                                self.imgK3.adjustSize()
                                self.imgK3.move(int(self.x/2), int(-1000))

                                self.labelLetK.adjustSize()
                                self.labelLetK.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'l':
                                self.movieL.stop()
                                self.labelL.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetL.adjustSize()
                                self.labelExcLetL.move(int(self.x/1.15), int(-1000))

                                self.imgL.adjustSize()
                                self.imgL.move(int(self.x/2), int(-1000))

                                self.labelLetL.adjustSize()
                                self.labelLetL.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'm':
                                self.movieM.stop()
                                self.labelM.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetM.adjustSize()
                                self.labelExcLetM.move(int(self.x/1.15), int(-1000))

                                self.imgM.adjustSize()
                                self.imgM.move(int(self.x/2), int(-1000))

                                self.labelLetM.adjustSize()
                                self.labelLetM.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'n':
                                self.movieN.stop()
                                self.labelN.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetN.adjustSize()
                                self.labelExcLetN.move(int(self.x/1.15), int(-1000))

                                self.imgN.adjustSize()
                                self.imgN.move(int(self.x/2), int(-1000))

                                self.labelLetN.adjustSize()
                                self.labelLetN.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'o':
                                self.movieO.stop()
                                self.labelO.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetO.adjustSize()
                                self.labelExcLetO.move(int(self.x/1.15), int(-1000))

                                self.imgO.adjustSize()
                                self.imgO.move(int(self.x/2), int(-1000))

                                self.labelLetO.adjustSize()
                                self.labelLetO.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'p':
                                self.movieP.stop()
                                self.labelP.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetP.adjustSize()
                                self.labelExcLetP.move(int(self.x/1.15), int(-1000))

                                self.imgP.adjustSize()
                                self.imgP.move(int(self.x/2), int(-1000))

                                self.labelLetP.adjustSize()
                                self.labelLetP.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'q':
                                self.movieQ.stop()
                                self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetQ.adjustSize()
                                self.labelExcLetQ.move(int(self.x/1.15), int(-1000))

                                self.imgQ.adjustSize()
                                self.imgQ.move(int(self.x/2), int(-1000))

                                self.labelLetQ.adjustSize()
                                self.labelLetQ.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'r':
                                self.movieR.stop()
                                self.labelR.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetR.adjustSize()
                                self.labelExcLetR.move(int(self.x/1.15), int(-1000))

                                self.imgR.adjustSize()
                                self.imgR.move(int(self.x/2), int(-1000))

                                self.labelLetR.adjustSize()
                                self.labelLetR.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 's':
                                self.movieS.stop()
                                self.labelS.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetS.adjustSize()
                                self.labelExcLetS.move(int(self.x/1.15), int(-1000))

                                self.imgS.adjustSize()
                                self.imgS.move(int(self.x/2), int(-1000))

                                self.labelLetS.adjustSize()
                                self.labelLetS.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 't':
                                self.movieT.stop()
                                self.labelT.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetT.adjustSize()
                                self.labelExcLetT.move(int(self.x/1.15), int(-1000))

                                self.imgT.adjustSize()
                                self.imgT.move(int(self.x/2), int(-1000))

                                self.labelLetT.adjustSize()
                                self.labelLetT.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'u':
                                self.movieU.stop()
                                self.labelU.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetU.adjustSize()
                                self.labelExcLetU.move(int(self.x/1.15), int(-1000))

                                self.imgU.adjustSize()
                                self.imgU.move(int(self.x/2), int(-1000))

                                self.labelLetU.adjustSize()
                                self.labelLetU.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'v':
                                self.movieV.stop()
                                self.labelV.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetV.adjustSize()
                                self.labelExcLetV.move(int(self.x/1.15), int(-1000))

                                self.imgV.adjustSize()
                                self.imgV.move(int(self.x/2), int(-1000))

                                self.labelLetV.adjustSize()
                                self.labelLetV.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'w':
                                self.movieW.stop()
                                self.labelW.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetW.adjustSize()
                                self.labelExcLetW.move(int(self.x/1.15), int(-1000))

                                self.imgW1.adjustSize()
                                self.imgW1.move(int(self.x/2), int(-1000))

                                self.imgW2.adjustSize()
                                self.imgW2.move(int(self.x/2), int(-1000))

                                self.imgW3.adjustSize()
                                self.imgW3.move(int(self.x/2), int(-1000))

                                self.labelLetW.adjustSize()
                                self.labelLetW.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'x':
                                self.movieX.stop()
                                self.labelX.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetX.adjustSize()
                                self.labelExcLetX.move(int(self.x/1.15), int(-1000))

                                self.imgX1.adjustSize()
                                self.imgX1.move(int(self.x/2), int(-1000))

                                self.imgX2.adjustSize()
                                self.imgX2.move(int(self.x/2), int(-1000))

                                self.imgX3.adjustSize()
                                self.imgX3.move(int(self.x/2), int(-1000))

                                self.labelLetX.adjustSize()
                                self.labelLetX.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'y':
                                self.movieY.stop()
                                self.labelY.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetY.adjustSize()
                                self.labelExcLetY.move(int(self.x/1.15), int(-1000))

                                self.imgY1.adjustSize()
                                self.imgY1.move(int(self.x/2), int(-1000))

                                self.imgY2.adjustSize()
                                self.imgY2.move(int(self.x/2), int(-1000))

                                self.imgY3.adjustSize()
                                self.imgY3.move(int(self.x/2), int(-1000))

                                self.labelLetY.adjustSize()
                                self.labelLetY.move(int(self.x/1.8), int(-1000))
                            elif letraRemover == 'z':
                                self.movieZ.stop()
                                self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                                self.labelExcLetZ.adjustSize()
                                self.labelExcLetZ.move(int(self.x/1.15), int(-1000))

                                self.imgZ1.adjustSize()
                                self.imgZ1.move(int(self.x/2), int(-1000))

                                self.imgZ2.adjustSize()
                                self.imgZ2.move(int(self.x/2), int(-1000))

                                self.imgZ3.adjustSize()
                                self.imgZ3.move(int(self.x/2), int(-1000))

                                self.imgZ4.adjustSize()
                                self.imgZ4.move(int(self.x/2), int(-1000))

                                self.labelLetZ.adjustSize()
                                self.labelLetZ.move(int(self.x/1.8), int(-1000))
                        ## printar a letra
                        if True:
                            if letraPrintar == 'a':
                                self.labelA.setGeometry(QtCore.QRect(int(self.x/1.2), int(self.y/3.5), 600, 600))
                                self.movieA.start()

                                self.imgA.adjustSize()
                                self.imgA.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'b':
                                self.labelB.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieB.start()

                                self.imgB.adjustSize()
                                self.imgB.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'c':
                                self.labelC.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieC.start()

                                self.imgC.adjustSize()
                                self.imgC.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'd':
                                self.labelD.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieD.start()

                                self.imgD.adjustSize()
                                self.imgD.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'e':
                                self.labelE.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieE.start()

                                self.imgE.adjustSize()
                                self.imgE.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'f':
                                self.labelF.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieF.start()

                                self.imgF.adjustSize()
                                self.imgF.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'g':
                                self.labelG.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieG.start()

                                self.imgG.adjustSize()
                                self.imgG.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'h':
                                self.labelH.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieH.start()

                                self.imgH1.adjustSize()
                                self.imgH1.move(int(self.x/3), int(self.y/3.5))

                                self.imgH2.adjustSize()
                                self.imgH2.move(int(self.x/2), int(self.y/3.5))

                                self.imgH3.adjustSize()
                                self.imgH3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'i':
                                self.labelI.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieI.start()

                                self.imgI1.adjustSize()
                                self.imgI1.move(int(self.x/3.2), int(self.y/3.5))

                                self.imgI2.adjustSize()
                                self.imgI2.move(int(self.x/2.25), int(self.y/3.5))

                                self.imgI3.adjustSize()
                                self.imgI3.move(int(self.x/1.74), int(self.y/3.5))

                                self.imgI4.adjustSize()
                                self.imgI4.move(int(self.x/1.42), int(self.y/3.5))
                            elif letraPrintar == 'j':
                                self.labelJ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieJ.start()

                                self.imgJ1.adjustSize()
                                self.imgJ1.move(int(self.x/3), int(self.y/3.5))

                                self.imgJ2.adjustSize()
                                self.imgJ2.move(int(self.x/2), int(self.y/3.5))

                                self.imgJ3.adjustSize()
                                self.imgJ3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'k':
                                self.labelK.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieK.start()

                                self.imgK1.adjustSize()
                                self.imgK1.move(int(self.x/3), int(self.y/3.5))

                                self.imgK2.adjustSize()
                                self.imgK2.move(int(self.x/2), int(self.y/3.5))

                                self.imgK3.adjustSize()
                                self.imgK3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'l':
                                self.labelL.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieL.start()

                                self.imgL.adjustSize()
                                self.imgL.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'm':
                                self.labelM.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieM.start()

                                self.imgM.adjustSize()
                                self.imgM.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'n':
                                self.labelN.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieN.start()

                                self.imgN.adjustSize()
                                self.imgN.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'o':
                                self.labelO.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieO.start()

                                self.imgO.adjustSize()
                                self.imgO.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'p':
                                self.labelP.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieP.start()

                                self.imgP.adjustSize()
                                self.imgP.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'q':
                                self.labelQ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieQ.start()

                                self.imgQ.adjustSize()
                                self.imgQ.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'r':
                                self.labelR.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieR.start()

                                self.imgR.adjustSize()
                                self.imgR.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 's':
                                self.labelS.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieS.start()

                                self.imgS.adjustSize()
                                self.imgS.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 't':
                                self.labelT.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieT.start()

                                self.imgT.adjustSize()
                                self.imgT.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'u':
                                self.labelU.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieU.start()

                                self.imgU.adjustSize()
                                self.imgU.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'v':
                                self.labelV.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieV.start()

                                self.imgV.adjustSize()
                                self.imgV.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'w':
                                self.labelW.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieW.start()

                                self.imgW1.adjustSize()
                                self.imgW1.move(int(self.x/3), int(self.y/3.5))

                                self.imgW2.adjustSize()
                                self.imgW2.move(int(self.x/2), int(self.y/3.5))

                                self.imgW3.adjustSize()
                                self.imgW3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'x':
                                self.labelX.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieX.start()

                                self.imgX3.adjustSize()
                                self.imgX3.move(int(self.x/3), int(self.y/3.5))

                                self.imgX2.adjustSize()
                                self.imgX2.move(int(self.x/2), int(self.y/3.5))

                                self.imgX1.adjustSize()
                                self.imgX1.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'y':
                                self.labelY.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieY.start()

                                self.imgY1.adjustSize()
                                self.imgY1.move(int(self.x/3), int(self.y/3.5))

                                self.imgY2.adjustSize()
                                self.imgY2.move(int(self.x/2), int(self.y/3.5))

                                self.imgY3.adjustSize()
                                self.imgY3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'z': 
                                self.labelZ.setGeometry(QtCore.QRect(int(self.x/1.18), int(self.y/3.5), 600, 600))
                                self.movieZ.start()

                                self.imgZ1.adjustSize()
                                self.imgZ1.move(int(self.x/1.7), int(self.y/3.5))

                                self.imgZ2.adjustSize()
                                self.imgZ2.move(int(self.x/2.25), int(self.y/3.5))

                                self.imgZ4.adjustSize()
                                self.imgZ4.move(int(self.x/2.25), int(self.y/1.65))

                                self.imgZ3.adjustSize()
                                self.imgZ3.move(int(self.x/1.7), int(self.y/1.65))
      
                    if menu_opc3 == 2 :
                        ##Opc gerais
                        if True:
                            #print('Menu op3 == 2')
                            if confirmacaoMenuOpcNivel == 0:
                                #QApplication.processEvents()                 
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(int(self.x/3), int(self.y/2.8))

                            if confirmacaoMenuOpcNivel == 1:
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(-1000, -1000)

                                if estagio == 1:
                                    self.imgTelaInicio.setGeometry(int(self.x/3.3), 0,0, 0)
                                    self.imgTelaInicio.adjustSize()
                                    if estagio1 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio1 = 2
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[0]))
                                            palavraSub = str(palavraNivelMedioInicio[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra1.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra1.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[0]))
                                            palavraSub = str(palavraNivelMedioInicio[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio1 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio1 = 3
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[1]))
                                            palavraSub = str(palavraNivelMedioInicio[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra2.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra2.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[1]))
                                            palavraSub = str(palavraNivelMedioInicio[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio1 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio1 = 4
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[2]))
                                            palavraSub = str(palavraNivelMedioInicio[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra3.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra3.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[2]))
                                            palavraSub = str(palavraNivelMedioInicio[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                            # teste
                                    elif estagio1 == 4:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 4:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 2
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[3]))
                                            palavraSub = str(palavraNivelMedioInicio[3])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra4.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra4.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioInicio[3]))
                                            palavraSub = str(palavraNivelMedioInicio[3])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                elif estagio == 2:
                                    self.imgTelaInicio.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaInicio.adjustSize()
                                    ## faseInicio ,faseMeio , faseFim , faseChefao

                                    if faseMeio == 'sala_principal':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_jantar':
                                        self.imgTelaMeioSalaJantar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_rei':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if estagio2 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio2 = 2
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[0]))
                                            palavraSub = str(palavraNivelMedioMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra5.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra5.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[0]))
                                            palavraSub = str(palavraNivelMedioMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio2 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio2 = 3
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[1]))
                                            palavraSub = str(palavraNivelMedioMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra6.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra6.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[1]))
                                            palavraSub = str(palavraNivelMedioMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio2 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 3
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[2]))
                                            palavraSub = str(palavraNivelMedioMeio[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra7.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra7.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioMeio[2]))
                                            palavraSub = str(palavraNivelMedioMeio[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                elif estagio == 3:
                                    self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaJantar.adjustSize()

                                    self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaRei.adjustSize()

                                    self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaEstar.adjustSize()


                                    if faseFim == 'torre_com_armamento':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()


                                        self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_princesa':
                                        self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_dragao':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()
                                    if estagio3 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 2
                                            tamanhoPalavra = (len(palavraNivelMedioFim[0]))
                                            palavraSub = str(palavraNivelMedioFim[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra8.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra8.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioFim[0]))
                                            palavraSub = str(palavraNivelMedioFim[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio3 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 3
                                            tamanhoPalavra = (len(palavraNivelMedioFim[1]))
                                            palavraSub = str(palavraNivelMedioFim[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra9.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelMedioPalavra9.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioFim[1]))
                                            palavraSub = str(palavraNivelMedioFim[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    
                                    elif estagio3 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 15
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 9
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 6
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 3
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 1
                                            menu_opc2 = 1
                                            entrar_opc = 0
                                            letra = 'proximo'
                                            trav = 1
                                            confirmacaoMenuOpcNivel = 0
                                            entr1vez  = 0
                                            menu_opc3 = 0
                                            tamanhoPalavra = (len(palavraNivelMedioFim[2]))
                                            palavraSub = str(palavraNivelMedioFim[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelMedioPalavra10.move(-10000, -10000)
                                            contAux = 0

                                            resetePontos = 1

                                            data_e_hora_atuais = datetime.now()
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                            arquivo = 'ranks.txt'
                                            teste_arquivo_exist = os.path.exists(arquivo)
                                            if teste_arquivo_exist == False:
                                                arquivo = open('ranks.txt', 'w')
                                                arquivo.close()
                                            conteudo = ('Nome: '+ nomeJogador + ' , Fase: Princesa , Modalidade: Medio , Pontos: ' + str(somatorioPontos) + ' , Dia: ' +
                                                        data_e_hora_em_texto)   # insira seu conteúdo
                                            arquivo = open("ranks.txt", "a")
                                            arquivo.write('\n' + conteudo)
                                            arquivo.close()
                                            
                                            somatorioPontos = 0
                                        else:    
                                            self.nivelMedioPalavra10.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelMedioFim[2]))
                                            palavraSub = str(palavraNivelMedioFim[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                        ##Limpar letra
                        if True:
                            if letraRemover == 'a':
                                self.imgA.adjustSize()
                                self.imgA.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'b':
                                

                                self.imgB.adjustSize()
                                self.imgB.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'c':
                                self.imgC.adjustSize()
                                self.imgC.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'd':
                                self.imgD.adjustSize()
                                self.imgD.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'e':
                                self.imgE.adjustSize()
                                self.imgE.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'f':
                                self.imgF.adjustSize()
                                self.imgF.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'g':
                                self.imgG.adjustSize()
                                self.imgG.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'h':
                                self.imgH1.adjustSize()
                                self.imgH1.move(int(self.x/2), int(-1000))

                                self.imgH2.adjustSize()
                                self.imgH2.move(int(self.x/2), int(-1000))

                                self.imgH3.adjustSize()
                                self.imgH3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'i':
                                self.imgI1.adjustSize()
                                self.imgI1.move(int(self.x/2), int(-1000))

                                self.imgI2.adjustSize()
                                self.imgI2.move(int(self.x/2), int(-1000))

                                self.imgI3.adjustSize()
                                self.imgI3.move(int(self.x/2), int(-1000))

                                self.imgI4.adjustSize()
                                self.imgI4.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'j':
                                self.imgJ1.adjustSize()
                                self.imgJ1.move(int(self.x/2), int(-1000))

                                self.imgJ2.adjustSize()
                                self.imgJ2.move(int(self.x/2), int(-1000))

                                self.imgJ3.adjustSize()
                                self.imgJ3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'k':
                                self.imgK1.adjustSize()
                                self.imgK1.move(int(self.x/2), int(-1000))

                                self.imgK2.adjustSize()
                                self.imgK2.move(int(self.x/2), int(-1000))

                                self.imgK3.adjustSize()
                                self.imgK3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'l':
                                self.imgL.adjustSize()
                                self.imgL.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'm':
                                self.imgM.adjustSize()
                                self.imgM.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'n':
                                self.imgN.adjustSize()
                                self.imgN.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'o':
                                self.imgO.adjustSize()
                                self.imgO.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'p':
                                self.imgP.adjustSize()
                                self.imgP.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'q':
                                self.imgQ.adjustSize()
                                self.imgQ.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'r':
                                self.imgR.adjustSize()
                                self.imgR.move(int(self.x/2), int(-1000))
                            elif letraRemover == 's':
                                self.imgS.adjustSize()
                                self.imgS.move(int(self.x/2), int(-1000))
                            elif letraRemover == 't':
                                self.imgT.adjustSize()
                                self.imgT.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'u':
                                self.imgU.adjustSize()
                                self.imgU.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'v':
                                self.imgV.adjustSize()
                                self.imgV.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'w':
                                self.imgW1.adjustSize()
                                self.imgW1.move(int(self.x/2), int(-1000))

                                self.imgW2.adjustSize()
                                self.imgW2.move(int(self.x/2), int(-1000))

                                self.imgW3.adjustSize()
                                self.imgW3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'x':
                                self.imgX1.adjustSize()
                                self.imgX1.move(int(self.x/2), int(-1000))

                                self.imgX2.adjustSize()
                                self.imgX2.move(int(self.x/2), int(-1000))

                                self.imgX3.adjustSize()
                                self.imgX3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'y':
                                self.imgY1.adjustSize()
                                self.imgY1.move(int(self.x/2), int(-1000))

                                self.imgY2.adjustSize()
                                self.imgY2.move(int(self.x/2), int(-1000))

                                self.imgY3.adjustSize()
                                self.imgY3.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'z':
                                self.imgZ1.adjustSize()
                                self.imgZ1.move(int(self.x/2), int(-1000))

                                self.imgZ2.adjustSize()
                                self.imgZ2.move(int(self.x/2), int(-1000))

                                self.imgZ3.adjustSize()
                                self.imgZ3.move(int(self.x/2), int(-1000))

                                self.imgZ4.adjustSize()
                                self.imgZ4.move(int(self.x/2), int(-1000))
                        ## printar a letra
                        if True:
                            if letraPrintar == 'a':
                                self.imgA.adjustSize()
                                self.imgA.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'b':
                                self.imgB.adjustSize()
                                self.imgB.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'c':
                                self.imgC.adjustSize()
                                self.imgC.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'd':
                                self.imgD.adjustSize()
                                self.imgD.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'e':
                                self.imgE.adjustSize()
                                self.imgE.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'f':
                                self.imgF.adjustSize()
                                self.imgF.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'g':
                                self.imgG.adjustSize()
                                self.imgG.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'h':
                                self.imgH1.adjustSize()
                                self.imgH1.move(int(self.x/3), int(self.y/3.5))

                                self.imgH2.adjustSize()
                                self.imgH2.move(int(self.x/2), int(self.y/3.5))

                                self.imgH3.adjustSize()
                                self.imgH3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'i':
                                self.imgI1.adjustSize()
                                self.imgI1.move(int(self.x/3.2), int(self.y/3.5))

                                self.imgI2.adjustSize()
                                self.imgI2.move(int(self.x/2.25), int(self.y/3.5))

                                self.imgI3.adjustSize()
                                self.imgI3.move(int(self.x/1.74), int(self.y/3.5))

                                self.imgI4.adjustSize()
                                self.imgI4.move(int(self.x/1.42), int(self.y/3.5))
                            elif letraPrintar == 'j':
                                self.imgJ1.adjustSize()
                                self.imgJ1.move(int(self.x/3), int(self.y/3.5))

                                self.imgJ2.adjustSize()
                                self.imgJ2.move(int(self.x/2), int(self.y/3.5))

                                self.imgJ3.adjustSize()
                                self.imgJ3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'k':
                                self.imgK1.adjustSize()
                                self.imgK1.move(int(self.x/3), int(self.y/3.5))

                                self.imgK2.adjustSize()
                                self.imgK2.move(int(self.x/2), int(self.y/3.5))

                                self.imgK3.adjustSize()
                                self.imgK3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'l':
                                self.imgL.adjustSize()
                                self.imgL.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'm':
                                self.imgM.adjustSize()
                                self.imgM.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'n':
                                self.imgN.adjustSize()
                                self.imgN.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'o':
                                self.imgO.adjustSize()
                                self.imgO.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'p':
                                self.imgP.adjustSize()
                                self.imgP.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'q':
                                self.imgQ.adjustSize()
                                self.imgQ.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'r':
                                self.imgR.adjustSize()
                                self.imgR.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 's':
                                self.imgS.adjustSize()
                                self.imgS.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 't':
                                self.imgT.adjustSize()
                                self.imgT.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'u':
                                self.imgU.adjustSize()
                                self.imgU.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'v':
                                self.imgV.adjustSize()
                                self.imgV.move(int(self.x/2), int(self.y/3.5))
                            elif letraPrintar == 'w':
                                self.imgW1.adjustSize()
                                self.imgW1.move(int(self.x/3), int(self.y/3.5))

                                self.imgW2.adjustSize()
                                self.imgW2.move(int(self.x/2), int(self.y/3.5))

                                self.imgW3.adjustSize()
                                self.imgW3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'x':
                                self.imgX3.adjustSize()
                                self.imgX3.move(int(self.x/3), int(self.y/3.5))

                                self.imgX2.adjustSize()
                                self.imgX2.move(int(self.x/2), int(self.y/3.5))

                                self.imgX1.adjustSize()
                                self.imgX1.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'y':
                                self.imgY1.adjustSize()
                                self.imgY1.move(int(self.x/3), int(self.y/3.5))

                                self.imgY2.adjustSize()
                                self.imgY2.move(int(self.x/2), int(self.y/3.5))

                                self.imgY3.adjustSize()
                                self.imgY3.move(int(self.x/1.5), int(self.y/3.5))
                            elif letraPrintar == 'z': 
                                self.imgZ1.adjustSize()
                                self.imgZ1.move(int(self.x/1.7), int(self.y/3.5))

                                self.imgZ2.adjustSize()
                                self.imgZ2.move(int(self.x/2.25), int(self.y/3.5))

                                self.imgZ4.adjustSize()
                                self.imgZ4.move(int(self.x/2.25), int(self.y/1.65))

                                self.imgZ3.adjustSize()
                                self.imgZ3.move(int(self.x/1.7), int(self.y/1.65))
                    if menu_opc3 == 3 :
                        ##opcoes gerais
                        if True:
                            if confirmacaoMenuOpcNivel == 0:
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(int(self.x/3), int(self.y/2.15))
                            if confirmacaoMenuOpcNivel == 1:
                                self.imgSeta.adjustSize()
                                self.imgSeta.move(-1000, -1000)                               
                                if estagio == 1:
                                    self.imgTelaInicio.setGeometry(int(self.x/3.3), 0,0, 0)
                                    self.imgTelaInicio.adjustSize()
                                    if estagio1 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0                                      
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio1 = 2
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[0]))
                                            palavraSub = str(palavraNivelDificilInicio[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra1.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra1.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[0]))
                                            palavraSub = str(palavraNivelDificilInicio[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio1 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio1 = 3
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[1]))
                                            palavraSub = str(palavraNivelDificilInicio[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra2.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra2.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[1]))
                                            palavraSub = str(palavraNivelDificilInicio[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio1 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 1 and estagio1 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 2
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[2]))
                                            palavraSub = str(palavraNivelDificilInicio[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra3.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra3.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilInicio[2]))
                                            palavraSub = str(palavraNivelDificilInicio[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')         
                                elif estagio == 2:
                                    self.imgTelaInicio.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaInicio.adjustSize()
                                    ## faseInicio ,faseMeio , faseFim , faseChefao

                                    if faseMeio == 'sala_principal':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_jantar':
                                        self.imgTelaMeioSalaJantar.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if faseMeio == 'sala_rei':
                                        self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaJantar.adjustSize()

                                        self.imgTelaMeioSalaRei.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaMeioSalaRei.adjustSize()

                                        self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                        self.imgTelaMeioSalaEstar.adjustSize()
                                    if estagio2 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio2 = 2
                                            tamanhoPalavra = len(palavraNivelDificilMeio[0])
                                            palavraSub = str(palavraNivelDificilMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra4.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra4.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilMeio[0]))
                                            palavraSub = str(palavraNivelDificilMeio[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio2 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio2 = 3
                                            tamanhoPalavra = (len(palavraNivelDificilMeio[1]))
                                            palavraSub = str(palavraNivelDificilMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra5.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra5.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilMeio[1]))
                                            palavraSub = str(palavraNivelDificilMeio[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio2 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 2 and estagio2 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 3
                                            tamanhoPalavra = (len(palavraNivelDificilMeio[2]))
                                            palavraSub = str(palavraNivelDificilMeio[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra6.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra6.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilMeio[2]))
                                            palavraSub = str(palavraNivelDificilMeio[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                elif estagio == 3:
                                    self.imgTelaMeioSalaJantar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaJantar.adjustSize()

                                    self.imgTelaMeioSalaRei.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaRei.adjustSize()

                                    self.imgTelaMeioSalaEstar.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaMeioSalaEstar.adjustSize()


                                    if faseFim == 'torre_com_armamento':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()


                                        self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_princesa':
                                        self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()

                                    if faseFim == 'torre_com_dragao':
                                        self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimPrincesa.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimPrincesa.adjustSize()

                                        self.imgTelaFimDragao.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimDragao.adjustSize()

                                        self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                        ##self.imgTelaFimArmamento.setGeometry(int(self.x/3.3), 0,0, 0)
                                        self.imgTelaFimArmamento.adjustSize()
                                    if estagio3 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 2
                                            tamanhoPalavra = (len(palavraNivelDificilFim[0]))
                                            palavraSub = str(palavraNivelDificilFim[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra7.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra7.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilFim[0]))
                                            palavraSub = str(palavraNivelDificilFim[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio3 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 3
                                            tamanhoPalavra = (len(palavraNivelDificilFim[1]))
                                            palavraSub = str(palavraNivelDificilFim[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra8.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra8.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilFim[1]))
                                            palavraSub = str(palavraNivelDificilFim[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio3 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio3 = 4
                                            tamanhoPalavra = (len(palavraNivelDificilFim[2]))
                                            palavraSub = str(palavraNivelDificilFim[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra9.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra9.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilFim[2]))
                                            palavraSub = str(palavraNivelDificilFim[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    elif estagio3 == 4:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 60:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 3:
                                                somatorioPontos = somatorioPontos + 20
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 16
                                            elif contadorPonto <= 9:
                                                somatorioPontos = somatorioPontos + 12
                                            elif contadorPonto <= 15:
                                                somatorioPontos = somatorioPontos + 8
                                            elif contadorPonto <= 60:
                                                somatorioPontos = somatorioPontos + 4
                                            elif contadorPonto > 60:
                                                somatorioPontos = somatorioPontos + 1
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 3 and estagio3 == 4:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 4
                                            tamanhoPalavra = (len(palavraNivelDificilFim[3]))
                                            palavraSub = str(palavraNivelDificilFim[3])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra10.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra10.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(palavraNivelDificilFim[3]))
                                            palavraSub = str(palavraNivelDificilFim[3])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                elif estagio == 4:
                                    self.imgTelaFimPrincesa.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaFimPrincesa.adjustSize()

                                    self.imgTelaFimDragao.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaFimDragao.adjustSize()

                                    self.imgTelaFimArmamento.setGeometry(-10000,-10000,-10000, -10000)
                                    self.imgTelaFimArmamento.adjustSize()

                                    self.imgTelaChefao.setGeometry(int(self.x/3.3), 0,0, 0)
                                    self.imgTelaChefao.adjustSize()

                                    if estagio4 == 1:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 10:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 4:
                                                somatorioPontos = somatorioPontos + 40
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 32
                                            elif contadorPonto <= 10:
                                                somatorioPontos = somatorioPontos + 24
                                            elif contadorPonto > 10:
                                                somatorioPontos = somatorioPontos + (-2000)
                                                contadorPonto = 0 
                                        if trocaLetra == 1 and estagio == 4 and estagio4 == 1:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio4 = 2
                                            tamanhoPalavra = (len(vetChefao[0]))
                                            palavraSub = str(vetChefao[0])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra11.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra11.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(vetChefao[0]))
                                            palavraSub = str(vetChefao[0])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    if estagio4 == 2:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 10:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 4:
                                                somatorioPontos = somatorioPontos + 40
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 32
                                            elif contadorPonto <= 10:
                                                somatorioPontos = somatorioPontos + 24
                                            elif contadorPonto > 10:
                                                somatorioPontos = somatorioPontos + (-2000)
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 4 and estagio4 == 2:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio4 = 3
                                            tamanhoPalavra = (len(vetChefao[1]))
                                            palavraSub = str(vetChefao[1])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra12.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra12.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(vetChefao[1]))
                                            palavraSub = str(vetChefao[1])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    if estagio4 == 3:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 10:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 4:
                                                somatorioPontos = somatorioPontos + 40
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 32
                                            elif contadorPonto <= 10:
                                                somatorioPontos = somatorioPontos + 24
                                            elif contadorPonto > 10:
                                                somatorioPontos = somatorioPontos + (-2000)
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 4 and estagio4 == 3:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio4 = 4
                                            tamanhoPalavra = (len(vetChefao[2]))
                                            palavraSub = str(vetChefao[2])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra13.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra13.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(vetChefao[2]))
                                            palavraSub = str(vetChefao[2])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    if estagio4 == 4:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 10:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 4:
                                                somatorioPontos = somatorioPontos + 40
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 32
                                            elif contadorPonto <= 10:
                                                somatorioPontos = somatorioPontos + 24
                                            elif contadorPonto > 10:
                                                somatorioPontos = somatorioPontos + (-2000)
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 4 and estagio4 == 4:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio4 = 5
                                            tamanhoPalavra = (len(vetChefao[3]))
                                            palavraSub = str(vetChefao[3])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra14.move(-10000, -10000)
                                            contAux = 0
                                        else:    
                                            self.nivelDificilPalavra14.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(vetChefao[3]))
                                            palavraSub = str(vetChefao[3])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                                    if estagio4 == 5:
                                        if resetePontos == 1:
                                            contadorPonto = 0
                                            resetePontos = 0
                                        if contadorPonto > 10:
                                            letra = 'next'
                                            trocaLetra = 1                                        
                                        if letra  == 'next':
                                            if contadorPonto <= 4:
                                                somatorioPontos = somatorioPontos + 40
                                            elif contadorPonto <= 6:
                                                somatorioPontos = somatorioPontos + 32
                                            elif contadorPonto <= 10:
                                                somatorioPontos = somatorioPontos + 24
                                            elif contadorPonto > 10:
                                                somatorioPontos = somatorioPontos + (-2000)
                                                contadorPonto = 0
                                        if trocaLetra == 1 and estagio == 4 and estagio4 == 5:
                                            letraRemover = letraPrintar
                                            trocaLetra = 0
                                            contAux = contAux + 1
                                        if contAux == tamanhoPalavra:
                                            estagio = 1
                                            menu_opc2 = 1
                                            entrar_opc = 0
                                            letra = 'proximo'
                                            trav = 1
                                            confirmacaoMenuOpcNivel = 0
                                            entr1vez  = 0
                                            menu_opc3 = 0
                                            tamanhoPalavra = (len(vetChefao[4]))
                                            palavraSub = str(vetChefao[4])
                                            result = palavraSub[-(tamanhoPalavra - (contAux - 1))]
                                            
                                            letraRemover = unidecode.unidecode(result.lower()) 
                                            letraPrintar = ''
                                            self.nivelDificilPalavra15.move(-10000, -10000)
                                            contAux = 0

                                            self.imgTelaChefao.setGeometry(-10000,-10000,-10000, -10000)
                                            self.imgTelaChefao.adjustSize()

                                            resetePontos = 1

                                            data_e_hora_atuais = datetime.now()
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
                                            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
                                            arquivo = 'ranks.txt'
                                            teste_arquivo_exist = os.path.exists(arquivo)
                                            if teste_arquivo_exist == False:
                                                arquivo = open('ranks.txt', 'w')
                                                arquivo.close()
                                            conteudo = ('Nome: '+ nomeJogador + ' , Fase: Princesa , Modalidade: Dificil , Pontos: ' + str(somatorioPontos) + ' , Dia: ' +
                                                        data_e_hora_em_texto)   # insira seu conteúdo
                                            arquivo = open("ranks.txt", "a")
                                            arquivo.write('\n' + conteudo)
                                            arquivo.close()
                                            
                                            somatorioPontos = 0
                                        else:    
                                            self.nivelDificilPalavra15.move(int(self.x/2), int(self.y/50))
                                            tamanhoPalavra = (len(vetChefao[4]))
                                            palavraSub = str(vetChefao[4])
                                            result = palavraSub[-(tamanhoPalavra - contAux)]
                                            #print(result)
                                            letra = unidecode.unidecode(result.lower())
                                            letraPrintar = unidecode.unidecode(result.lower())
                                            #print('entrou')
                        ##Limpar letra
                        if True:
                            if letraRemover == 'a':
                                self.letraModalidadeDificilA.adjustSize()
                                self.letraModalidadeDificilA.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'b':
                                self.letraModalidadeDificilB.adjustSize()
                                self.letraModalidadeDificilB.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'c':
                                self.letraModalidadeDificilC.adjustSize()
                                self.letraModalidadeDificilC.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'd':
                                self.letraModalidadeDificilD.adjustSize()
                                self.letraModalidadeDificilD.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'e':
                                self.letraModalidadeDificilE.adjustSize()
                                self.letraModalidadeDificilE.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'f':
                                self.letraModalidadeDificilF.adjustSize()
                                self.letraModalidadeDificilF.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'g':
                                self.letraModalidadeDificilG.adjustSize()
                                self.letraModalidadeDificilG.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'h':
                                self.letraModalidadeDificilH.adjustSize()
                                self.letraModalidadeDificilH.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'i':
                                self.letraModalidadeDificilI.adjustSize()
                                self.letraModalidadeDificilI.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'j':
                                self.letraModalidadeDificilJ.adjustSize()
                                self.letraModalidadeDificilJ.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'k':
                                self.letraModalidadeDificilK.adjustSize()
                                self.letraModalidadeDificilK.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'l':
                                self.letraModalidadeDificilL.adjustSize()
                                self.letraModalidadeDificilL.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'm':
                                self.letraModalidadeDificilM.adjustSize()
                                self.letraModalidadeDificilM.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'n':
                                self.letraModalidadeDificilN.adjustSize()
                                self.letraModalidadeDificilN.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'o':
                                self.letraModalidadeDificilO.adjustSize()
                                self.letraModalidadeDificilO.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'p':
                                self.letraModalidadeDificilP.adjustSize()
                                self.letraModalidadeDificilP.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'q':
                                self.letraModalidadeDificilQ.adjustSize()
                                self.letraModalidadeDificilQ.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'r':
                                self.letraModalidadeDificilR.adjustSize()
                                self.letraModalidadeDificilR.move(int(self.x/2), int(-1000))
                            elif letraRemover == 's':
                                self.letraModalidadeDificilS.adjustSize()
                                self.letraModalidadeDificilS.move(int(self.x/2), int(-1000))
                            elif letraRemover == 't':
                                self.letraModalidadeDificilT.adjustSize()
                                self.letraModalidadeDificilT.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'u':
                                self.letraModalidadeDificilU.adjustSize()
                                self.letraModalidadeDificilU.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'v':
                                self.letraModalidadeDificilV.adjustSize()
                                self.letraModalidadeDificilV.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'w':
                                self.letraModalidadeDificilW.adjustSize()
                                self.letraModalidadeDificilW.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'x':
                                self.letraModalidadeDificilX.adjustSize()
                                self.letraModalidadeDificilX.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'y':
                                self.letraModalidadeDificilY.adjustSize()
                                self.letraModalidadeDificilY.move(int(self.x/2), int(-1000))
                            elif letraRemover == 'z':
                                self.letraModalidadeDificilZ.adjustSize()
                                self.letraModalidadeDificilZ.move(int(self.x/2), int(-1000))
                        ## printar a letra
                        if True:
                            if letraPrintar == 'a':
                                self.letraModalidadeDificilA.adjustSize()
                                self.letraModalidadeDificilA.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'b':
                                self.letraModalidadeDificilB.adjustSize()
                                self.letraModalidadeDificilB.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'c':
                                self.letraModalidadeDificilC.adjustSize()
                                self.letraModalidadeDificilC.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'd':
                                self.letraModalidadeDificilD.adjustSize()
                                self.letraModalidadeDificilD.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'e':
                                self.letraModalidadeDificilE.adjustSize()
                                self.letraModalidadeDificilE.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'f':
                                self.letraModalidadeDificilF.adjustSize()
                                self.letraModalidadeDificilF.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'g':
                                self.letraModalidadeDificilG.adjustSize()
                                self.letraModalidadeDificilG.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'h':
                                self.letraModalidadeDificilH.adjustSize()
                                self.letraModalidadeDificilH.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'i':
                                self.letraModalidadeDificilI.adjustSize()
                                self.letraModalidadeDificilI.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'j':
                                self.letraModalidadeDificilJ.adjustSize()
                                self.letraModalidadeDificilJ.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'k':
                                self.letraModalidadeDificilK.adjustSize()
                                self.letraModalidadeDificilK.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'l':
                                self.letraModalidadeDificilL.adjustSize()
                                self.letraModalidadeDificilL.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'm':
                                self.letraModalidadeDificilM.adjustSize()
                                self.letraModalidadeDificilM.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'n':
                                self.letraModalidadeDificilN.adjustSize()
                                self.letraModalidadeDificilN.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'o':
                                self.letraModalidadeDificilO.adjustSize()
                                self.letraModalidadeDificilO.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'p':
                                self.letraModalidadeDificilP.adjustSize()
                                self.letraModalidadeDificilP.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'q':
                                self.letraModalidadeDificilQ.adjustSize()
                                self.letraModalidadeDificilQ.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'r':
                                self.letraModalidadeDificilR.adjustSize()
                                self.letraModalidadeDificilR.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 's':
                                self.letraModalidadeDificilS.adjustSize()
                                self.letraModalidadeDificilS.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 't':
                                self.letraModalidadeDificilT.adjustSize()
                                self.letraModalidadeDificilT.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'u':
                                self.letraModalidadeDificilU.adjustSize()
                                self.letraModalidadeDificilU.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'v':
                                self.letraModalidadeDificilV.adjustSize()
                                self.letraModalidadeDificilV.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'w':
                                self.letraModalidadeDificilW.adjustSize()
                                self.letraModalidadeDificilW.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'x':
                                self.letraModalidadeDificilX.adjustSize()
                                self.letraModalidadeDificilX.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'y':
                                self.letraModalidadeDificilY.adjustSize()
                                self.letraModalidadeDificilY.move(int(self.x/1.6), int(self.y/3.5))
                            elif letraPrintar == 'z': 
                                self.letraModalidadeDificilZ.adjustSize()
                                self.letraModalidadeDificilZ.move(int(self.x/1.6), int(self.y/3.5))
                    if menu_opc3 == 'sair':
                        menu_opc3 = 0
                        entr1vez = 0
                        confirmacaoMenuOpcNivel = 0
                if menu_opc2 == 5 and entrar_opc != 1:   
                    QApplication.processEvents()
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/1.74))

                if menu_opc2 == 5 and entrar_opc == 1:
                    QApplication.processEvents()
                    print("entrei opc 5") 
                    if True:
                        letra = 'voltar'

                        self.imgSeta.move(int(-100), int(-100))
                        


                        entrar_1_vez = 1
                        self.imgSeta.move(int(-100), int(-100))

                        self.op1MenuVisualizarAlfabeto.adjustSize()
                        self.op1MenuVisualizarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuPraticarAlfabeto.adjustSize()
                        self.op1MenuPraticarAlfabeto.move(int(-100), int(-100))

                        self.op1MenuJogar.adjustSize()
                        self.op1MenuJogar.move(int(-100), int(-100))

                        self.op1MenuRecompensas.adjustSize()
                        self.op1MenuRecompensas.move(int(-100), int(-100))

                        self.imgMenu.adjustSize()
                        self.imgMenu.move(int(self.x /3.3), int(-2000))

                        self.ranks.adjustSize()
                        self.ranks.move(int(self.x/1.7), int(self.y/5))

                        self.tabelaRanks.adjustSize()
                        self.tabelaRanks.move(int(self.x/2.9), int(self.y/3))
                        troca_opc = 2
                    if voltarMenu == 'sair':
                        self.tabelaRanks.adjustSize()
                        self.tabelaRanks.move(-5000, -5000)
                        self.ranks.adjustSize()
                        self.ranks.move(-500, -500)
                        menu_opc2 = 1
                        troca_opc = 0
                        entrar_opc = 0
                        letra = 'proximo'
                        cont1 = 0
                        voltarMenu = 'null'
            if menu_opc1 == 5:
                QApplication.processEvents()
                self.labelPricipalMovimentaoBotes.adjustSize()
                self.labelPricipalMovimentaoBotes.move(int(self.x), int(self.y/2.6))

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        contador = 0
        reducao = 1
        global menu_opc1 , menu_opc2 , dentro_menu_opc2, entrar_opc , troca_opc, visualizarLetra,menu_opc2_soletra, letra , voltarMenu,menu_opc3, confirmacaoMenuOpcNivel,trocaLetra,contadorPonto 
        letra_Momento = 'Iniciando'
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
                            if reducao == 1:
                                ###################################################################################
                                # Ponto 4 do dedao
                                dedao_x_4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
                                dedao_y_4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
                                dedao_4 = (int(dedao_x_4), int(dedao_y_4))
                                # print(dedao_4)

                                ######################################################################################
                                # Ponto 3 do dedao
                                dedao_x_3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width
                                dedao_y_3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height
                                dedao_3 = (int(dedao_x_3), int(dedao_y_3))
                                dedao_3_ = (int(dedao_x_3) + int(dedao_y_3))
                                # print(dedao_3)

                                ######################################################################################
                                # Ponto 2 do dedao
                                dedao_x_2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width
                                dedao_y_2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height
                                dedao_2 = (int(dedao_x_2), int(dedao_y_2))
                                # print(dedao_2)

                                ######################################################################################
                                # Ponto 1 do dedao
                                dedao_x_1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width
                                dedao_y_1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height
                                dedao_1 = (int(dedao_x_1), int(dedao_y_1))
                                # print(dedao_1)

                                ######################################################################################
                                # Ponto 0 mão
                                mao_x_0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width
                                mao_y_0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height
                                mao_0 = (int(mao_x_0), int(mao_y_0))
                                # print(mao_0)

                                ######################################################################################
                                # Ponto 8 indicador
                                indicador_x_8 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
                                indicador_y_8 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
                                indicador_8 = (int(indicador_x_8), int(indicador_y_8))
                                # print(indicador_8)

                                ######################################################################################
                                # Ponto 7 indicador
                                indicador_x_7 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width
                                indicador_y_7 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height
                                indicador_7 = (int(indicador_x_7), int(indicador_y_7))
                                indicador_7_ = (int(indicador_x_7) + int(indicador_y_7))
                                # print(indicador_7)

                                ######################################################################################
                                # Ponto 6 indicador
                                indicador_x_6 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width
                                indicador_y_6 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height
                                indicador_6 = (int(indicador_x_6), int(indicador_y_6))
                                # print(indicador_6)

                                ######################################################################################
                                # Ponto 5 indicador
                                indicador_x_5 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width
                                indicador_y_5 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height
                                indicador_5 = (int(indicador_x_5), int(indicador_y_5))
                                # print(indicador_5)

                                ######################################################################################
                                # Ponto 12 Medio
                                indicador_x_12 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width
                                indicador_y_12 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height
                                indicador_12 = (int(indicador_x_12), int(indicador_y_12))
                                # print(indicador_12)

                                ######################################################################################
                                # Ponto 11 Medio
                                indicador_x_11 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width
                                indicador_y_11 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height
                                indicador_11 = (int(indicador_x_11), int(indicador_y_11))
                                # print(indicador_11)

                                ######################################################################################
                                # Ponto 10 Medio
                                indicador_x_10 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width
                                indicador_y_10 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height
                                indicador_10 = (int(indicador_x_10), int(indicador_y_10))
                                # print(indicador_10)

                                ######################################################################################
                                # Ponto 9 Medio
                                indicador_x_9 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width
                                indicador_y_9 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height
                                indicador_9 = (int(indicador_x_9), int(indicador_y_9))
                                # print(indicador_9)

                                ######################################################################################
                                # Ponto 16 anelar
                                indicador_x_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width
                                indicador_y_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height
                                indicador_z_16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z
                                # print(indicador_z_16)
                                indicador_16 = (int(indicador_x_16), int(indicador_y_16))
                                # print(indicador_16)

                                ######################################################################################
                                # Ponto 15 anelar
                                indicador_x_15 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width
                                indicador_y_15 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height
                                indicador_15 = (int(indicador_x_15), int(indicador_y_15))
                                # print(indicador_15)

                                ######################################################################################
                                # Ponto 14 anelar
                                indicador_x_14 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width
                                indicador_y_14 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height
                                indicador_14 = (int(indicador_x_14), int(indicador_y_14))
                                # print(indicador_14)

                                ######################################################################################
                                # Ponto 13 anelar
                                indicador_x_13 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width
                                indicador_y_13 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height
                                indicador_13 = (int(indicador_x_13), int(indicador_y_13))
                                # print(indicador_13)

                                ######################################################################################
                                # Ponto 20 Mindinho
                                indicador_x_20 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width
                                indicador_y_20 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height
                                indicador_20 = (int(indicador_x_20), int(indicador_y_20))
                                # print(indicador_20)

                                ######################################################################################
                                # Ponto 19 Mindinho
                                indicador_x_19 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width
                                indicador_y_19 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height
                                indicador_19 = (int(indicador_x_19), int(indicador_y_19))
                                # print(indicador_19)

                                ######################################################################################
                                # Ponto 18 Mindinho
                                indicador_x_18 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width
                                indicador_y_18 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height
                                indicador_18 = (int(indicador_x_18), int(indicador_y_18))
                                # print(indicador_18)

                                ######################################################################################
                                # Ponto 17 Mindinho
                                indicador_x_17 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width
                                indicador_y_17 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height
                                indicador_17 = (int(indicador_x_17), int(indicador_y_17))
                            if letra_Momento == 'a':
                                
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)
                    
                                if f < 20 and g > 0:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador
                                
                                if contador >= 5:
                                    print("Letra A")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 2                                     
                                    time.sleep(2)
                                    contadorPonto = 0
                                                                
                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_6),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'b':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                if(dedao_x_4 > indicador_x_9):

                                    f = (dedao_x_4 - indicador_x_9)
                                if (dedao_x_4 < indicador_x_9):
                                    f = (indicador_x_9 - dedao_x_4)

                                if f < 20:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_16 > indicador_y_12 and indicador_y_20 > indicador_y_12 and indicador_y_8 > indicador_y_12:

                                    if indicador_y_15 > indicador_y_16:
                                        COLOR3 = (0, 255, 0)
                                        contador = 1 + contador

                                    if indicador_y_11 > indicador_y_12:
                                        COLOR4 = (0, 255, 0)
                                        contador = 1 + contador

                                    if indicador_y_19 > indicador_y_20:
                                        COLOR5 = (0, 255, 0)
                                        contador = 1 + contador

                                    if indicador_y_7 > indicador_y_8:
                                        COLOR6 = (0, 255, 0)
                                        contador = 1 + contador

                                if contador >= 5:
                                    print("Letra B")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 3 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                               
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_9),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_9, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'c':

                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_x_8 > indicador_x_12:
                                    d = (indicador_x_8 - indicador_x_12)

                                if indicador_x_8 < indicador_x_12:
                                    d = (indicador_x_12 - indicador_x_8)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_3 - indicador_y_7)

                                if ((g) > (f + (f*0.22))):
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                if d < 10:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if dd < 10:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 10:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador
                               

                                if contador >= 4:
                                    print("Letra c")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 4 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0
                               
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_12),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'd':

                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                if(dedao_x_4 > indicador_x_12):
                                    f = (dedao_x_4 - indicador_x_12)
                                if (dedao_x_4 < indicador_x_12):
                                    f = (indicador_x_12 - dedao_x_4)

                                if f < 14:
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                gg = (indicador_y_6 - indicador_y_10)
                                ff = (indicador_y_8 - indicador_y_18)

                                if(gg < 0 and ff < 0):
                                    gg = gg * -1
                                    ff = ff * -1
                                elif (gg < 0):
                                    gg = gg * -1
                                elif(ff < 0):
                                    ff = ff * -1


                                if(gg > ff):
                                    d = gg / ff
                                else:
                                    d = ff / gg
                                if(d > 3.8 and d < 5.2):
                                    contador = 1 + contador
                                    COLOR = (0, 255, 0)
                                    COLOR6 = (0, 255, 0)

                                if indicador_y_8 < indicador_y_7:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if dd < 14:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 14:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra D")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 5 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0
                                #########################################################################
                                cv2.line(image, (indicador_6), (indicador_10),
                                            COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_10, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (indicador_8), (indicador_18),
                                            COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_18, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_12),
                                            COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_7),
                                            COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                            COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                            COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                            (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)                            
                            elif letra_Momento == 'e':

                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if(dedao_x_3 > indicador_x_8):
                                    g = (dedao_x_3 - indicador_x_8)
                                if (dedao_x_3 < indicador_x_8):
                                    g = (indicador_x_8 - dedao_x_3)

                                if f < 10:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                if g < 10:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 6:
                                    print("Letra E")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 6 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'f':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                
                                f = indicador_y_8 - dedao_y_4
                                if(f < 0):
                                    f = f * -1

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_16 > indicador_y_12 and indicador_y_20 > indicador_y_12:

                                    if indicador_y_15 > indicador_y_16:
                                        COLOR3 = (0, 255, 0)
                                        contador = 1 + contador

                                    if indicador_y_11 > indicador_y_12:
                                        COLOR4 = (0, 255, 0)
                                        contador = 1 + contador
 
                                    if indicador_y_19 > indicador_y_20:
                                        COLOR5 = (0, 255, 0)
                                        contador = 1 + contador

                                if contador >= 4:
                                    print("Letra F")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 7 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################                       
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)                               
                            elif letra_Momento == 'g':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                    if indicador_y_9 < indicador_y_12:
                                        COLOR4 = (0, 255, 0)
                                        contador = 1 + contador

                                    if indicador_y_17 < indicador_y_20:
                                        COLOR5 = (0, 255, 0)
                                        contador = 1 + contador
                                else:
                                    if indicador_y_16 > indicador_y_12:
                                        COLOR4 = (0, 255, 0)
                                        contador = 1 + contador

                                        if indicador_y_20 > indicador_y_16:

                                            COLOR5 = (0, 255, 0)
                                            contador = 1 + contador

                                            COLOR3 = (0, 255, 0)
                                            contador = 1 + contador

                                f = indicador_y_10 - dedao_y_4
                                if(f < 0):
                                    f = f * -1

                                if f < 20:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador

                                if(indicador_y_6 < dedao_y_4):
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra G")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 8 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                cv2.line(image, (indicador_6), (dedao_4),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_10), (dedao_4),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_10, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################

                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'h':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = indicador_y_6 - dedao_y_4
                                g = indicador_y_10 - dedao_y_4

                                if indicador_x_8 > indicador_x_12:
                                    virar = 1
                                if indicador_x_8 < indicador_x_12:
                                    vira = 2
                                if virar == 1:
                                    if indicador_x_12 > indicador_x_8:
                                        COLO6 = (0, 255, 0)
                                        contador = 1 + contador
                                if vira == 2:
                                    if indicador_x_12 < indicador_x_8:
                                        contador = 1 + contador
                                        COLOR6 = (0, 255, 0)
                                if(f < 0):
                                    f = f * -1
                                if(g < 0):
                                    g = g * -1
                                if f < 20:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                if g < 20:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra H")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 9 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                cv2.line(image, (indicador_6), (dedao_4),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_10), (dedao_4),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_10, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################

                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'i':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = (dedao_y_4 - indicador_y_7)
                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_14 > indicador_y_19:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra I")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 10 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                #####################################################################
                                cv2.line(image, (indicador_14), (indicador_19),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_14, 4,
                                        (255, 0, 255), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_19, 4, (255, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_7),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'j':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if indicador_x_8 > indicador_x_20:
                                    virar = 1
                                if indicador_x_8 < indicador_x_20:
                                    vira = 2
                                if virar == 1:
                                    if indicador_x_20 > indicador_x_8:
                                        COLO6 = (0, 255, 0)
                                        contador = 1 + contador
                                if vira == 2:
                                    if indicador_x_20 < indicador_x_8:
                                        contador = 1 + contador
                                        COLOR6 = (0, 255, 0)

                                f = (dedao_y_4 - indicador_y_7)

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_14 > indicador_y_19:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 6:
                                    print("Letra J")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 11
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                #####################################################################
                                cv2.line(image, (indicador_14), (indicador_19),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_14, 4,
                                        (255, 0, 255), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_19, 4, (255, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_7),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_20), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'k':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = indicador_y_6 - dedao_y_4
                                g = indicador_y_10 - dedao_y_4

                                if indicador_x_8 > indicador_x_12:
                                    virar = 1
                                if indicador_x_8 < indicador_x_12:
                                    vira = 2
                                if virar == 1:
                                    if indicador_x_12 > indicador_x_8:
                                        COLO6 = (0, 255, 0)
                                        contador = 1 + contador
                                if vira == 2:
                                    if indicador_x_12 < indicador_x_8:
                                        contador = 1 + contador
                                        COLOR6 = (0, 255, 0)
                                if(f < 0):
                                    f = f * -1
                                if(g < 0):
                                    g = g * -1
                                if f < 20:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                if g < 20:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador
                                    if subir == 0:
                                        subir = dedao_y_4
                                if (subir + 50 < dedao_y_4):
                                    contador = 1 + contador
                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 6:
                                    print("Letra K")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 12 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                cv2.line(image, (indicador_6), (dedao_4),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_10), (dedao_4),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_10, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################

                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'l':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_2 - indicador_y_6)

                                if ((f) > (g + (g*0.22))):
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)
                                s = dedao_y_2 - indicador_y_6

                                if indicador_y_13 < indicador_y_16:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                  
                                if indicador_y_9 < indicador_y_12:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra L")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 13 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                               
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_7),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'm':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = indicador_x_20 - dedao_x_4
                                if(f < 0):
                                    f = f * -1

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra M")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 14 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                cv2.line(image, (dedao_4), (indicador_20),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'n':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = indicador_x_20 - dedao_x_4
                                g = indicador_x_16 - dedao_x_4
                                if(f < 0):
                                    f = f * -1
                                if(g < 0):
                                    g = g * -1

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador
                                if g < 15:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra N")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 15
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                cv2.line(image, (dedao_4), (indicador_20),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'o':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_x_8 > indicador_x_12:
                                    d = (indicador_x_8 - indicador_x_12)

                                if indicador_x_8 < indicador_x_12:
                                    d = (indicador_x_12 - indicador_x_8)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_3 - indicador_y_7)

                                if f < 15:
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                if d < 10:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if dd < 10:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 10:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra O")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 16
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_12),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'p':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                f = indicador_y_6 - dedao_y_4
                                g = indicador_y_10 - dedao_y_4

                                if(g < 0):
                                    g = g * -1

                                if g < 20:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 3:
                                    print("Letra P")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 17
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                ###################################################################
                                cv2.line(image, (indicador_10), (dedao_4),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_10, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'q':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_8):
                                    f = (dedao_x_4 - indicador_x_8)
                                if (dedao_x_4 < indicador_x_8):
                                    f = (indicador_x_8 - dedao_x_4)

                                if f < 45:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra Q")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 18
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'r':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if(indicador_x_8 > indicador_x_12):
                                    g = (indicador_x_8 - indicador_x_12)
                                if (indicador_x_8 < indicador_x_12):
                                    g = (indicador_x_12 - indicador_x_8)

                                if g < 15:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador

                                if(indicador_x_7 > indicador_x_11):
                                    h = (indicador_x_7 - indicador_x_11)
                                if (indicador_x_7 < indicador_x_11):
                                    h = (indicador_x_11 - indicador_x_7)

                                if h < 8:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra R")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 19 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_7), (indicador_11),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_11, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_8),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 's':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if(dedao_x_3 > indicador_x_8):
                                    g = (dedao_x_3 - indicador_x_8)
                                if (dedao_x_3 < indicador_x_8):
                                    g = (indicador_x_8 - dedao_x_3)

                                if f < 10:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                if g < 10:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 6:
                                    print("Letra S")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 20
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 't':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_8):
                                    f = (dedao_x_4 - indicador_x_8)
                                if (dedao_x_4 < indicador_x_8):
                                    f = (indicador_x_8 - dedao_x_4)

                                if f < 10:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_15 > indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_11 > indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_19 > indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra T")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 21 
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'u':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if(indicador_x_7 > indicador_x_11):
                                    h = (indicador_x_7 - indicador_x_11)
                                if (indicador_x_7 < indicador_x_11):
                                    h = (indicador_x_11 - indicador_x_7)

                                if h < 20:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra U")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 22
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_7), (indicador_11),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_11, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'v':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if f < 15:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if(indicador_x_7 > indicador_x_11):
                                    h = (indicador_x_7 - indicador_x_11)
                                if (indicador_x_7 < indicador_x_11):
                                    h = (indicador_x_11 - indicador_x_7)

                                if h > 30:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra V")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 23 
                                    time.sleep(2)
                                    contadorPonto = 0

                                contador = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_7), (indicador_11),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_11, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_7, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'w':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_20):
                                    f = (dedao_x_4 - indicador_x_20)
                                if (dedao_x_4 < indicador_x_20):
                                    f = (indicador_x_20 - dedao_x_4)

                                if f < 10:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador
                                    if subir == 0:
                                        subir = dedao_y_4

                                if (subir > dedao_y_4 + 40):
                                    contador = 1 + contador
                                    con = con + 1

                                if indicador_y_15 > indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_11 > indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_7 > indicador_y_8:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra W")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 24
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                if con == 2:

                                    subir = 0
                                    con = 0
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_20),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'x':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                COLOR7 = (0, 0, 0)
                                if dedao_x_4 > indicador_x_8:
                                    d = (dedao_x_4 - indicador_x_8)

                                if dedao_x_4 < indicador_x_8:
                                    d = (indicador_x_8 - dedao_x_4)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                if dedao_x_4 > indicador_x_8:
                                    if d < 60:
                                        COLOR7 = (0, 255, 0)
                                        contador = 1 + contador
                                if dedao_x_4 < indicador_x_8:
                                    if d > 30:
                                        COLOR7 = (0, 255, 0)
                                        contador = 1 + contador

                                if dd < 16:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if ddd < 16:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if f < 25:
                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                    if ladinho == 0:
                                        ladinho = dedao_x_4

                                if dedao_x_4 > indicador_x_8:
                                    if (ladinho + 60 < dedao_x_4):
                                        contador = 1 + contador

                                if dedao_x_4 < indicador_x_8:
                                    if (ladinho > dedao_x_4 + 60):
                                        contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 8:
                                    print("Letra X")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 25
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                if con == 2:
                                    ladinho = 0
                                    con = 0

                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR7, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)               
                            elif letra_Momento == 'y':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                COLOR7 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_20):

                                    f = (dedao_x_4 - indicador_x_20)
                                if (dedao_x_4 < indicador_x_20):
                                    f = (indicador_x_20 - dedao_x_4)

                                if f > 60:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador
                                    if subir == 0:
                                        subir = dedao_y_4
                                if (subir > dedao_y_4 + 40):
                                    contador = 1 + contador
                                    con = con + 1
                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 5:
                                    print("Letra Y")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 26
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                if con == 2:
                                    subir = 0
                                    con = 0
                                ###################################################################
                                cv2.line(image, (dedao_4), (indicador_20),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)                            
                            elif letra_Momento == 'z':
                                COLOR = (0, 0, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)

                                if(dedao_x_4 > indicador_x_16):
                                    f = (dedao_x_4 - indicador_x_16)
                                if (dedao_x_4 < indicador_x_16):
                                    f = (indicador_x_16 - dedao_x_4)

                                if f < 15:

                                    COLOR = (0, 255, 0)
                                    contador = 1 + contador
                                    if contar == 0:
                                        contar = 1
                                    if ladinho == 0:
                                        ladinho = indicador_x_8
                                    if (ladinho > indicador_x_8 + 40):

                                        if contar == 1:
                                            y = indicador_y_8
                                            x = indicador_x_8
                                        contar = 2

                                if contar == 2:
                                    if (x + 40 < indicador_x_8 and indicador_y_8 > y + 30):
                                        contar = 3
                                        xx = indicador_x_8
                                if contar == 3:

                                    if (xx > indicador_x_8 + 15):
                                        contar = 4

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if contar == 4:
                                    contador = 1 + contador
                                if contador >= 5:
                                    print("Letra Z")
                                    print("vc Acertou")
                                    letra = 'next'
                                    trocaLetra = 1
                                    menu_opc2_soletra  = 27
                                    time.sleep(2)
                                    contadorPonto = 0
                                contador = 0
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_16),
                                        COLOR, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                #########################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)                               
                            elif letra_Momento == 'proximo':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)
                    
                                if f < 20 and g > 0:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador
                                
                                if contador >= 5:
                                    print("Proximo")
                                    print("vc Acertou")
                                    letra_Momento = 'nenhuma'
                                    if dentro_menu_opc2 == 1:
                                        print("dentro if")
                                        if menu_opc2 == 5:
                                            menu_opc2 = 2
                                            troca_opc = 1
                                            QApplication.processEvents()
                                            time.sleep(1)
                                        else:
                                            menu_opc2 = menu_opc2 + 1
                                            QApplication.processEvents()
                                            time.sleep(1)
                                            troca_opc = 1
                                    else: 
                                        menu_opc2 = 1                               
                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_6),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'proximo2':

                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)
                    
                                if f < 20 and g > 0:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador
                                print(visualizarLetra)
                                if contador >= 5:
                                    print("Letra proximo2")
                                    print("vc Acertou")
                                    letra_Momento = 'nenhuma'                                    
                                    if (visualizarLetra == 27):
                                        visualizarLetra = 1
                                    visualizarLetra = visualizarLetra + 1
                                    QApplication.processEvents()
                                    time.sleep(0.5)
                             
                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_6),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)   
                            elif letra_Momento == 'proximo3':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_x_8 > indicador_x_12:
                                    d = (indicador_x_8 - indicador_x_12)

                                if indicador_x_8 < indicador_x_12:
                                    d = (indicador_x_12 - indicador_x_8)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_3 - indicador_y_7)

                                if ((g) > (f + (f*0.22))):
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                if d < 10:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if dd < 10:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 10:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador
                                if contador >= 4:
                                    print("Proximo3")
                                    print("vc Acertou")
                                    #letra_Momento = 'nenhuma'

                                    if menu_opc3 == 0:
                                        menu_opc3 = 1
                                        QApplication.processEvents()
                                        time.sleep(1)
                                    else:
                                        menu_opc3 = menu_opc3 + 1
                                        QApplication.processEvents()
                                        time.sleep(1)
                                        if menu_opc3 == 4:
                                            menu_opc3 = 1
                                    letra = 'selecionar2'
                                    #print(letra)
                                                               
                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_12),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)
                            elif letra_Momento == 'voltar':
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                                
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)
                    
                                if f < 20 and g > 0:
                                    COLOR2 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_13 < indicador_y_16:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador
                                if contador >= 5:
                                    print("Letra voltar")
                                    print("vc Acertou")
                                    voltarMenu = 'sair'
                                    print(voltarMenu)
                                    letra = 'proximo'
                                    menu_opc2 = 1
                                    entrar_opc = 0
                                    QApplication.processEvents()                                                     
                                contador = 0
                                
                                #########################################################################
                                cv2.line(image, (dedao_3), (indicador_6),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_6, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_3, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_16),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_12),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_20),
                                        COLOR6, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (mao_0), (indicador_8),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, mao_0, 4, (0, 0, 0), 2, cv2.LINE_AA)  
                            elif letra_Momento == 'selecionar2':

                                
                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_x_8 > indicador_x_12:
                                    d = (indicador_x_8 - indicador_x_12)

                                if indicador_x_8 < indicador_x_12:
                                    d = (indicador_x_12 - indicador_x_8)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_3 - indicador_y_7)

                                if ((g) > (f + (f*0.22))):
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                if d < 10:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if dd < 10:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 10:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador
                               
                                print("entrou selecionar")
                                if contador >= 4:
                                    print("Letra B")
                                    print("vc Acertou")
                                    letra = 'a'
                                    confirmacaoMenuOpcNivel = 1
                                else:
                                    letra = 'proximo3'    
                                
                                contador = 0
                               
                               #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_12),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                
                                
                            elif letra_Momento == 'selecionar':

                                COLOR = (0, 255, 0)
                                COLOR2 = (0, 0, 0)
                                COLOR3 = (0, 0, 0)
                                COLOR4 = (0, 0, 0)
                                COLOR5 = (0, 0, 0)
                                COLOR6 = (0, 0, 0)
                               
                                f = (dedao_x_3 - indicador_x_6)
                                g = (indicador_y_6 - dedao_y_4)

                                if indicador_x_8 > indicador_x_12:
                                    d = (indicador_x_8 - indicador_x_12)

                                if indicador_x_8 < indicador_x_12:
                                    d = (indicador_x_12 - indicador_x_8)

                                if indicador_x_12 > indicador_x_16:
                                    dd = (indicador_x_12 - indicador_x_16)

                                if indicador_x_12 < indicador_x_16:
                                    dd = (indicador_x_16 - indicador_x_12)

                                if indicador_x_16 > indicador_x_20:
                                    ddd = (indicador_x_16 - indicador_x_20)

                                if indicador_x_16 < indicador_x_20:
                                    ddd = (indicador_x_20 - indicador_x_16)

                                f = (dedao_y_4 - indicador_y_8)
                                g = (dedao_y_3 - indicador_y_7)

                                if ((g) > (f + (f*0.22))):
                                    contador = 1 + contador
                                    COLOR2 = (0, 255, 0)

                                if d < 10:
                                    COLOR3 = (0, 255, 0)
                                    contador = 1 + contador
                                if dd < 10:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                if ddd < 10:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador
                               

                                if contador >= 4:
                                    print("Letra B")
                                    print("vc Acertou")
                                    letra_Momento = 'nenhuma'
                                    entrar_opc = 1
                                   
                                
                                contador = 0
                               
                                #########################################################################
                                cv2.line(image, (dedao_4), (indicador_8),
                                        COLOR2, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, dedao_4, 4, (0, 0, 0), 2, cv2.LINE_AA)

                                ###################################################################
                                cv2.line(image, (indicador_8), (indicador_12),
                                        COLOR3, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_8, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_12), (indicador_16),
                                        COLOR4, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_12, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                ###################################################################
                                cv2.line(image, (indicador_16), (indicador_20),
                                        COLOR5, 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_20, 4,
                                        (0, 0, 0), 2, cv2.LINE_AA)
                                cv2.circle(image, indicador_16, 4, (0, 0, 0), 2, cv2.LINE_AA)
                                
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
    threading.Thread(target = contadorPontuacao).start()
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
# Abrindo A janaela do Windos
window()
########################################################