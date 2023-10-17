from interpreter.expr.Expr import Expr
from interpreter.expr.Variable import Variable
from interpreter.Commands.Command import Command

class Assign_Command(Command):
  def __init__(self, linha, variable, expr):
    super().__init__(linha)
    self.variable = variable
    self.expr = expr

  def execute(self):
    valor = int(self.expr.execute())
    self.variable.setValue(valor)