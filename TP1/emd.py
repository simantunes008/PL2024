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

modalidades.sort()

print("Modalidades:", modalidades)
print("Porcentagem de atletas aptos: {:.2f}%".format(aptos / numero_de_atletas * 100))
print("Porcentagem de atletas imptos: {:.2f}%".format(imptos / numero_de_atletas * 100))
print("Distribuição de atletas por escalão etário:")
for escalao, num_atletas in escaloes.items():
    porcentagem = (num_atletas / numero_de_atletas) * 100
    print(f"Escalão {escalao}: {num_atletas} atletas ({porcentagem:.2f}%)")
