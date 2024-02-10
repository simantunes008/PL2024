import sys

sys.stdin.readline()

linhas = sys.stdin.readlines()

modalidades = []
aptos = 0
imptos = 0
numero_de_atletas = len(linhas)
escaloes = {}

for linha in linhas:
    campo = linha.split(",")
    modalidade = campo[8].strip().lower()
    apto = campo[12].strip().lower()
    idade = int(campo[5])
    
    # Verifica se a modalidade já está na lista
    if modalidade not in modalidades:
        # Caso não esteja adciona-a
        modalidades.append(modalidade)
    
    # Verifica se o altleta está apto ou não
    if apto == 'true':
        aptos += 1
    elif apto == 'false':
        imptos += 1
    
    # Calcula o escalão com base na idade
    escalao = idade // 5 # Divisão inteira por 5
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
