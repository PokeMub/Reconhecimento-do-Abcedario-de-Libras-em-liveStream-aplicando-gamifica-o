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
# https://www.youtube.com/watch?v=2RVVC9rrDco&ab_channel=Andr%C3%A9LuizFran%C3%A7aBatista
#teste
nomeJogador = 0
visualizarLetra = 1
letra = 'vazio'
menu_opc1 = 0
menu_opc2 = 0
entrar_opc = 0
troca_opc = 0
dentro_menu_opc2 = 0
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

        # self.te = te()
        # self.te.start()
        self.setLayout(self.VBL)
        self.initUI()
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    ################################################################################

    def initUI(self):
        # self.showMaximized()

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

        # Titulo da janela
        self.setWindowTitle("Tela Inicial")
        ####################################################

        # Label com o Nome do Jogo
        ## detectar fontes do pc https://flippingtypical.com/  

        ## Imagem Tela Menu
        self.imgMenu = QLabel(self)
        self.enderecoImMenu = QPixmap('imagens/menuImagem.jpg')
        self.imgMenu.setPixmap(self.enderecoImMenu)
        self.imgMenu.setGeometry(0, 0,0, 0)

        
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
        ## Segunda tela

        ## Label Principal Explicando pra que serve os sinais
        self.labelPricipalMovimentaoBotes = QLabel("Sinais para Movimentação dos Botões", self)
        self.labelPricipalMovimentaoBotes.setFont(QFont('Arial Black', 30))
        self.labelPricipalMovimentaoBotes.adjustSize()
        self.labelPricipalMovimentaoBotes.move(-500, -500)


        ### Adicionando uma imagem
        ## Label da Imagem Proximo
        self.labelImagProximo = QLabel("Proximo", self)
        self.labelImagProximo.setFont(QFont('Arial Black', 20))
        self.labelImagProximo.adjustSize()
        self.labelImagProximo.move(-500, -500)
		## Imagem Proximo
        self.imgProximo = QLabel(self)
        self.enderecoImgProx = QPixmap('imagens/proximo.jpg')
        self.imgProximo.setPixmap(self.enderecoImgProx)
        self.imgProximo.setGeometry(0, 0,0, 0)


        ## Label da Imagem Selecionar
        self.labelImagSelecionar = QLabel("Selecionar", self)
        self.labelImagSelecionar.setFont(QFont('Arial Black', 20))
        self.labelImagSelecionar.adjustSize()
        self.labelImagSelecionar.move(-500, -500)
        ## Imagem Selecionar

        self.imgSelecionar = QLabel(self)
        self.enderecoImgSel = QPixmap('imagens/selecionar.jpg')
        self.imgSelecionar.setPixmap(self.enderecoImgSel)
        self.imgSelecionar.setGeometry(0, 0,0, 0)


        ## Label da Imagem Voltar
        self.labelImagVoltar = QLabel("Voltar", self)
        self.labelImagVoltar.setFont(QFont('Arial Black', 20))
        self.labelImagVoltar.adjustSize()
        self.labelImagVoltar.move(-500, -500)
		## Imagem Voltar
        self.imgVoltar = QLabel(self)
        self.enderecoImVolt = QPixmap('imagens/voltar.jpg')
        self.imgVoltar.setPixmap(self.enderecoImVolt)
        self.imgVoltar.setGeometry(0, 0,0, 0)
        
        

        self.op1MenuVisualizarAlfabeto = QPushButton(self)
        self.op1MenuVisualizarAlfabeto.setText("Visualizar Alfabeto")
        self.op1MenuVisualizarAlfabeto.setFont(QFont('Arial Black', 20))
        self.op1MenuVisualizarAlfabeto.setStyleSheet("border :6px solid black;") 
        self.op1MenuVisualizarAlfabeto.resize(150, 40) 
        self.op1MenuVisualizarAlfabeto.adjustSize()
        self.op1MenuVisualizarAlfabeto.setGeometry(1000, 1000, int(self.x/1.5), 100) 
        self.op1MenuVisualizarAlfabeto.move(-500, -500)

        self.op1MenuPraticarAlfabeto = QPushButton(self)
        self.op1MenuPraticarAlfabeto.setText("Praticar Alfabeto")
        self.op1MenuPraticarAlfabeto.setFont(QFont('Arial Black', 20))
        self.op1MenuPraticarAlfabeto.setStyleSheet("border :6px solid black;") 
        self.op1MenuPraticarAlfabeto.resize(150, 40) 
        self.op1MenuPraticarAlfabeto.adjustSize()
        self.op1MenuPraticarAlfabeto.setGeometry(1000, 1000, int(self.x/1.5), 100) 
        self.op1MenuPraticarAlfabeto.move(-500, -500)
        
        self.op1MenuJogar = QPushButton(self)
        self.op1MenuJogar.setText("Jogar")
        self.op1MenuJogar.setFont(QFont('Arial Black', 20))
        self.op1MenuJogar.setStyleSheet("border :6px solid black;") 
        self.op1MenuJogar.resize(150, 40) 
        self.op1MenuJogar.adjustSize()
        self.op1MenuJogar.setGeometry(1000, 1000, int(self.x/1.5), 100) 
        self.op1MenuJogar.move(-500, -500)

        self.op1MenuRecompensas = QPushButton(self)
        self.op1MenuRecompensas.setText("Ranks")
        self.op1MenuRecompensas.setFont(QFont('Arial Black', 20))
        self.op1MenuRecompensas.setStyleSheet("border :6px solid black;") 
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
        ###################################################################################################################################    
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
        # trsG = QTransform().rotate(90)
        # self.imgG.setPixmap(QPixmap(self.imageG).transformed(trsG))
        
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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra H2
        self.imageH2 = QImage('letras/H2.jpg') 
        self.imgH2 = QLabel(self)
        self.enderecoH2 = QPixmap('letras/H2.jpg')
        self.imgH2.setPixmap(self.enderecoH2)  
        self.imgH2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra H3
        self.imageH3 = QImage('letras/H3.jpg') 
        self.imgH3 = QLabel(self)
        self.enderecoH3 = QPixmap('letras/H3.jpg')
        self.imgH3.setPixmap(self.enderecoH3)  
        self.imgH3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra J2
        self.imageJ2 = QImage('letras/J2.jpg') 
        self.imgJ2 = QLabel(self)
        self.enderecoJ2 = QPixmap('letras/J2.jpg')
        self.imgJ2.setPixmap(self.enderecoJ2)  
        self.imgJ2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra J3
        self.imageJ3 = QImage('letras/J3.jpg') 
        self.imgJ3 = QLabel(self)
        self.enderecoJ3 = QPixmap('letras/J3.jpg')
        self.imgJ3.setPixmap(self.enderecoJ3)  
        self.imgJ3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra X2
        self.imageX2 = QImage('letras/X2.jpg') 
        self.imgX2 = QLabel(self)
        self.enderecoX2 = QPixmap('letras/X2.jpg')
        self.imgX2.setPixmap(self.enderecoX2)  
        self.imgX2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra X3
        self.imageX3 = QImage('letras/X3.jpg') 
        self.imgX3 = QLabel(self)
        self.enderecoX3 = QPixmap('letras/X3.jpg')
        self.imgX3.setPixmap(self.enderecoX3)  
        self.imgX3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra Y2
        self.imageY2 = QImage('letras/Y2.jpg') 
        self.imgY2 = QLabel(self)
        self.enderecoY2 = QPixmap('letras/Y2.jpg')
        self.imgY2.setPixmap(self.enderecoY2)  
        self.imgY2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra Y3
        self.imageY3 = QImage('letras/Y3.jpg') 
        self.imgY3 = QLabel(self)
        self.enderecoY3 = QPixmap('letras/Y3.jpg')
        self.imgY3.setPixmap(self.enderecoY3)  
        self.imgY3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra W2
        self.imageW2 = QImage('letras/W2.jpg') 
        self.imgW2 = QLabel(self)
        self.enderecoW2 = QPixmap('letras/W2.jpg')
        self.imgW2.setPixmap(self.enderecoW2)  
        self.imgW2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra W3
        self.imageW3 = QImage('letras/W3.jpg') 
        self.imgW3 = QLabel(self)
        self.enderecoW3 = QPixmap('letras/W3.jpg')
        self.imgW3.setPixmap(self.enderecoW3)  
        self.imgW3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))

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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra I2
        self.imageI2 = QImage('letras/I2.jpg') 
        self.imgI2 = QLabel(self)
        self.enderecoI2 = QPixmap('letras/I2.jpg')
        self.imgI2.setPixmap(self.enderecoI2)  
        self.imgI2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra I3
        self.imageI3 = QImage('letras/I3.jpg') 
        self.imgI3 = QLabel(self)
        self.enderecoI3 = QPixmap('letras/I3.jpg')
        self.imgI3.setPixmap(self.enderecoI3)  
        self.imgI3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
        
        ## Imagem Letra I4
        self.imageI4 = QImage('letras/I4.jpg') 
        self.imgI4 = QLabel(self)
        self.enderecoI4 = QPixmap('letras/I4.jpg')
        self.imgI4.setPixmap(self.enderecoI4)  
        self.imgI4.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))


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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra Z2
        self.imageZ2 = QImage('letras/Z2.jpg') 
        self.imgZ2 = QLabel(self)
        self.enderecoZ2 = QPixmap('letras/Z2.jpg')
        self.imgZ2.setPixmap(self.enderecoZ2)  
        self.imgZ2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra Z3
        self.imageZ3 = QImage('letras/Z3.jpg') 
        self.imgZ3 = QLabel(self)
        self.enderecoZ3 = QPixmap('letras/Z3.jpg')
        self.imgZ3.setPixmap(self.enderecoZ3)  
        self.imgZ3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
        
        ## Imagem Letra Z4
        self.imageZ4 = QImage('letras/Z4.jpg') 
        self.imgZ4 = QLabel(self)
        self.enderecoZ4 = QPixmap('letras/Z4.jpg')
        self.imgZ4.setPixmap(self.enderecoZ4)  
        self.imgZ4.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))


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
        # trsH1 = QTransform().rotate(90)
        # self.imgH1.setPixmap(QPixmap(self.imageH1).transformed(trsH1))
        
        ## Imagem Letra K2
        self.imageK2 = QImage('letras/K2.jpg') 
        self.imgK2 = QLabel(self)
        self.enderecoK2 = QPixmap('letras/K2.jpg')
        self.imgK2.setPixmap(self.enderecoK2)  
        self.imgK2.setGeometry(0, 0,0, 0)
        # trsH2 = QTransform().rotate(90)
        # self.imgH2.setPixmap(QPixmap(self.imageH2).transformed(trsH2))

        ## Imagem Letra K3
        self.imageK3 = QImage('letras/K3.jpg') 
        self.imgK3 = QLabel(self)
        self.enderecoK3 = QPixmap('letras/K3.jpg')
        self.imgK3.setPixmap(self.enderecoK3)  
        self.imgK3.setGeometry(0, 0,0, 0)
        # trsH3 = QTransform().rotate(90)
        # self.imgH3.setPixmap(QPixmap(self.imageH3).transformed(trsH3))
        
        ## Imagem Letra K4
        # self.imageK4 = QImage('letras/K4.jpg') 
        # self.imgK4 = QLabel(self)
        # self.enderecoK4 = QPixmap('letras/K4.jpg')
        # self.imgK4.setPixmap(self.enderecoK4)  
        # self.imgK4.setGeometry(0, 0,0, 0)


         ## Imagem Letra K5
        # self.imageK5 = QImage('letras/K5.jpg') 
        # self.imgK5 = QLabel(self)
        # self.enderecoK5 = QPixmap('letras/K5.jpg')
        # self.imgK5.setPixmap(self.enderecoK5)  
        # self.imgK5.setGeometry(0, 0,0, 0)



        ## Label Letra K
        
        self.labelLetK = QLabel("Letra K", self)
        self.labelLetK.setFont(QFont('Arial Black', 20))
        self.labelLetK.adjustSize()
        self.labelLetK.move(-500, -500)
        ############################################################################################################################
    #Metodo para ação do botão
    def btLogar_presionado(self):
        global letra , dentro_menu_opc2, entrar_opc, menu_opc2, troca_opc, visualizarLetra
        nomeJogador = self.nomeJogador.text()
        print(nomeJogador)
        trav = 0
        while True:
            # QApplication.processEvents()
            if menu_opc1 == 0 :
                if menu_opc1 == 0 and menu_opc2 == 0:
                    QApplication.processEvents()
                    
                    self.nomeJogador.hide()
                    self.btLogar.hide()

                    ## Label Principal Explicando pra que serve os sinais
                    self.labelPricipalMovimentaoBotes.adjustSize()
                    self.labelPricipalMovimentaoBotes.move(int(self.x/2.3), int(self.y/2.6))


                    ### Adicionando uma imagem
                    ## Label da Imagem Proximo
                    self.labelImagProximo.adjustSize()
                    self.labelImagProximo.move(int(self.x/3 + 150), int(self.y/1.9))
                    ## Imagem Proximo
                    self.imgProximo.setGeometry(int(self.x/3), int(self.y/1.7),400,300)


                    ## Label da Imagem Selecionar
                    self.labelImagSelecionar.adjustSize()
                    self.labelImagSelecionar.move(int(self.x/1.8 + 130), int(self.y/1.9))
                    ## Imagem Selecionar
                    self.imgSelecionar.setGeometry(int(self.x/1.8), int(self.y/1.7),400,300)


                    ## Label da Imagem Voltar
                    self.labelImagVoltar.adjustSize()
                    self.labelImagVoltar.move(int(self.x/1.284 + 135), int(self.y/1.9))
                    ## Imagem Voltar
                    self.imgVoltar.setGeometry(int(self.x/1.284), int(self.y/1.7),400,300)
                    # print ("oi")
                    ##############################################################
                if(troca_opc == 0):
                    letra = 'proximo'
                if troca_opc == 1:
                    letra = 'selecionar'
                if troca_opc == 2:
                    pass
                if menu_opc2 == 1:
                    QApplication.processEvents()
                    self.labelImagVoltar.adjustSize()
                    self.labelImagVoltar.move(-500, -500)
                    self.imgVoltar.setGeometry(int(-500), int(self.y/1.7),400,300)

                    self.labelImagSelecionar.adjustSize()
                    self.labelImagSelecionar.move(-500, -500)
                    self.imgSelecionar.setGeometry(int(-500), int(self.y/1.7),400,300)

                    self.labelImagProximo.adjustSize()
                    self.labelImagProximo.move(-500, -500)
                    self.imgProximo.setGeometry(int(-500), int(self.y/1.7),400,300)

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
                    self.imgMenu.move(int(self.x /3.3), int(-100))
                    
                    # self.imgSeta.adjustSize()
                    # 

                    dentro_menu_opc2 = 1
                    


