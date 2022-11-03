import os
import pandas as pd
import sys
import numpy as np
import random



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
## Definindo a tela do estagio
###########################################################################################
for variavel3 in range(0, 2):
  if variavel3 == 0:
    estagio = 'Meio'
  else:
    estagio = 'Fim'
  for variavel1 in range(0, tamanho):
    if arquivo.iloc[variavel1]['Estacao'] == estagio:
      ##print(arquivo.iloc[variavel1]['imagem'])
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

#print(meio)
#print(fim)
        
############################################################################################
##Sorteio das Telas
faseMeio = random.randint(0, (len(meio) - 1))
faseFim = random.randint(0, (len(fim) - 1))

faseMeio = meio[faseMeio]
faseFim = fim[faseFim]
faseInicio = 'chegada_castelo'
faseChefao = 'luta_contra_dragao'
#print(faseInicio)
#print(faseMeio)
#print(faseFim)
#print(faseChefao)
###########################################################################################


###########################################################################################
## Colocando as Palavras no Vetor
for variavel1 in range(0, tamanho):
  if arquivo.iloc[variavel1]['imagem'] == faseInicio:
    vetInicio.append(arquivo.iloc[variavel1]['Nome'])
  if arquivo.iloc[variavel1]['imagem'] == faseMeio:
    vetMeio.append(arquivo.iloc[variavel1]['Nome'])
  if arquivo.iloc[variavel1]['imagem'] == faseFim:
    vetFim.append(arquivo.iloc[variavel1]['Nome'])
  if arquivo.iloc[variavel1]['imagem'] == faseChefao:
    vetChefao.append(arquivo.iloc[variavel1]['Nome'])

#print(vetInicio)
#print(vetMeio)
#print(vetFim)
#print(vetChefao)
##########################################################################################


#########################################################################################
##Sorteando as Plavras
palavraNivelFacilInicio = []
palavraNivelFacilMeio = []
palavraNivelFacilFim = []
sortTemporario = ''
for faseFacil in range(0,5):
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
          palavraNivelFacilMeio.append(random.choice(vetMeio)) 
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
          palavraNivelFacilFim.append(random.choice(vetFim)) 
          nRepetir = 0
    nRepetir = 1  
print('Inicio - Facil: ')
print(palavraNivelFacilInicio )
print('################# ')

print('Meio - Facil: ')
print(palavraNivelFacilMeio )
print('################# ')

print('Fim - Facil: ' )
print(palavraNivelFacilFim )
print('################# ')