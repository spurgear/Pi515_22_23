"""Quadratic Formula Solver.
"""

import math


def solve(a, b, c):
  """Takes parameters a, b, c where ax^2 + bx + c = 0.
  """
  sqrt = math.sqrt(b * b - 4 * a * c)
  return (-b + sqrt) / 2.0, (-b - sqrt) / 2.0


if __name__ == '__main__':
  print(solve(1, 4, 3))
