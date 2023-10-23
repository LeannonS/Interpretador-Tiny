from lexical.SymbolTable import SymbolTable
from lexical.TokenType import TokenType
from lexical.Lexeme import Lexeme
from lexical.LexicalAnalysis import LexicalAnalysis

from interpreter.Commands.Command import Command
from interpreter.Commands.Blocks_Command import Blocks_Command
from interpreter.Commands.Assign_Command import Assign_Command
from interpreter.Commands.If_Command import If_Command
from interpreter.Commands.While_Command import While_Command
from interpreter.Commands.Output_Command import Output_Command

from interpreter.expr.BinaryIntExpr import BinaryIntExpr
from interpreter.expr.ConstBoolExpr import ConstBoolExpr
from interpreter.expr.ConstIntExpr import ConstIntExpr
from interpreter.expr.NegIntExpr import NegIntExpr
from interpreter.expr.NotBoolExpr import NotBoolExpr
from interpreter.expr.ReadIntExpr import ReadIntExpr
from interpreter.expr.SingleBoolExpr import SingleBoolExpr
from interpreter.expr.Variable import Variable

class SyntaticAnalysis:
  def __init__(self):
    self.lex = None
    self.currentToken = None
    self.currentIndex = 0
    self.tokenList = []

  def showError(self):
    print(f"Linha {self.currentToken.linha}: {self.lex.arquivo_em_linhas[self.currentToken.linha-1]}")
    
    if self.currentToken.type == TokenType.TT_INVALID_TOKEN:
      print(f"Lexema inválido [{self.currentToken.token}]")

    elif self.currentToken.type in [TokenType.TT_UNEXPECTED_EOF, TokenType.TT_END_OF_FILE]:
      print("Fim de arquivo inesperado")

    else:
      print(f"Lexema não esperado [{self.currentToken.token}]")
      
    exit(1)

  # Função usada para avançar para o próximo token esperado se o token atual for do tipo esperado. Se o tipo do token atual não for igual ao expectedToken, ela chama self.showError() para relatar um erro.
  def advance(self, expectedToken):
    if self.currentToken.type == expectedToken:
      self.currentIndex += 1
      if self.currentIndex < self.tamanho_lista:
        self.currentToken = self.tokenList[self.currentIndex]

    else:
        self.showError()

  # Esta função simplesmente avança para o próximo token, independentemente do tipo do token atual. Ela não verifica se o token é do tipo esperado; apenas incrementa o índice atual e atualiza currentToken.
  def nextToken(self):
    self.currentIndex += 1  
    self.currentToken = self.tokenList[self.currentIndex]

  def startLexicalAnalysis(self, input_file):
    self.lex = LexicalAnalysis()
    self.lex.nextToken(self.lex.readFile(input_file))
    self.tokenList = self.lex.tokenList
    self.currentToken = self.tokenList[self.currentIndex]

  def inicio(self, input_file):
    self.startLexicalAnalysis(input_file)
    self.tamanho_lista = len(self.tokenList)
    program_command = self.procProgram()
    self.advance(TokenType.TT_END_OF_FILE)
    
    return program_command

  # <program> ::= program <cmdlist>    
  def procProgram(self):
    self.advance(TokenType.TT_PROGRAM)
    
    return self.procCmdList()

  # <cmdlist> ::= <cmd> { <cmd> }        
  def procCmdList(self):
    linha = int(self.currentToken.linha)
    blocks_commands = Blocks_Command(linha)
    program_command = self.procCmd()
    blocks_commands.addCommand(program_command)

    while self.currentToken.type in [TokenType.TT_VAR, TokenType.TT_OUTPUT, TokenType.TT_IF, TokenType.TT_WHILE]:
      program_command = self.procCmd()
      blocks_commands.addCommand(program_command)

    return blocks_commands

  # <cmd> ::= (<assign> | <output> | <if> | <while>) ;
  def procCmd(self):
    program_command = None

    if self.currentToken.type == TokenType.TT_VAR:
      program_command = self.procAssign()
    elif self.currentToken.type == TokenType.TT_OUTPUT:
      program_command = self.procOutput()
    elif self.currentToken.type == TokenType.TT_IF:
      program_command = self.procIf()
    elif self.currentToken.type == TokenType.TT_WHILE:
      program_command = self.procWhile()
    else:
      self.showError()

    self.advance(TokenType.TT_SEMICOLON)
    
    return program_command 

  # <assign> ::= <var> = <intexpr>
  def procAssign(self):
    var = self.procVar()
    linha = int(self.currentToken.linha)
    self.advance(TokenType.TT_ASSIGN)
    expr = self.procIntExpr()
    
    return Assign_Command (linha, var, expr)

  # <output> ::= output <intexpr>
  def procOutput(self):
    self.advance(TokenType.TT_OUTPUT)
    linha = int(self.currentToken.linha)
    expr = self.procIntExpr()
    
    return Output_Command (linha, expr)

  # <if> ::= if <boolexpr> then <cmdlist> [ else <cmdlist> ] done
  def procIf(self):
    self.advance(TokenType.TT_IF)
    linha = int(self.currentToken.linha)

    bool_expr = self.procBoolExpr()
    self.advance(TokenType.TT_THEN)

    then_command = self.procCmdList()
    else_command = None

    if self.currentToken.type == TokenType.TT_ELSE:
      self.nextToken()
      else_command = self.procCmdList()

    self.advance(TokenType.TT_DONE)
    
    return If_Command(linha, bool_expr, then_command, else_command)

  # <while> ::= while <boolexpr> do <cmdlist> done
  def procWhile(self):
    self.advance(TokenType.TT_WHILE)
    linha = int(self.currentToken.linha)

    bool_expr = self.procBoolExpr()

    self.advance(TokenType.TT_DO)

    program_command = self.procCmdList()
    self.advance(TokenType.TT_DONE)

    return While_Command(linha, bool_expr, program_command)

  # <boolexpr> ::= false | true |
  #                not <boolexpr> |
  #                <intterm> (== | != | < | > | <= | >=) <intterm>
  def procBoolExpr(self):
    if self.currentToken.type == TokenType.TT_FALSE:
      self.nextToken()
      linha = int(self.currentToken.linha)
      
      return ConstBoolExpr(linha, False)

    elif self.currentToken.type == TokenType.TT_TRUE:
      self.nextToken()
      linha = int(self.currentToken.linha)
      
      return ConstBoolExpr(linha, False)
      
    elif self.currentToken.type == TokenType.TT_NOT:
      self.nextToken()
      linha = int(self.currentToken.linha)
      bool_expr = self.procBoolExpr()
      
      return NotBoolExpr (linha, bool_expr)

    else:
      linha = int(self.currentToken.linha)
      expr_left = self.procIntTerm()
      log_op = None

      if self.currentToken.type == TokenType.TT_EQUAL:
        log_op = SingleBoolExpr.Op.TT_EQUAL
        self.nextToken()

      elif self.currentToken.type == TokenType.TT_NOT_EQUAL:       
        log_op = SingleBoolExpr.Op.TT_NOT_EQUAL
        self.nextToken()

      elif self.currentToken.type ==TokenType.TT_LOWER: 
        log_op = SingleBoolExpr.Op.TT_LOWER
        self.nextToken()

      elif self.currentToken.type == TokenType.TT_LOWER_EQUAL:
        log_op = SingleBoolExpr.Op.TT_LOWER_EQUAL
        self.nextToken()

      elif self.currentToken.type == TokenType.TT_GREATER: 
        log_op = SingleBoolExpr.Op.TT_GREATER
        self.nextToken()

      elif self.currentToken.type == TokenType.TT_GREATER_EQUAL: 
        log_op = SingleBoolExpr.Op.TT_GREATER_EQUAL
        self.nextToken()

      else:
        self.showError()

      expr_right = self.procIntTerm()
      
      return SingleBoolExpr (linha, expr_left, log_op, expr_right)

  # <intexpr> ::= [ + | - ] <intterm> [ (+ | - | * | / | %) <intterm> ]
  def procIntExpr(self):
    boolean = False 
    left = None
    op = None

    if self.currentToken.type == TokenType.TT_ADD:
      self.nextToken()

    elif self.currentToken.type == TokenType.TT_SUB:
      self.nextToken()
      boolean = True

    if boolean:    
      linha = int(self.currentToken.linha)
      int_expr = self.procIntTerm()
      left = NegIntExpr(linha, int_expr)

    else:
      linha = int(self.currentToken.linha)
      left = self.procIntTerm()

    if self.currentToken.type == TokenType.TT_ADD:
      op = BinaryIntExpr.Op.TT_ADD
      self.nextToken()
      right = self.procIntTerm()
      left = BinaryIntExpr (linha, left, op, right)

    elif self.currentToken.type == TokenType.TT_SUB:
      op = BinaryIntExpr.Op.TT_SUB
      self.nextToken()
      right = self.procIntTerm()
      left = BinaryIntExpr (linha, left, op, right)

    elif self.currentToken.type == TokenType.TT_MUL:
      op = BinaryIntExpr.Op.TT_MUL
      self.nextToken()
      right = self.procIntTerm()
      left = BinaryIntExpr (linha, left, op, right)

    elif self.currentToken.type == TokenType.TT_DIV:
      op = BinaryIntExpr.Op.TT_DIV
      self.nextToken()
      right = self.procIntTerm()
      left = BinaryIntExpr (linha, left, op, right)

    elif self.currentToken.type == TokenType.TT_MOD:
      op = BinaryIntExpr.Op.TT_MOD
      self.nextToken()
      right = self.procIntTerm()
      left = BinaryIntExpr (linha, left, op, right)

    return left

  # <intterm> ::= <var> | <const> | read
  def procIntTerm(self):
    if self.currentToken.type == TokenType.TT_VAR:
      return self.procVar()

    elif self.currentToken.type == TokenType.TT_NUMBER:
      return self.procConst()

    else:
      self.advance(TokenType.TT_READ)
      linha = int(self.currentToken.linha)
      
      return ReadIntExpr(linha)

  # <var> ::= id
  def procVar(self):
    name = self.currentToken.token
    self.advance(TokenType.TT_VAR)

    return Variable (name).getVariavel(name)

  # <const> ::= number
  def procConst(self):
    name = self.currentToken.token
    self.advance(TokenType.TT_NUMBER)
    linha = int(self.currentToken.linha)
    num = int(name)

    return ConstIntExpr (linha, num)
