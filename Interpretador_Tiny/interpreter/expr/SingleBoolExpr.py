from enum import Enum
from interpreter.expr.Expr import Expr

class SingleBoolExpr (Expr):
  Op = Enum('Op', ['TT_EQUAL','TT_NOT_EQUAL','TT_LOWER','TT_LOWER_EQUAL','TT_GREATER', 'TT_GREATER_EQUAL'])

  OPERATOR_FUNCTIONS = {
    Op.TT_EQUAL: lambda x, y: x == y,
    Op.TT_NOT_EQUAL: lambda x, y: x != y,
    Op.TT_LOWER: lambda x, y: x < y,
    Op.TT_LOWER_EQUAL: lambda x, y: x <= y,
    Op.TT_GREATER: lambda x, y: x > y,
    Op.TT_GREATER_EQUAL: lambda x, y: x >= y,
  }

  def __init__(self, linha, left, logical_operator, right):
    super().__init__(linha)
    self.left = left
    self.right = right
    self.logical_operator = logical_operator

  def execute(self):
    expr1 = int(self.left.execute())
    expr2 = int(self.right.execute())

    operator_func = self.OPERATOR_FUNCTIONS.get(self.logical_operator)
    if operator_func:
        return operator_func(expr1, expr2)
    else:
        raise ValueError("Operador lógico inválido")