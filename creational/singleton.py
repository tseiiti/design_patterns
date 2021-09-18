class SingletonMeta(type):
  _instances = {}

  def __call__(self, *args, **kwargs):
    if self not in self._instances:
      instance = super().__call__(*args, **kwargs)
      self._instances[self] = instance
    return self._instances[self]


class Singleton(metaclass=SingletonMeta):
  def some_business_logic(self):
    """
    Finally, any singleton should define some business logic, which can be
    executed on its instance.
    """
    # ...


if __name__ == "__main__":
  s1 = Singleton()
  s2 = Singleton()

  if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
  else:
    print("Singleton failed, variables contain different instances.")

    