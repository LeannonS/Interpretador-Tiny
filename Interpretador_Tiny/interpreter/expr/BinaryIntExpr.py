from enum import Enum
from interpreter.expr.Expr import Expr

class BinaryIntExpr(Expr):
  Op = Enum('Op', ['TT_ADD', 'TT_SUB', 'TT_MUL', 'TT_DIV', 'TT_MOD', 'TT_POT'])

  OPERATOR_FUNCTIONS = {
    Op.TT_ADD: lambda x, y: x + y,
    Op.TT_SUB: lambda x, y: x - y,
    Op.TT_MUL: lambda x, y: x * y,
    Op.TT_DIV: lambda x, y: x // y,
    Op.TT_MOD: lambda x, y: x % y,
    Op.TT_POT: lambda x, y: x ** y,
  }

  def __init__(self, linha, left, operation, right):
    super().__init__(linha)
    self.left = left
    self.operation = operation
    self.right = right

  def execute(self):
    expr1 = int(self.left.execute())
    expr2 = int(self.right.execute())

    operator_func = self.OPERATOR_FUNCTIONS.get(self.operation)
    if operator_func:
      return operator_func(expr1, expr2)
      
    else:
      raise ValueError("Operador inválido")
