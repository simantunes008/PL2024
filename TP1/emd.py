import sys
import re

divisao_patern = re.compile(r',')

sys.stdin.readline()
linhas = sys.stdin.readlines()

modalidades = []
aptos = 0
imptos = 0
numero_de_atletas = len(linhas)
escaloes = {}

for linha in linhas:
    linha = linha.rstrip('\n')
    campos = divisao_patern.split(linha)
    
    # Verifica se a modalidade já existe e adiciona-a
    if campos[8].lower() not in modalidades:
        modalidades.append(campos[8].lower())
    
    # Verifica se o atleta está apto
    if re.match(r'^true$', campos[12].lower()):
        aptos += 1
    elif re.match(r'^false$', campos[12].lower()):
        imptos += 1
    
    # Calcula o escalão com base na divisão inteira por 5
    idade = int(campos[5])
    escalao = idade // 5
    if escalao in escaloes:
        escaloes[escalao] += 1
    else:
        escaloes[escalao] = 1

modalidades.sort() # Ordena a lista de modalidades

print("Modalidades:", modalidades)
print(f"Porcentagem de atletas aptos: {aptos / numero_de_atletas * 100:.2f}% ({aptos} atletas)")
print(f"Porcentagem de atletas imptos: {imptos / numero_de_atletas * 100:.2f}% ({imptos} atletas)")
print("Distribuição de atletas por escalão etário:")
for escalao, numero_de_atletas_p_escalao in escaloes.items():
    porcentagem = (numero_de_atletas_p_escalao / numero_de_atletas) * 100
    print(f"- Escalão {escalao}: {porcentagem:.2f}% ({numero_de_atletas_p_escalao} atletas)")
