'''
O Adapter é um padrão de projeto estrutural que permite objetos com interfaces 
incompatíveis colaborarem entre si.
'''



class Normal:
  def request(self) -> str:
    return 'Alvo: comportamento padrão.'


class Estranho:
  def specific_request(self) -> str:
    return '.rodatpada od laicepse otnematropmoC'


class Adaptador(Normal, Estranho):
  def request(self) -> str:
    return f'Adaptador: (traduzido) {self.specific_request()[::-1]}'


def client_code(normal: 'Normal') -> None:
  print(normal.request())


if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')

  print('Cliente: Posso trabalhar muito bem com os objetos Normal:')
  normal = Normal()
  client_code(normal)
  print()

  estranho = Estranho()
  print('Cliente: A classe Estranho tem uma interface estranha. '
        'Veja, eu não entendo:')
  print(f'Adaptee: {estranho.specific_request()}')
  print()

  print('Cliente: Mas posso trabalhar com isso por meio do Adaptador:')
  adaptador = Adaptador()
  client_code(adaptador)
