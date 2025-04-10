import time
import os
def limpar():
    if os.name == 'nt':
        os.system('cls')
#pagamento
def registrar_pagamento():
    global tempo, valor, kilometros

    while True:
        entrada = input("\n📅 Digite a quantidade de semanas que você ficou com o carro: ")
        try:
            tempo = int(entrada)
            break
        except ValueError:
            print("❌ Erro: você deve digitar apenas números.\n")

    while True:
        valortemp = input(f"\n💸 Digite o valor pago semanalmente para alugar o carro por {tempo} semanas: ")
        try:
            valor = int(valortemp)
            break
        except ValueError:
            print("❌ Erro: você deve digitar apenas números.\n")

    while True:
        kilometrostemp = input("\n🚗💨 Digite a quantidade de kms que você rodou com o carro: ")
        try:
            kilometros = int(kilometrostemp)
            break
        except ValueError:
            print("❌ Erro: você deve digitar apenas números.\n")

    print("\n✅ Pagamento registrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
#menuzinho

#funcão que cria o relatório dos usuários ⬇️
relatorios = {}

def criar_relatorio():
    global relatorios
    nome = input("\n🧑 Digite seu nome: ")
    carro = input("\n🚗 Modelo do carro alugado: ")
    while True:
        semanastemp = input("\n📅 Por quantas semanas alugou o carro? ")
        try:
            semanas= int(semanastemp)
            break
        except ValueError:
            print("⚠️ Por favor, digite um número válido para o valor.")

    while True:
        valor_pago_temp = input("\n💸 Valor semanal pago?: ")
        try:
            valor_pago = float(valor_pago_temp)
            break
        except ValueError:
            print("⚠️ Por favor, digite um número válido para o valor.")

    while True:
        kms = input("\n🚗💨 Quantos kilometros foi rodado? ")
        try:
            km = float(kms)
            break
        except ValueError:
            print("⚠️ Por favor, digite um número para kilometros.")

    avaliacao = input("\n✍️ Escreva sua avaliação sobre o carro🚗: ")

    relatorios[nome] = {
        "Carro": carro,
        "Dias": semanas,
        "Valor Pago": valor_pago,
        "Kilometragem": km,
        "Avaliação": avaliacao
    }

    print("\n✅ Relatório criado com sucesso!\n")

    nome_arquivo = f"relatorio_{nome}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de {nome}\n")
        arquivo.write(f"Carro alugado: {carro}\n")
        arquivo.write(f"Dias alugados: {semanas}\n")
        arquivo.write(f"Valor pago: R$ {valor_pago}\n")
        arquivo.write(f"Avaliação: {avaliacao}\n")

    print(f"📁 Relatório salvo como '{nome_arquivo}'")
    print("\n📁Salvando relatório aguarde...⏳")
    time.sleep(3)

    visualizar = input("Você deseja visualizar seu relatório? (SIM ou NÃO): ").strip().upper()
    if visualizar == "SIM":
        print("\nAbrindo relatório⏳")
        time.sleep(2)
        os.system(f"start {nome_arquivo}")
def menu():
    while True:
        limpar()
        print("\n📋 MENU DO SISTEMA DE PAGAMENTO")
        print("1️⃣  Registrar pagamento")
        print("2️⃣  Criar novo relatório")
        print("3️⃣  Sair do sistema")

        opcao = input("\nEscolha uma opção (1|2|3): ").strip()

        if opcao == "1":
            registrar_pagamento()
        elif opcao == "2":
            criar_relatorio()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            limpar()
            print("\nObrigado por utilizar nossa empresa 😊")
            break
        else:
            print("❌ Opção inválida. Tente novamente")
            time.sleep(2)
menu()