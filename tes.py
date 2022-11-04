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
# Definindo a tela do estagio
###########################################################################################
for variavel3 in range(0, 2):
    if variavel3 == 0:
        estagio = 'Meio'
    else:
        estagio = 'Fim'
    for variavel1 in range(0, tamanho):
        if arquivo.iloc[variavel1]['Estacao'] == estagio:
            # print(arquivo.iloc[variavel1]['imagem'])
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

# print(meio)
# print(fim)

############################################################################################
# Sorteio das Telas
faseMeio = random.randint(0, (len(meio) - 1))
faseFim = random.randint(0, (len(fim) - 1))

faseMeio = meio[faseMeio]
faseFim = fim[faseFim]
faseInicio = 'chegada_castelo'
faseChefao = 'luta_contra_dragao'
# print(faseInicio)
# print(faseMeio)
# print(faseFim)
# print(faseChefao)
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

# print(vetInicio)
# print(vetMeio)
# print(vetFim)
# print(vetChefao)
##########################################################################################


#########################################################################################
# Sorteando as Plavras
palavraNivelFacilInicio = []
palavraNivelFacilMeio = []
palavraNivelFacilFim = []

palavraNivelDificilInicio = []
palavraNivelDificilMeio = []
palavraNivelDificilFim = []

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


# print('################# ')
# print('Inicio - Facil: ')
# print(palavraNivelFacilInicio )
# print('################# ')

# print('Meio - Facil: ')
# print(palavraNivelFacilMeio )
# print('################# ')

# print('Fim - Facil: ' )
# print(palavraNivelFacilFim )
# print('################# ')


palavraNivelMedioInicio = []
palavraNivelMedioMeio = []
palavraNivelMedioFim = []
ent = 0
sortTemporario = ''
# for faseMedio in range(0, 10):
#     if faseMedio > -1 and faseMedio < 2:

#         if len(palavraNivelMedioInicio) == 0:
#             palavraNivelMedioInicio.append(random.choice(vetMeio))
#         else:
#             while (nRepetir == 1):
#                 if ent != 1:
#                     sortTemporario = random.choice(vetMeio)
#                     # print(palavraNivelMedioInicio[0], sortTemporario )
#                     if palavraNivelMedioInicio[0] == sortTemporario:
#                         nRepetir = 1
#                     else:
#                         palavraNivelMedioInicio.append(sortTemporario)
#                         # print( sortTemporario )
#                         nRepetir = 0
#                         ent = 1

#                 sortTemporario = random.choice(vetMeio)
#                 if palavraNivelMedioInicio[0] == sortTemporario or palavraNivelMedioInicio[1] == sortTemporario:
#                     nRepetir = 1
#                 else:
#                     palavraNivelMedioInicio.append(sortTemporario)
#                     nRepetir = 0
#                 # else:
#                 #     if len(palavraNivelMedioInicio) == 1:
#                 #         palavraNivelMedioInicio.append(random.choice(vetMeio))
#                 #     else:
#                 #         if palavraNivelMedioInicio[1] == sortTemporario:
#                 #             nRepetir = 1
#                 #         else:
#                 #             if len(palavraNivelMedioInicio) == 2:
#                 #                 palavraNivelMedioInicio.append(random.choice(vetMeio))
#                 #             else:
#                 #                 if palavraNivelMedioInicio[2] == sortTemporario:
#                 #                     nRepetir = 1
#                 #                 else:
#                 #                     if len(palavraNivelMedioInicio) == 3:
#                 #                         palavraNivelMedioInicio.append(random.choice(vetMeio))
#                 #                         nRepetir = 0
#                 #                     else:
#                 #                         if palavraNivelMedioInicio[3] == sortTemporario:
#                 #                             nRepetir = 1
#                 #                         else:
#                 #                             palavraNivelMedioInicio.append(random.choice(vetMeio))
#                 #                             nRepetir = 0
#         nRepetir = 1

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

print('################# ')
print('Inicio - Medio: ')
print(palavraNivelMedioInicio)
print('################# ')

print('Meio - Medio: ')
print(palavraNivelMedioMeio)
print('################# ')

print('Fim - Medio: ')
print(palavraNivelMedioFim)
print('################# ')
print('')
print('')
print('')
