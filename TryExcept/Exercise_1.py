import ast

# Create a try/except that will run successfully
try:
  # Add something that will run successfully
  p = open("Exercise_2.py", 'r')
  ast.parse(p.read())

except SyntaxError as ex:
  print(f"Got syntax error! {ex}")

except Exception as ex:
  print(ex)
  print(type(ex))
  print("try/except 1 produced an error")

  # Create a try/except that will fail to run
try:
  # Add something that will not run successfully
  1 + 1
except Exception as ex:
  print("try/except 2 produced an error")
  print(ex)

# The whole program should still complete, despite an error occurring above
print("program did not abort")
