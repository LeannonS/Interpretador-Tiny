from lexical.TokenType import TokenType

SymbolTable = {
  # Símbolos
	';': TokenType.TT_SEMICOLON,
	'=': TokenType.TT_ASSIGN,

	# Operadores lógicos de comparação
	'==': TokenType.TT_EQUAL,
	'!=': TokenType.TT_NOT_EQUAL,
	'<':  TokenType.TT_LOWER,
	'<=': TokenType.TT_LOWER_EQUAL,
	'>':  TokenType.TT_GREATER,
	'>=': TokenType.TT_GREATER_EQUAL,

	# Operadores Aritméticos
	'+': TokenType.TT_ADD,
	'-': TokenType.TT_SUB,
	'*': TokenType.TT_MUL,
	'/': TokenType.TT_DIV,
	'%': TokenType.TT_MOD,
	'^': TokenType.TT_POT,

	# Palavras-chave da linguagem Tiny
	'program': TokenType.TT_PROGRAM,
	'while': TokenType.TT_WHILE,
	'do': TokenType.TT_DO,
	'done': TokenType.TT_DONE,
	'if': TokenType.TT_IF,
	'then': TokenType.TT_THEN,
	'else': TokenType.TT_ELSE,
	'output': TokenType.TT_OUTPUT,
	'true': TokenType.TT_TRUE,
	'false': TokenType.TT_FALSE,
	'read': TokenType.TT_READ,
	'not': TokenType.TT_NOT,
}
