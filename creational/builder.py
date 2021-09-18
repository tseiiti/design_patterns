from abc import ABC, abstractmethod


class Product1():
  def __init__(self) -> None:
    self.parts = []

  def add(self, part) -> None:
    self.parts.append(part)

  def list_parts(self) -> None:
    print(f"Partes do produto: {', '.join(self.parts)}", end='')
    print('\n')


class Builder(ABC):
  @abstractmethod
  def produce_part_a(self) -> None:
    pass

  @abstractmethod
  def produce_part_b(self) -> None:
    pass

  @abstractmethod
  def produce_part_c(self) -> None:
    pass


class ConcreteBuilder1(Builder):
  def __init__(self) -> None:
    self._product = Product1()
    
  @property
  def product(self) -> Product1:
    product = self._product
    self._product = Product1()
    return product

  def produce_part_a(self) -> None:
    self._product.add('Parte A1')

  def produce_part_b(self) -> None:
    self._product.add('Parte B1')

  def produce_part_c(self) -> None:
    self._product.add('Parte C1')


class Director:
  def build_minimal_viable_product(self) -> None:
    self.builder.produce_part_a()

  def build_full_featured_product(self) -> None:
    self.builder.produce_part_a()
    self.builder.produce_part_b()
    self.builder.produce_part_c()



if __name__ == '__main__':
  from os import system, name
  system('cls' if name == 'nt' else 'clear')

  director = Director()
  builder = ConcreteBuilder1()
  director.builder = builder

  print('Construindo um produto mínimo: ')
  director.build_minimal_viable_product()
  builder.product.list_parts()

  print('Construindo um produto completo: ')
  director.build_full_featured_product()
  builder.product.list_parts()

  print('Construindo um produto personalizado sem o diretor: ')
  builder.produce_part_a()
  builder.produce_part_b()
  builder.product.list_parts()


