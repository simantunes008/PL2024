import sys

sys.stdin.readline()

linhas = sys.stdin.readlines()

modalidades = []
aptos = 0
imptos = 0
numero_de_atletas = len(linhas)

for linha in linhas:
    campos = linha.split(",")
    modalidade = campos[8]
    apto = campos[12].strip()
    # Verifica se o altleta está apto ou não
    if apto == 'true':
        aptos += 1
    elif apto == 'false':
        imptos += 1
    # Verifica se a modalidade já está na lista
    if modalidade not in modalidades:
        # Caso não esteja adciona-a
        modalidades.append(modalidade)

modalidades.sort()

print("Modalidades:", modalidades)
print("Porcentagem de atletas aptos: {:.2f}%".format(aptos / numero_de_atletas * 100))
print("Porcentagem de atletas imptos: {:.2f}%".format(imptos / numero_de_atletas * 100))
