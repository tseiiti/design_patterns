from abc import ABC, abstractmethod

'''
O Abstract Factory é um padrão de projeto criacional que permite que você 
produza famílias de objetos relacionados sem ter que especificar suas classes 
concretas.

Permite criar um conjuto de objetos que também possuem um conjunto de funções
semelhantes. Os objetos devem ter as mesmas funções da família.
'''


class ProdutoAAbstract(ABC):
  @abstractmethod
  def funcao_util_a(self) -> str:
    pass


class ProdutoA1(ProdutoAAbstract):
  def funcao_util_a(self) -> str:
    return 'resultado do produto A1'


class ProdutoA2(ProdutoAAbstract):
  def funcao_util_a(self) -> str:
    return 'resultado do produto A2'


class ProdutoBAbstract(ABC):
  @abstractmethod
  def funcao_util_b(self) -> str:
    pass

  @abstractmethod
  def outra_funcao_util_b(self, colaborador: ProdutoAAbstract) -> str:
    pass


class ProdutoB1(ProdutoBAbstract):
  def funcao_util_b(self) -> str:
    return 'O resultado do produto B1.'
  def outra_funcao_util_b(self, colaborador: ProdutoAAbstract) -> str:
    result = colaborador.funcao_util_a()
    return f'O resultado do B1 colaborando com o ({result})'


class ProdutoB2(ProdutoBAbstract):
  def funcao_util_b(self) -> str:
    return 'O resultado do produto B2.'
  def outra_funcao_util_b(self, colaborador: ProdutoAAbstract) -> str:
    result = colaborador.funcao_util_a()
    return f'O resultado do B2 colaborando com o ({result})'


class FabricaAbstract(ABC):
  @abstractmethod
  def cria_produto_a(self) -> ProdutoAAbstract:
    pass

  @abstractmethod
  def cria_produto_b(self) -> ProdutoBAbstract:
    pass


class Fabrica1(FabricaAbstract):
  def cria_produto_a(self) -> ProdutoAAbstract:
    return ProdutoA1()
  def cria_produto_b(self) -> ProdutoBAbstract:
    return ProdutoB1()


class Fabrica2(FabricaAbstract):
  def cria_produto_a(self) -> ProdutoAAbstract:
    return ProdutoA2()

  def cria_produto_b(self) -> ProdutoBAbstract:
    return ProdutoB2()


def client_code(fabrica: FabricaAbstract) -> None:
  produto_a = fabrica.cria_produto_a()
  produto_b = fabrica.cria_produto_b()
  print(f'{produto_b.funcao_util_b()}')
  print(f'{produto_b.outra_funcao_util_b(produto_a)}')

if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')

  print('Cliente: Testando o código do cliente com o primeiro tipo de fábrica:')
  client_code(Fabrica1())
  print('\nCliente: Testando o mesmo código de cliente com o segundo tipo de fábrica:')
  client_code(Fabrica2())
