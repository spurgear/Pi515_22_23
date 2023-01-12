def greet(name):
  try:
    greeting = "Hello " + name + "!"
    print(greeting)
  # Add TypeError handling
  # Add a catch-all exception
  except TypeError:
    pass
  except:
    pass


# Test the function below

greet("ABC")
greet(123)