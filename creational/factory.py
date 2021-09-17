from utils import *

class Product():
  def operation(self) -> str:
    interface_exception(self)

class ConcreteProduct1(Product):
  def operation(self) -> str:
    return '{Resultado do Produto de Concreto1}'

class ConcreteProduct2(Product):
  def operation(self) -> str:
    return '{Resultado do Produto de Concreto2}'

class Creator():
  def __init__(self):
    abstract_exception(self)
      
  def factory_method(self):
    interface_exception(self)
    
  def some_operation(self):
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

# if __name__ == '__main__':
#   cls()
#   print('\nApp: lançado com o ConcreteCreator1.')
#   client_code(ConcreteCreator1())
#   print('\nApp: lançado com o ConcreteCreator2.')
#   client_code(ConcreteCreator2())
