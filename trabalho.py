import time
import os
while True:
    entrada = input("Digite a quantidade de dias que você ficou com o carro: ")
    try:
        tempo = int(entrada)
        break
    except ValueError:
        print("Erro: você deve digitar apenas números\n")

while True:
    valortemp = input(f"Digite o valor pago para alugar o carro por {tempo} dias: ")
    try:
        valor = int(valortemp)
        break
    except ValueError:
        print("Erro: você deve digitar apenas números\n")

while True:
    kilometrostemp = input("Digite a quantidade de kms que você rodou com o carro: ")
    try:
        kilometros = int(kilometrostemp)
        break
    except ValueError:
        print("Erro: você deve digitar apenas números\n")
#funcão que cria o relatório dos usuários ⬇️
relatorios = {}

def criar_relatorio():
    global relatorios

    nome = input("Digite seu nome: ")
    carro = input("Modelo do carro alugado: ")

    
    while True:
        dias = input("Por quantos dias alugou o carro? ")
        if dias.isdigit():
            dias = int(dias)
            break
        else:
            print("⚠️ Por favor, digite apenas números para os dias.")

    
    while True:
        valor_pago = input("Valor total pago: ")
        try:
            valor_pago = float(valor_pago)
            break
        except ValueError:
            print("⚠️ Por favor, digite um número válido para o valor.")

    while True:
        kms = input("Quantos kilometros foi rodado? ")
        try:
            km = float(kms)
            break
        except ValueError:
            print("⚠️ Por favor, digite um número para kilometros.")

    avaliacao = input("Escreva sua avaliação sobre o carro: ")

    relatorios[nome] = {
        "Carro": carro,
        "Dias": dias,
        "Valor Pago": valor_pago,
        "Kilometragem": km,
        "Avaliação": avaliacao
    }

    print("\n✅ Relatório criado com sucesso!\n")

    nome_arquivo = f"relatorio_{nome}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de {nome}\n")
        arquivo.write(f"Carro alugado: {carro}\n")
        arquivo.write(f"Dias alugados: {dias}\n")
        arquivo.write(f"Valor pago: R$ {valor_pago}\n")
        arquivo.write(f"Avaliação: {avaliacao}\n")

    print(f"📁 Relatório salvo como '{nome_arquivo}'")

    time.sleep(3)

    visualizar = input("Você deseja visualizar seu relatório? (SIM ou NÃO): ").strip().upper()
    if visualizar == "SIM":
        os.system(f"start {nome_arquivo}")
while True:
    relatoriotemp = input("Você gostaria de fazer um relatório sobre o carro utilizado? Responda com SIM ou NÃO: ").upper()

    if relatoriotemp == "SIM":
        criar_relatorio()
        break
    elif relatoriotemp == "NAO" or relatoriotemp == "NÃO":
        print("Obrigado por utilizar nossa empresa 😊")
        break
    else:
        print("Resposta inválida. Digite apenas SIM ou NÃO.\n")