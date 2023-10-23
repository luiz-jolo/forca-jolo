import re

def valida_string(string_digitada):
    if(len(string_digitada) > 1):
        print('Digite somente 1 letra')
    elif(len(string_digitada) <= 0):
        print('Digite ao menos 1 letra')
    else:
        if(valida_letra_brasileira(string_digitada)):
            print('Passou na validação !!!')
        else:
            print('Não passou na validação :(')

def valida_letra_brasileira(texto):
    if re.match(r'^[a-zA-ZáàâãéèêíïóôõúçÁÀÂÃÉÈÊÍÏÓÔÕÚÇ]$', texto):
        return True
    else:
        return False