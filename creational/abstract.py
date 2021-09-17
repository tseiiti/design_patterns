from utils import *

class AbstractProductA():
  def useful_function_a(self) -> str:
    raise InterfaceException(self)

class ConcreteProductA1(AbstractProductA):
  def useful_function_a(self) -> str:
    return 'resultado do produto A1'

class ConcreteProductA2(AbstractProductA):
  def useful_function_a(self) -> str:
    return 'resultado do produto A2'

class AbstractProductB():
  def useful_function_b(self) -> None:
    raise InterfaceException(self)
  def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
    raise InterfaceException(self)

class ConcreteProductB1(AbstractProductB):
  def useful_function_b(self) -> str:
    return 'O resultado do produto B1.'

  def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
    result = collaborator.useful_function_a()
    return f'O resultado do B1 colaborando com o ({result})'

class ConcreteProductB2(AbstractProductB):
  def useful_function_b(self) -> str:
    return 'O resultado do produto B2.'

  def another_useful_function_b(self, collaborator: AbstractProductA):
    result = collaborator.useful_function_a()
    return f'O resultado do B2 colaborando com o ({result})'

class AbstractFactory():
  def create_product_a(self) -> AbstractProductA:
    raise InterfaceException(self)
  def create_product_b(self) -> AbstractProductB:
    raise InterfaceException(self)

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
  print('\nCliente: Testando o código do cliente com o primeiro tipo de fábrica:')
  client_code(ConcreteFactory1())
  print('\nCliente: Testando o mesmo código de cliente com o segundo tipo de fábrica:')
  client_code(ConcreteFactory2())
