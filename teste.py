from os import system, name
system('cls' if name == 'nt' else 'clear')

def p(ver):
  print(ver)
  print('- Old List:', old_list)
  print('- ID Old..:', id(old_list))
  print('- New List:', new_list)
  print('- ID New..:', id(new_list))
  
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
new_list[2][2] = 9
old_list.append([4, 4, 4])
old_list[1][1] = 'AA'
old_list[3][1] = 3
p('Versão 1:')

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list.copy()
new_list[2][2] = 9
old_list.append([4, 4, 4])
old_list[1][1] = 'AA'
old_list[3][1] = 3
p('Versão 2:')

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.copy(old_list)
new_list[2][2] = 9
old_list.append([4, 4, 4])
old_list[1][1] = 'AA'
old_list[3][1] = 3
p('Versão 3:')

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = copy.deepcopy(old_list)
new_list[2][2] = 9
old_list.append([4, 4, 4])
old_list[1][1] = 'AA'
old_list[3][1] = 3
p('Versão 4:')

