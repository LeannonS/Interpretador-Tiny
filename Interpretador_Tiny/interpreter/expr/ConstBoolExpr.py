from enum import Enum
from interpreter.expr.Expr import Expr

class ConstBoolExpr (Expr):
  def __init__(self, linha, booleano):
    super().__init__(linha)
    self.booleano = booleano

  def execute(self):
    return self.booleano