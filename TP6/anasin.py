import ply.yacc as yacc

from analex import tokens

variables = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_statement_question(p):
    '''statement : QUESTION VARIABLE'''
    val = input()
    try:
        p[0] = int(val)
    except ValueError:
        print("Invalid input. Assuming 0.")
        p[0] = 0
    variables[p[2]] = p[0]

def p_statement_exclamation(p):
    '''statement : EXCLAMATION expression'''
    print(p[2])

def p_statement_assign(p):
    '''statement : VARIABLE ASSIGN expression'''
    variables[p[1]] = p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_variable(p):
    '''expression : VARIABLE'''
    p[0] = variables.get(p[1], 0)

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        print('')
        break
    if not s: continue
    parser.parse(s)
