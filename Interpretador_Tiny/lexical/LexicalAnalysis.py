from lexical.SymbolTable import SymbolTable
from lexical.TokenType import TokenType
from lexical.Lexeme import Lexeme

class LexicalAnalysis:
  def __init__ (self):
    self.lines  = []
    self.tokenList = []

  def readFile(self, nome):
    try:
      with open(nome, 'r') as arquivo:
        self.c = arquivo.read()
        arquivo.seek(0)
        self.lines = arquivo.readlines()
        return self.c
    
    except FileNotFoundError:
      print(f"O arquivo {nome} não foi encontrado.")
          
  def nextToken(self, c):
    current_lexeme = ''
    estado = 1
    posicao_atual = 0
    linhas = 1
    tam_arquivo = len(c)
    lexema_final = Lexeme (' ', ' ', 0)
    
    while posicao_atual <= tam_arquivo:  

      # 1- O estado onde o automato começa e se mantem ao ler espaços em branco e novas linhas
      if estado == 1:
        if posicao_atual == tam_arquivo:
          lexema_final = Lexeme('', TokenType.TT_END_OF_FILE, linhas)
          self.tokenList.append(lexema_final)
          break
              
        elif c[posicao_atual] in (' ', '\r', '\t', '\n'):
          if c[posicao_atual] == '\n':
            linhas += 1
            
          posicao_atual = posicao_atual + 1 
          estado = 1

        elif c[posicao_atual] == '#':
          posicao_atual = posicao_atual + 1
          estado = 2
              
        elif c[posicao_atual] in ('=', '<', '>'):
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1 
          estado = 3
              
        elif c[posicao_atual] == '!':
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 4
          
        elif c[posicao_atual] in (';', '+', '-', '*', '%', '/'):
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 7
          
        elif c[posicao_atual].isalpha() == True:
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 5
          
        elif c[posicao_atual].isdigit() == True:
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual =  posicao_atual + 1
          estado = 6
          
        else:
          current_lexeme = current_lexeme + c[posicao_atual]
          lexema_final = Lexeme (current_lexeme, TokenType.TT_INVALID_TOKEN, linhas)
          print(f"(_{current_lexeme}_, {lexema_final.type}, linha: {lexema_final.linha})")
          self.tokenList.append(lexema_final)
          print('\nQuebra de execução......')
          exit()  

      # 2 - O estado que representa a leitura de comentarios, o automato continua nele até ler uma nova linhas
      elif estado == 2:
        if c[posicao_atual] != '\n':
          posicao_atual = posicao_atual + 1
          estado = 2
            
        elif c[posicao_atual] == '\n':
          if c[posicao_atual] == '\n':
            linhas += 1
            
          posicao_atual =  posicao_atual + 1
          estado = 1
      
      # 3 - O estado que representa a leitura de uma atribuicao (=) ou comparacao (>, <, >=, <=, ==)
      elif estado == 3:
        if c[posicao_atual] == '=':
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 7
        
        else:
          estado = 7

      # 4 - Estado que lida com o operador de negação (!).
      elif estado == 4:
        if c[posicao_atual] == '=':
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 7 
            
        elif posicao_atual == tam_arquivo - 1:
          current_lexeme = current_lexeme + c[posicao_atual]
          lexema_final = Lexeme (current_lexeme, TokenType.TT_UNEXPECTED_EOF, linhas)
          print(f"(_{current_lexeme}_, {lexema_final.type}), linha: {lexema_final.linha}")
          self.tokenList.append(lexema_final)                        
          print('\nQuebra de execução......')
          exit()
            
        else:
          current_lexeme = current_lexeme + c[posicao_atual]
          lexema_final = Lexeme (current_lexeme, TokenType.TT_INVALID_TOKEN, linhas)
          print(f"(_{current_lexeme}_, {lexema_final.type}, linha: {lexema_final.linha})")
          self.tokenList.append(lexema_final)
          print('\nQuebra de execução......')
          exit()
              

      # 5 - Estado que lida com letras e identificadores.
      elif estado == 5:
        if c[posicao_atual].isalpha() == True:
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 5
          
        elif c[posicao_atual].isalpha() == False:
          estado = 7

      # 6 - Estado que lida com dígitos e números.
      elif estado == 6:
        if c[posicao_atual].isdigit() == True:
          current_lexeme = current_lexeme + c[posicao_atual]
          posicao_atual = posicao_atual + 1
          estado = 6
          
        elif c[posicao_atual].isdigit() == False:
          if current_lexeme in SymbolTable:
            token_type = SymbolTable[current_lexeme]

          else:
            token_type = TokenType.TT_NUMBER

          lexema_final = Lexeme(current_lexeme, token_type, linhas)
          self.tokenList.append(lexema_final)
          current_lexeme = ''
          estado = 1

      # 7 - Estado que verifica se o token é um identificador.
      elif estado == 7:
        if current_lexeme in SymbolTable:
          token_type = SymbolTable[current_lexeme]
        
        else:
          token_type = TokenType.TT_VAR

        lexema_final = Lexeme(current_lexeme, token_type, linhas)
        self.tokenList.append(lexema_final)
        current_lexeme = ''
        estado = 1