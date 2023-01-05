import random, math
import string

def greeting(name):
  """A greeting to the given name.
  
  
  """
  i = math.pow(2.0, 3.0)
  j = random.randint(0, 10)
  print("Hello,", name, i, j)


if __name__ == '__main__':
  greeting("World")
