import ply.lex as lex

tokens = (
    'VARIABLE',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ASSIGN',
    'QUESTION',
    'EXCLAMATION',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_QUESTION = r'\?'
t_EXCLAMATION = r'!'

def t_VARIABLE(t):
    r'[a-zA-Z][\w]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Descomentar para debug
# data = '''
# ? a
# ! a * 2 + 7
# b = (a + 3) * 4 - 5
# ! a + b
# '''
# 
# lexer.input(data)
# 
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break
#     print(tok)
