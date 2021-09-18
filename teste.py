
from os import system, name
system('cls' if name == 'nt' else 'clear')

from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
   @abstractmethod
   def method_to_implement(self, input):
      return
class Foo(Shape):
   # pass
   def method_to_implement(self, input):
      return

# shape = Shape()
foo = Foo()




# class Button(object):
#    html = ""
#    def get_html(self):
#       return self.html

# class Image(Button):
#    html = "<img></img>"

# class Input(Button):
#    html = "<input></input>"

# class Flash(Button):
#    html = "<obj></obj>"

# class ButtonFactory():
#    def create_button(self, typ):
#       targetclass = typ.capitalize()
#       return globals()[targetclass]()

# buttonFactory = ButtonFactory()
# buttons = ['image', 'input', 'flash']
# list_objs = []
# for b in buttons:
#    list_objs.append(buttonFactory.create_button(b))

# for l in list_objs:
#   print(l.__class__.__name__, l.get_html())

