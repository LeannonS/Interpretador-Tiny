from enum import Enum
from interpreter.expr.Expr import Expr

class Variable (Expr):
  variables_map = {}

  def __init__(self, nome):
    super().__init__(-1)
    self.nome = nome
    self.valor = 0

  def getVariavel(self, nome):
    var = self.variables_map.get(nome)

    if var is None:
      var = Variable(nome)
      self.variables_map[nome] = var

    return var

  def setValue(self, valor):
    self.valor = valor

  def execute(self):
    return self.valor