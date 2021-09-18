from os import system, name
system('cls' if name == 'nt' else 'clear')

'''
O Prototype é um padrão de projeto criacional que permite copiar objetos 
existentes sem fazer seu código ficar dependente de suas classes.

Operador "=" faz uma nova referencia para o mesmo objeto.
Método .copy() faz refencia mas permite "adicionar novos" conteúdos. É útil 
pois cria um novo id.
Função copy.deepcopy é que realmente cria um novo objeto clonado.
'''

def p(ver):
  print(ver)
  print('- Lista Velha:', lista_velha)
  print('- Id Velha...:', id(lista_velha))
  print('- Lista Nova.:', lista_nova)
  print('- Id Nova....:', id(lista_nova))
  
lista_velha = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
lista_nova = lista_velha
lista_nova[2][2] = 9
lista_velha.append([4, 4, 4])
lista_velha[1][1] = 'AA'
lista_velha[3][1] = 3
p('Versão 1:')

lista_velha = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
lista_nova = lista_velha.copy()
lista_nova[2][2] = 9
lista_velha.append([4, 4, 4])
lista_velha[1][1] = 'AA'
lista_velha[3][1] = 3
p('Versão 2:')

import copy
lista_velha = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
lista_nova = copy.copy(lista_velha)
lista_nova[2][2] = 9
lista_velha.append([4, 4, 4])
lista_velha[1][1] = 'AA'
lista_velha[3][1] = 3
p('Versão 3:')

import copy
lista_velha = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
lista_nova = copy.deepcopy(lista_velha)
lista_nova[2][2] = 9
lista_velha.append([4, 4, 4])
lista_velha[1][1] = 'AA'
lista_velha[3][1] = 3
p('Versão 4:')