####################################################################
                if menu_opc2 == 2 and entrar_opc == 1:
                    QApplication.processEvents()
                    letra = 'proximo2'
                    troca_opc = 2
                    # print("entrei opc 2") 
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
                        
                        ## Remover tela antiga antigos
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

                    elif visualizarLetra == 3:
                         ## Remover tela antiga antigos
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
                    #####################################################################

                    elif visualizarLetra == 12:
                        self.movieK.stop()
                        self.labelK.setGeometry(QtCore.QRect(int(self.x/1.2), int(-1000), 600, 600))

                        self.labelExcLetK.adjustSize()
                        self.labelExcLetK.move(int(self.x/1.15), int(-1000))

                        # self.imgK1.adjustSize()
                        # self.imgK1.move(int(self.x/2), int(-1000))

                        # self.imgK2.adjustSize()
                        # self.imgK2.move(int(self.x/2), int(-1000))

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
                        # print(visualizarLetra) 
                    #####################################################################
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
                        # print(visualizarLetra) 
                        # dentro_menu_opc2 = 1

                if menu_opc2 == 2 and entrar_opc != 1:   
                    QApplication.processEvents()
                    # print("teste2")
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/4))



                if menu_opc2 == 3 and entrar_opc != 1:   
                    QApplication.processEvents()
                    # print("teste3")
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/2.8))
                    
                if menu_opc2 == 3 and entrar_opc == 1:
                    QApplication.processEvents()
                    letra = 'proximo2'
                    troca_opc = 2
                    print("entrei opc 3") 
                    self.imgSeta.move(int(-100), int(-100))



                if menu_opc2 == 4 and entrar_opc != 1:   
                    QApplication.processEvents()
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/2.15))
                    # print("teste4")
                if menu_opc2 == 4 and entrar_opc == 1:
                    QApplication.processEvents()
                    letra = 'proximo2'
                    troca_opc = 2
                    print("entrei opc 4") 
                    self.imgSeta.move(int(-100), int(-100))




                if menu_opc2 == 5 and entrar_opc != 1:   
                    QApplication.processEvents()
                    self.imgSeta.adjustSize()
                    self.imgSeta.move(int(self.x/3), int(self.y/1.74))
                    # print("teste4")
                if menu_opc2 == 5 and entrar_opc == 1:
                    QApplication.processEvents()
                    letra = 'proximo2'
                    troca_opc = 2
                    print("entrei opc 5") 
                    self.imgSeta.move(int(-100), int(-100))
                
            if menu_opc1 == 5:

                QApplication.processEvents()
                self.labelPricipalMovimentaoBotes.adjustSize()
                self.labelPricipalMovimentaoBotes.move(int(self.x), int(self.y/2.6))

  

    def segundaTela(self):
        ## Label Principal Explicando pra que serve os sinais
        self.labelPricipalMovimentaoBotes = QLabel("Sinais para Movimentação dos Botões", self)
        self.labelPricipalMovimentaoBotes.setFont(QFont('Arial Black', 30))
        self.labelPricipalMovimentaoBotes.adjustSize()
        self.labelPricipalMovimentaoBotes.move(int(self.x/2.3), int(self.y/2.6))


        ### Adicionando uma imagem
        ## Label da Imagem Proximo
        self.labelImagProximo = QLabel("Proximo", self)
        self.labelImagProximo.setFont(QFont('Arial Black', 20))
        self.labelImagProximo.adjustSize()
        self.labelImagProximo.move(int(self.x/3 + 150), int(self.y/1.9))
		## Imagem Proximo
        self.imgProximo = QLabel(self)
        self.enderecoImgProx = QPixmap('imagens/proximo.jpg')
        self.imgProximo.setPixmap(self.enderecoImgProx)
        self.imgProximo.setGeometry(int(self.x/3), int(self.y/1.7),400,300)


        ## Label da Imagem Selecionar
        self.labelImagSelecionar = QLabel("Selecionar", self)
        self.labelImagSelecionar.setFont(QFont('Arial Black', 20))
        self.labelImagSelecionar.adjustSize()
        self.labelImagSelecionar.move(int(self.x/1.8 + 130), int(self.y/1.9))
        ## Imagem Selecionar

        self.imgSelecionar = QLabel(self)
        self.enderecoImgSel = QPixmap('imagens/selecionar.jpg')
        self.imgSelecionar.setPixmap(self.enderecoImgSel)
        self.imgSelecionar.setGeometry(int(self.x/1.8), int(self.y/1.7),400,300)


        ## Label da Imagem Voltar
        self.labelImagVoltar = QLabel("Voltar", self)
        self.labelImagVoltar.setFont(QFont('Arial Black', 20))
        self.labelImagVoltar.adjustSize()
        self.labelImagVoltar.move(int(self.x/1.284 + 135), int(self.y/1.9))
		## Imagem Voltar
        self.imgVoltar = QLabel(self)
        self.enderecoImVolt = QPixmap('imagens/voltar.jpg')
        self.imgVoltar.setPixmap(self.enderecoImVolt)
        self.imgVoltar.setGeometry(int(self.x/1.284), int(self.y/1.7),400,300)
        ##############################################################
