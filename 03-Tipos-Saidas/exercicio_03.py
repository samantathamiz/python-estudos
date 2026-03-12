nome = 'João'
nota = 10
print (('A nota de %s foi %s') %(nome, nota))                             #variáveis informadas em TUPLA (explicitadas posteriormente)
nome = 'José Maria'
print (('A nota de %s foi %s') %(nome, nota))
nome = 'Carlos'
nota = 7
print (('A nota de %s foi %s') %(nome, nota))
media = 8.65
print (('A nota de %s foi %s e a média do semestre foi %s') %(nome, nota, media))
print ('A nota de %(n1)s foi %(n2)s' % {'n1': nome, 'n2': nota})           #passar como dicionário (também compostas explicadas posteriormente)
print ('A nota de {} foi {}'.format(nome, nota))                           #.format também explicitar posteriormente as variáveis
print (f'A nota de {nome} foi {nota}')                                     #f-string - as variáveis são passadas como parâmetros
print ('A nota de' + nome + 'foi' + str(nota))                             #converter para strings usando operador '+' para concatená-las
