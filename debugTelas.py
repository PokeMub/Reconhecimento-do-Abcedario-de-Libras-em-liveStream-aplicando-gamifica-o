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

            ## Instanciando as telas
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
        
        ## Inicialização labels Modalidade Facil
        if True:
            ## Facil - Inicio    
            self.nivelFacilPalavra1 = QLabel(palavraNivelFacilInicio[0], self)
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
            self.nivelMedioPalavra10.move(-1000,-1000)
            #self.nivelMedioPalavra10.move(int(self.x/2), int(self.y/7))

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
            #self.nivelDificilPalavra15.move(-1000,-1000)
            #self.nivelDificilPalavra15.move(int(self.x/2), int(self.y/7))























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