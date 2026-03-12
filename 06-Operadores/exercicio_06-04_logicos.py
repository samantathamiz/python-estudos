print(0 and 16)             #zero é falso pois zero representa ausência/ algoritmo pára e retorna o falso da expressão
print(not 0)                #not 0 = not false = true / ou zero false = true
print(2 and 19)             #retorna 2 pois verdadeiro e pára. se 2 fosse falso retornaria o próximo verdadeiro
print(1 or 20)              #retorna 1 pois verdadeiro e pára. se 1 fosse falso retornaria p próximo verdadeiro
print(2 or not 33)          #resolve o not 33, 33 diferente de 0, então=true, depois not 33 inverte = false 
print(not 4 or 54)          #resolve o 4, 4=true, inverte por causa do not, então 4=false, 54 verdadeiro, imprime 54
print(not 6 or not 888)     #resolve 6 e 888 = verdadeiro porém not inverte, então retorna false em ambos
