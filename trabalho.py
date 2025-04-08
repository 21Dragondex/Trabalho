while True:
    entrada = input("Digite a quantidade de dias que você ficou com o carro: ")
    try:
        tempo = int(entrada)
    except ValueError:
        print("Erro: você deve digitar apenas números\n")
    valortemp = input(f"Digite o valor pago para alugar o carro por {tempo} dias: ")
    try:
        valor = int(valortemp)
        break
    except ValueError:
        print(f"Erro: você deve digitar apenas números\n")
#funcão que cria o relatório dos usuários ⬇️
relatorios = {}

relatoriotemp = input("Você gostaria de fazer um relatório sobre o carro utilizado? responda com sim ou não: ").upper()
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

if relatoriotemp == 'SIM':
    criar_relatorio()
else:
    print("Obrigado por utilizar nossa empresa 😊")

