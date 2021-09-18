from abc import ABC, abstractmethod

'''
O Abstract Factory é um padrão de projeto criacional que permite que você 
produza famílias de objetos relacionados sem ter que especificar suas classes 
concretas.

Permite criar um conjuto de objetos que também possuem um conjunto de funções
semelhantes. Os objetos devem ter as mesmas funções da família.
'''


class AbstractProductA(ABC):
  @abstractmethod
  def useful_function_a(self) -> str:
    pass


class ConcreteProductA1(AbstractProductA):
  def useful_function_a(self) -> str:
    return 'resultado do produto A1'


class ConcreteProductA2(AbstractProductA):
  def useful_function_a(self) -> str:
    return 'resultado do produto A2'


class AbstractProductB(ABC):
  @abstractmethod
  def useful_function_b(self) -> str:
    pass

  @abstractmethod
  def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
    pass


class ConcreteProductB1(AbstractProductB):
  def useful_function_b(self) -> str:
    return 'O resultado do produto B1.'
  def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
    result = collaborator.useful_function_a()
    return f'O resultado do B1 colaborando com o ({result})'


class ConcreteProductB2(AbstractProductB):
  def useful_function_b(self) -> str:
    return 'O resultado do produto B2.'
  def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
    result = collaborator.useful_function_a()
    return f'O resultado do B2 colaborando com o ({result})'


class AbstractFactory(ABC):
  @abstractmethod
  def create_product_a(self) -> AbstractProductA:
    pass

  @abstractmethod
  def create_product_b(self) -> AbstractProductB:
    pass


class ConcreteFactory1(AbstractFactory):
  def create_product_a(self) -> AbstractProductA:
    return ConcreteProductA1()
  def create_product_b(self) -> AbstractProductB:
    return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
  def create_product_a(self) -> AbstractProductA:
    return ConcreteProductA2()

  def create_product_b(self) -> AbstractProductB:
    return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
  product_a = factory.create_product_a()
  product_b = factory.create_product_b()
  print(f'{product_b.useful_function_b()}')
  print(f'{product_b.another_useful_function_b(product_a)}')

if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')
  print('\nCliente: Testando o código do cliente com o primeiro tipo de fábrica:')
  client_code(ConcreteFactory1())
  print('\nCliente: Testando o mesmo código de cliente com o segundo tipo de fábrica:')
  client_code(ConcreteFactory2())
