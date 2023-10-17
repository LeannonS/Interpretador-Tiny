from interpreter.expr.Expr import Expr
from interpreter.expr.Variable import Variable
from interpreter.Commands.Command import Command

class While_Command(Command):
  def __init__(self, linha, BoolCondition, commands):
    super().__init__(linha)
    self.BoolCondition = BoolCondition
    self.commands = commands

  def execute(self):
    while self.BoolCondition.execute():
      self.commands.execute()