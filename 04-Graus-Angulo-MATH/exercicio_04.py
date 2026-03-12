import math
angulo = float(input('Informe um valor em graus para um ângulo: '))       #variável armazena float e já pede valor
print (f'O ângulo informado foi {angulo}')                                #printar o valor informado (para variável)
radiano = math.radians(angulo)                                            #converter graus p/ radiano (funções sin, cos e tangente trabalham com radianos)
seno = math.sin(radiano)                                                  #função calcula seno puxando da biblioteca math 
cosseno = math.cos(radiano)                                               #função calcula cosseno puxando da biblioteca math 
tangente = math.tan(radiano)                                              #função calcula tangente puxando da biblioteca math 
print (f'Seno: {seno: .2f}')                                              #imprimindo o valor encontrado para seno / .2f imprime só 2 casas decimais
print (f'Cosseno: {cosseno: .2f}')                                        #imprimindo o valor encontrado para cosseno
print (f'Tangente: {tangente: .2f}')                                      #imprimindo o valor encontrado para tangete
