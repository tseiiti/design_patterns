from abc import ABC, abstractmethod

'''
O Factory Method é um padrão criacional de projeto que fornece uma interface 
para criar objetos em uma superclasse, mas permite que as subclasses alterem 
o tipo de objetos que serão criados.

Permite criar objetos que possuem a mesma função que pode ser feita de formas
diferentes. As funções devem ter a mesma entreda e saida.
No python acho que não precisa da classe criadora.
'''


class ProdutoInterface(ABC):
  @abstractmethod
  def operacao(self) -> str:
    pass


class Produto1(ProdutoInterface):
  def operacao(self) -> str:
    return '{Resultado do Produto 1}'


class Produto2(ProdutoInterface):
  def operacao(self) -> str:
    return '{Resultado do Produto 2}'


class FabricaInterface(ABC):
  @abstractmethod
  def fabricar(self) -> ProdutoInterface:
    pass

  def chama_operacao(self) -> str:
    product = self.fabricar()
    result = f'Criador: o mesmo código da fábrica acabou de funcionar com {product.operacao()}'
    return result


class Fabrica1(FabricaInterface):
  def fabricar(self) -> ProdutoInterface:
    return Produto1()


class Fabrica2(FabricaInterface):
  def fabricar(self) -> ProdutoInterface:
    return Produto2()


def client_code(creator: FabricaInterface) -> None:
  print(f'Cliente: Não conheço a classe do criador, mas ainda funciona.'
        f'\n{creator.chama_operacao()}')

if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')
  print('\nApp: lançado com o Fabrica 1.')
  client_code(Fabrica1())
  print('\nApp: lançado com o Fabrica 2.')
  client_code(Fabrica2())

