from enum import Enum
from interpreter.expr.Expr import Expr

class ConstIntExpr (Expr):
  def __init__(self, linha, valor):
    super().__init__(linha)
    self.valor = valor

  def execute(self):
    return self.valor