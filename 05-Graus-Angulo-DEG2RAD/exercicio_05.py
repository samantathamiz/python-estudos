import numpy as np                                                       #importar a biblioteca NumPy
while True:                                                              #loop infinito (tudo abaixo do while identado com 4 espaços)
    angulo = float(input('Informe um valor para o ângulo: '))
    radiano = np.deg2rad(angulo)                                         #converter graus para radianos
    seno = np.sin(radiano)                                               #chamar a função seno da biblioteca NumPy
    cosseno = np.cos(radiano)                                            #chamar a função cosseno da biblioteca NumPy
    tangente = np.tan(radiano)                                           #chamar a função tangente da biblioteca NumPy
    print (f'Seno: {seno: .2f}')                                         #imprime seno com 2 casas decimais
    print (f'Cosseno: {cosseno: .2f}')                                   #imprime cosseno com 2 casas decimais
    print (f'Tangente: {tangente: .2f}')                                 #imprime tangente com 2 casas decimais
    continuar = input('Deseja calcular um novo ângulo? (s/n): ')
    if continuar.lower() == 'n':                                         #abaixo do while 4 espaçoes e abaixo do if 8 espaços
        print('Você chegou ao fim dos cálculos, até a próxima!') 
                                                                         #se continuar = true = loop continua, senão a função para e printa mensagem 
        break
                                                                         #foi necessário importar a biblioteca NumPy 
                                                                              (tanto chamando na 1ª linha de código quanto via terminal)
                                                                         # no terminal a importação foi feita com o comando: pip install numpy 
