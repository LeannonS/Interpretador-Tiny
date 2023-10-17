from enum import Enum
from interpreter.expr.Expr import Expr

class NotBoolExpr (Expr): 
  def __init__(self, linha, bool_expr):
    super().__init__(linha)
    self.bool_expr = bool_expr

  def execute(self):
    return not self.bool_expr.execute()