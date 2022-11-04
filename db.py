palavraNivelMedioInicio = []
palavraNivelMedioMeio = []
palavraNivelMedioFim = []

sortTemporario = ''
for faseMedio in range(0,10):
  if faseMedio == 0 and faseMedio < 4:
    if len(palavraNivelMedioInicio) == 0:    
      palavraNivelMedioInicio.append(random.choice(vetMeio))   
    else:
      while (nRepetir == 1):
        sortTemporario = random.choice(vetMeio)
        if palavraNivelMedioInicio[0] == sortTemporario:
          nRepetir = 1
        else:
            if palavraNivelMedioInicio[1] == sortTemporario:
                nRepetir = 1
            else:
                if palavraNivelMedioInicio[2] == sortTemporario:
                    nRepetir = 1
                else:
                    if palavraNivelMedioInicio[3] == sortTemporario:
                        nRepetir = 1
                    else:
                        palavraNivelMedioInicio.append(random.choice(vetMeio)) 
                        nRepetir = 0
    nRepetir = 1 
  elif faseMedio > 3 and faseMedio < 7:
    if len(palavraNivelMedioMeio) == 0:    
      palavraNivelMedioMeio.append(random.choice(vetMeio))   
    else:
      while (nRepetir == 1):
        sortTemporario = random.choice(vetMeio)
        if palavraNivelMedioMeio[0] == sortTemporario:
          nRepetir = 1
        else:
          palavraNivelMedioMeio.append(random.choice(vetMeio)) 
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
          palavraNivelMedioFim.append(random.choice(vetFim)) 
          nRepetir = 0
    nRepetir = 1  
    
print('################# ')
print('Inicio - Medio: ')
print(palavraNivelMedioInicio )
print('################# ')

print('Meio - Medio: ')
print(palavraNivelMedioMeio )
print('################# ')

print('Fim - Medio: ' )
print(palavraNivelMedioFim )
print('################# ')