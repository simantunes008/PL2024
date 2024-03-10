import sys, re

def somador_on_off(texto):
    token_specification = [
        ('INT', r'[+-]?\d+'),             
        ('ON',  r'[oO][nN]'),             
        ('OFF', r'[oO][fF]{2}'),
        ('EQ', r'=')
    ]
    pattern = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    
    estado = True
    soma = 0
    iterador = 0
    
    while iterador < len(texto):
        m = re.match(pattern, texto[iterador:])
        if m:
            token = m.groupdict()
            iterador = iterador + m.end()
            if token['EQ']:
                print('=', soma)
            elif token['ON']:
                estado = True
            elif token['OFF']:
                estado = False
            elif token['INT']:
                if estado:
                    valor = int(m.group('INT'))
                    soma = soma + valor
        else:
            iterador += 1

def main():
    input = sys.stdin.read()
    somador_on_off(input)

if __name__ == '__main__':
    main()
