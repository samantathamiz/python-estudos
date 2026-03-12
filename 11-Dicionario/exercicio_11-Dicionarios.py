pessoa = {                                         #cria variável pessoa para guardar informações
    "nome":"Ana",                                  #chaves { } significam que estou criando um dicionário 
    "idade":"25"    
}
for chave,valor in pessoa.items():                 #chave e valor são etiquetas
    print(chave, valor)                            #chaves => nome e idade são chaves
                                                   #Ana e 25 são valores

                                                   # FOR está percorrendo o dicionário
                                                   # FOR = loop (repetição)
                                                   # chave, valor => a cada volta do loop, me dê a chave e o valor
                                                   # in significa dentro de.
                                                   # .items () pega cada par chave + valor do dicionário
                                                   # ou seja:
                                                   # ("nome","Ana")
                                                   # ("idade","25")    
