import sys
import re

def tokenize(code):
    token_specification = [
        ('NUM',     r'\d+'),             
        ('ATRIB',   r'>=|>|<|<=|==|!='),
        ('ID',      r'[a-z]\w*'),
        ('OP',      r'Select|From|Where'),
        ('COMA',    r','), 
        ('NEWLINE', r'\n'),           
        ('SKIP',    r'[ \t]+'),                       
        ('ERRO',    r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    for m in mo:
        dic = m.groupdict()
        if dic['NUM'] is not None:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['ATRIB'] is not None:
            t = ("ATRIB", dic['ATRIB'], linha, m.span())
        elif dic['ID'] is not None:
            t = ("ID", dic['ID'], linha, m.span())
        elif dic["OP"] is not None: 
            t = ("OP", dic['OP'], linha,m.span())
        elif dic["NEWLINE"] is not None: 
            t = ("NEWLINE", dic['NEWLINE'], linha,m.span())
        elif dic["SKIP"] is not None: 
            t = ("SKIP", dic['SKIP'], linha,m.span())
        elif dic["COMA"] is not None: 
            t = ("COMA", dic['COMA'], linha,m.span())    
        else:
            t = ("ERRO", m.group(), linha, m.span())
        reconhecidos.append(t)
    
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok) 
