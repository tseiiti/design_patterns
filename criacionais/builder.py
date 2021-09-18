from abc import ABC, abstractmethod

'''
O Builder é um padrão de projeto criacional que permite a você construir 
objetos complexos passo a passo. O padrão permite que você produza diferentes 
tipos e representações de um objeto usando o mesmo código de construção.

O objeto final pode ter diferentes resultados de acordo com a forma de 
construir. Pode ter vários produtos, construtores, diretores.
'''

class Produto():
  def __init__(self) -> None:
    self.partes = []

  def adiciona(self, part) -> None:
    self.partes.append(part)

  def listar_partes(self) -> None:
    print(f"Partes do produto: {', '.join(self.partes)}", end='')
    print('\n')


class ConstrutorInterface(ABC):
  @abstractmethod
  def produzir_parte_a(self) -> None:
    pass

  @abstractmethod
  def produzir_parte_b(self) -> None:
    pass

  @abstractmethod
  def produzir_parte_c(self) -> None:
    pass


class Construtor(ConstrutorInterface):
  def __init__(self) -> None:
    self._produto = Produto()
    
  @property
  def produto(self) -> Produto:
    product = self._produto
    self._produto = Produto()
    return product

  def produzir_parte_a(self) -> None:
    self._produto.adiciona('Parte A1')

  def produzir_parte_b(self) -> None:
    self._produto.adiciona('Parte B1')

  def produzir_parte_c(self) -> None:
    self._produto.adiciona('Parte C1')


class Diretor:
  def produto_simples(self) -> None:
    self.builder.produzir_parte_a()

  def produto_completo(self) -> None:
    self.builder.produzir_parte_a()
    self.builder.produzir_parte_b()
    self.builder.produzir_parte_c()



if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')

  diretor = Diretor()
  construtor = Construtor()
  diretor.builder = construtor

  print('Construindo um produto simples: ')
  diretor.produto_simples()
  construtor.produto.listar_partes()

  print('Construindo um produto completo: ')
  diretor.produto_completo()
  construtor.produto.listar_partes()

  print('Construindo um produto personalizado sem o diretor: ')
  construtor.produzir_parte_a()
  construtor.produzir_parte_b()
  construtor.produto.listar_partes()