# print(letra)

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        contador = 0
        contador_troca_opc = 0
        global menu_opc1 , menu_opc2 , dentro_menu_opc2, entrar_opc , troca_opc, visualizarLetra
        letra_Momento = 'Iniciando'
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands
        self.ThreadActive = True
        cap = cv2.VideoCapture(0)
        while self.ThreadActive:
            with mp_hands.Hands(
                    max_num_hands=1,
                    # model_complexity=0,
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
                            

                            # global menu_opc1
                            # menu_opc1 = 3
                            # print(letra)
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
                            # print(indicador_17)

                            distancia_8_4 = int(np.sqrt((indicador_x_8 - dedao_x_4)
                                                        ** 2+(indicador_y_8 - dedao_y_4)**2))

                            distancia_7_3 = int(np.sqrt((indicador_x_7 - dedao_x_3)
                                                        ** 2+(indicador_y_7 - dedao_y_3)**2))

                            distancia_6_2 = int(np.sqrt((indicador_x_6 - dedao_x_2)
                                                        ** 2+(indicador_y_6 - dedao_y_2)**2))

                            distancia_5_1 = int(np.sqrt((indicador_x_5 - dedao_x_1)
                                                        ** 2+(indicador_y_5 - dedao_y_1)**2))

                            distancia_12_0 = int(np.sqrt((indicador_x_12 - mao_x_0)
                                                        ** 2+(indicador_y_12 - mao_y_0)**2))

                            distancia_16_0 = int(np.sqrt((indicador_x_16 - mao_x_0)
                                                        ** 2+(indicador_y_16 - mao_y_0)**2))

                            distancia_20_0 = int(np.sqrt((indicador_x_20 - mao_x_0)
                                                        ** 2+(indicador_y_20 - mao_y_0)**2))

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
                                    letra_Momento = 'nenhuma'
                                    # global menu_opc1
                                    menu_opc1 = 1
                                                                   
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
                                    letra_Momento = 'nenhuma'
                                    letra_Momento = 'nenhuma'
                                    menu_opc1 = 2

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

                                    letra_Momento = 'nenhuma'
                                    menu_opc1 = 3
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
                                ###################################################################

  
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
                                    menu_opc1 = 4
                                    letra_Momento = 'nenhuma'

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
                                ###################################################################
                                
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
                                    # print("opa")
                                    # print("t")
                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador
                                    # print("opa")
                                    # print("t")
                                if indicador_y_17 < indicador_y_20:
                                    COLOR5 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 6:
                                    print("Letra E")
                                    print("vc Acertou")
                                    menu_opc1 = 5
                                    letra_Momento = 'nenhuma'
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
                                # print(f)

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
                                    menu_opc1 = 6
                                    letra_Momento = 'nenhuma'

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
                                    menu_opc1 = 7
                                    letra_Momento = 'nenhuma'

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
                                    menu_opc1 = 8
                                    letra_Momento = 'nenhuma'

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
                                # g = (indicador_y_6 - dedao_y_4)

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
                                    menu_opc1 = 9
                                    letra_Momento = 'nenhuma'

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
                                # g = (indicador_y_6 - dedao_y_4)

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
                                    menu_opc1 = 10
                                    letra_Momento = 'nenhuma'

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
                                    menu_opc1 = 11
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 12
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 13
                                    letra_Momento = 'nenhuma'
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

                                # if indicador_y_13 < indicador_y_16:
                                #     COLOR3 = (0, 255, 0)
                                #     contador = 1 + contador

                                if indicador_y_9 < indicador_y_12:
                                    COLOR4 = (0, 255, 0)
                                    contador = 1 + contador

                                if indicador_y_5 < indicador_y_8:
                                    COLOR6 = (0, 255, 0)
                                    contador = 1 + contador

                                if contador >= 4:
                                    print("Letra N")
                                    print("vc Acertou")
                                    menu_opc1 = 14
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 15
                                    letra_Momento = 'nenhuma'

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
                                ###################################################################

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
                                    menu_opc1 = 16
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 17
                                    letra_Momento = 'nenhuma'
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
                                ###################################################################

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
                                    menu_opc1 = 18
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 19
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 20
                                    letra_Momento = 'nenhuma'
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
                                    menu_opc1 = 21
                                    letra_Momento = 'nenhuma'

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
                                    menu_opc1 = 22
                                    letra_Momento = 'nenhuma'

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
                                    menu_opc1 = 23
                                    letra_Momento = 'nenhuma'
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
                                ###################################################################

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
                                    menu_opc1 = 24
                                    letra_Momento = 'nenhuma'
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
                                ###################################################################

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
                                    menu_opc1 = 25
                                    letra_Momento = 'nenhuma'
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
                                ###################################################################

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
                                    menu_opc1 = 26
                                    letra_Momento = 'nenhuma'
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
                                    print("Letra A")
                                    print("vc Acertou")
                                    letra_Momento = 'nenhuma'
                                    # global menu_opc1

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
                            elif letra_Momento == 'selecionar':
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
                                    letra_Momento = 'nenhuma'
                                    entrar_opc = 1
                                   
                                
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
                                
                                QApplication.processEvents()
                                time.sleep(0.5)
                                troca_opc = 0
                            mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style())
                    # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
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
########################################################


# Abrindo A janaela do Windos
window()
########################################################