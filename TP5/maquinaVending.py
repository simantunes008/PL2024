import json
import ply.lex as lex

saldo = 0.0
moeda_mode = False
selecionar_mode = False


with open('stock.json', 'r') as json_file:
    stock = json.load(json_file)


def converte_valor(valor):
    valor_euros = int(valor)
    valor_centimos = int((valor - valor_euros) * 100)
    
    if valor_euros != 0 and valor_centimos != 0:
        resultado = f"{valor_euros}e{valor_centimos}c"
    elif valor_euros != 0 and valor_centimos == 0:
        resultado = f"{valor_euros}e"
    elif valor_euros == 0 and valor_centimos != 0:
        resultado = f"{valor_centimos}c"
    else:
        resultado = '0c'
    
    return resultado


def calcula_troco(valor):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1] 
    resultado = ""
    
    valor = int(valor * 100)
    
    for moeda in moedas:
        qtd_moeda = valor // moeda
        
        if qtd_moeda > 0:
            if moeda >= 100:
                resultado += f"{qtd_moeda}x {moeda // 100}e, "
            else:
                resultado += f"{qtd_moeda}x {moeda}c, "
            
            valor -= moeda * qtd_moeda
    
    if resultado:
        resultado = resultado[:-2]
        resultado += '.'
    else:
        resultado = '0x 0c.'
    
    return resultado


tokens = (
    'OP',
    'ID',
    'MOEDA',
    'VIR',
    'PONTO'
)


t_VIR = r','
t_ignore  = ' \t\n'


def t_OP(token):
    r'\b[A-Z]+\b'
    global moeda_mode, selecionar_mode
    
    if token.value == 'LISTAR':
        print('maq:')
        print('cod | nome | quantidade | preço')
        print('------------------')
        for produto in stock:
            print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")
    
    if token.value == 'MOEDA':
        moeda_mode = True
    
    if token.value == 'SELECIONAR':
        selecionar_mode = True
    
    if token.value == 'SAIR':
        print(f'maq: Pode retirar o troco: {calcula_troco(saldo)}')
        print('maq: Até à próxima')


def t_ID(token):
    r'[A-Z]\d+'
    global selecionar_mode, stock, saldo
    
    if selecionar_mode:
        for produto in stock:
            if produto['cod'] == token.value:
                if saldo > produto['preco']:
                    saldo -= produto['preco']
                    produto['quant'] -= 1
                    print(f'Pode retirar o produto "{produto["nome"]}"')
                    print(f'maq: Saldo = {converte_valor(saldo)}')
                else:
                    print('maq: Saldo insuficiente para satisfazer o seu pedido')
                    print(f'maq: Saldo = {converte_valor(saldo)}; Pedido = {converte_valor(produto["preco"])}')
    selecionar_mode = False


def t_MOEDA(token):
    r'\d+[ec]'
    global saldo
    
    if moeda_mode:
        if token.value.endswith('e'):
            saldo += float(token.value[:-1])
        else:
            saldo += float(token.value[:-1]) * 0.01


def t_PONTO(token):
    r'\.'
    global moeda_mode
    moeda_mode = False
    print(f'maq: Saldo = {converte_valor(saldo)}')


def t_error(token):
    token.lexer.skip(1)


lexer = lex.lex()


def tokenize_input(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break


print('maq: 2024-03-08, Stock carregado, Estado atualizado.')
print('maq: Bom dia. Estou disponível para atender o seu pedido')
while True:
    user_input = input('>> ')
    tokenize_input(user_input)
    if user_input == "SAIR":
        break


with open('stock.json', 'w') as json_file:
    json.dump(stock, json_file, indent=4)
