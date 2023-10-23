from Tools import gerador_palavra, valida_entrada, separador


print('#####################')
print('Bem vindo ao clássico jogo da F O R C A')
print('#####################')

animais = ['rinoceronte', 'macaco', 'arara', 'capivara', 'jacare', 'zebra']

def jogar():
    
    animal = gerador_palavra.gerar_palavra(animais)
    chute = input('Digite uma letra\n')
    retorno = valida_entrada.valida_string(chute)

jogar()