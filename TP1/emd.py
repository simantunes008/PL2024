import sys
import re

# Regex para dividir uma linha csv
divisao_patern = re.compile(r',')

sys.stdin.readline()
linhas = sys.stdin.readlines()

modalidades = []
aptos = 0
inaptos = 0
numero_de_atletas = len(linhas)
escaloes = {}

for linha in linhas:
    linha = linha.rstrip('\n')
    campos = divisao_patern.split(linha)
    
    # Verifica se a modalidade já está na lista e caso contrário adiciona-a
    if campos[8].lower() not in modalidades:
        modalidades.append(campos[8].lower())
    
    # Verifica através do Regex se um atleta está apto ou não
    if re.match(r'^true$', campos[12].lower()):
        aptos += 1
    elif re.match(r'^false$', campos[12].lower()):
        inaptos += 1
    
    # Verifica através do Regex se a idadde é um inteiro válido
    if re.match(r'^\d+$', campos[5]):
        escalao = int(campos[5]) // 5
        if escalao in escaloes:
            escaloes[escalao] += 1
        else:
            escaloes[escalao] = 1

print("Modalidades:")
for i, modalidade in enumerate(sorted(modalidades), 1):
    print(f"- Modalidade {i}: {modalidade.capitalize()}")
print(f"Porcentagem de atletas aptos: {aptos / numero_de_atletas * 100:.2f}% ({aptos} atletas)")
print(f"Porcentagem de atletas inaptos: {inaptos / numero_de_atletas * 100:.2f}% ({inaptos} atletas)")
print("Distribuição de atletas por escalão etário:")
for escalao, numero_de_atletas_p_escalao in escaloes.items():
    porcentagem = (numero_de_atletas_p_escalao / numero_de_atletas) * 100
    print(f"- Escalão {escalao}: {porcentagem:.2f}% ({numero_de_atletas_p_escalao} atletas)")
