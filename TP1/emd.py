import sys

sys.stdin.readline()

linhas = sys.stdin.readlines()

modalidades = []
aptos = 0
imptos = 0
numero_de_atletas = len(linhas)

for linha in linhas:
    campo = linha.split(",")
    modalidade = campo[8]
    apto = campo[12].strip()
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
    
    print(idade)

modalidades.sort()

print("Modalidades:", modalidades)
print("Porcentagem de atletas aptos: {:.2f}%".format(aptos / numero_de_atletas * 100))
print("Porcentagem de atletas imptos: {:.2f}%".format(imptos / numero_de_atletas * 100))
