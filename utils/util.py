import inspect
from os import system, name

class InterfaceException(Exception):
  def __init__(self, instance):
    cn = instance.__class__.__name__
    sn = instance.__class__.__bases__[0].__name__
    if sn == 'object':
      self.message = f'Classe "{cn}" é uma interface e necessita de uma classe herdeira'
      self.message += f' que implemente o método "{inspect.stack()[1][3]}"'
    else:
      self.message = f'Classe "{cn}"  precisa implementar o método '
      self.message += f'"{inspect.stack()[1][3]}" da interface "{sn}"'
    super().__init__(self.message)

class AbstractException(Exception):
  def __init__(self, instance):
    cn = instance.__class__.__name__
    super().__init__(f'Classe abstrata "{cn}" não pode instanciar um objeto')



def interface_exception(instance):
  if instance:
    raise InterfaceException(instance)

def abstract_exception(instance):
  sn = instance.__class__.__bases__[0].__name__
  if sn == 'object':
    raise AbstractException(instance)

def cls():
  system('cls' if name == 'nt' else 'clear')
