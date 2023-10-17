from interpreter.expr.Expr import Expr
from interpreter.expr.Variable import Variable
from interpreter.Commands.Command import Command

class If_Command (Command):
  def __init__(self, linha, bool_expr, then_command, else_command):
    super().__init__(linha)
    self.bool_expr = bool_expr
    self.then_command = then_command
    self.else_command = else_command

  def execute(self):
    if self.bool_expr.execute():
      self.then_command.execute()
      
    else:
      if self.else_command:
        self.else_command.execute()   