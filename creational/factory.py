from abc import ABC, abstractmethod

'''
O Factory Method é um padrão criacional de projeto que fornece uma interface 
para criar objetos em uma superclasse, mas permite que as subclasses alterem 
o tipo de objetos que serão criados.

Permite criar objetos que possuem a mesma função que pode ser feita de formas
diferentes. As funções devem ter a mesma entreda e saida.
No python acho que não precisa da classe criadora.
'''

class Product(ABC):
  @abstractmethod
  def operation(self) -> str:
    pass

class ConcreteProduct1(Product):
  def operation(self) -> str:
    return '{Resultado do Produto de Concreto1}'

class ConcreteProduct2(Product):
  def operation(self) -> str:
    return '{Resultado do Produto de Concreto2}'

class Creator(ABC):
  @abstractmethod
  def factory_method(self) -> Product:
    pass
  def some_operation(self) -> str:
    product = self.factory_method()
    result = f'Criador: o mesmo código do criador acabou de funcionar com {product.operation()}'
    return result

class ConcreteCreator1(Creator):
  def factory_method(self) -> Product:
    return ConcreteProduct1()

class ConcreteCreator2(Creator):
  def factory_method(self) -> Product:
    return ConcreteProduct2()

def client_code(creator: Creator) -> None:
  print(f'Cliente: Não conheço a classe do criador, mas ainda funcion\n'
        f'{creator.some_operation()}')

if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')
  print('\nApp: lançado com o ConcreteCreator1.')
  client_code(ConcreteCreator1())
  print('\nApp: lançado com o ConcreteCreator2.')
  client_code(ConcreteCreator2())
