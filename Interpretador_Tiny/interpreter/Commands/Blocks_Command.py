from interpreter.expr.Expr import Expr
from interpreter.expr.Variable import Variable
from interpreter.Commands.Command import Command

class Blocks_Command(Command):
  def __init__(self, linha):
    super().__init__(linha)
    self.commands_list = []

  def addCommand(self, command_aux):
    self.commands_list.append(command_aux)

  def execute(self):
    for object in self.commands_list:
      object.execute()