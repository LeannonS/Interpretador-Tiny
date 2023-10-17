from enum import Enum
from interpreter.expr.Expr import Expr

class NegIntExpr (Expr):
  def __init__(self, linha, int_expr):
    super().__init__(linha)
    self.int_expr = int_expr

  def execute(self):
    return -self.int_expr.execute()