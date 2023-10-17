from interpreter.expr.Expr import Expr
from interpreter.expr.Variable import Variable
from interpreter.Commands.Command import Command

class Output_Command(Command):
  def __init__(self, linha, expr):
    super().__init__(linha)
    self.expr = expr

  def execute(self):
    print(self.expr.execute())