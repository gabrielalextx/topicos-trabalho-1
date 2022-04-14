# -*- coding: utf-8 -*-
def Bissexto(ano):
    #verifica se é ordinário
    ord = 1
    #verifica se é bissexto
    bis = 0
    #string para fazer o print de acordo com o tipo de ano
    tipo = ''
    
    #input do ano e se verifica se é inválido
    if (ano < 2000) or (ano > 10000):
        tipo += 'INVÁLIDO'
        #print(tipo)
        return tipo
    #calcula se é bissexto
    if (ano % 4 == 0) and (not (ano % 100 == 0) or (ano % 400 == 0)):
        ord = 0
        bis = 1
        tipo += 'Bissexto'
    #calcula se é huluculu
    if (ano % 15 == 0):
        ord = 0
        if (tipo != ''):
            tipo += ', Huluculu'
        else:
            tipo += 'Huluculu'
    #calcula se é bulukulu
    if (ano % 55 == 0) and bis:
        tipo += ', Bulukulu'
    #se nenhum dos anteriores, é ordinário
    if ord:
        tipo += 'Ordinário'
    #print(tipo)
    return tipo