from enum import Enum
from interpreter.expr.Expr import Expr

class ReadIntExpr(Expr):
  def __init__(self, linha):
    super().__init__(linha)

  def execute(self):
    while True:
      try:
        var = int(input())
        return var
        
      except ValueError:
        pass