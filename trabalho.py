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
#devedor
def checar_debitos():
    while True:
        print("\n🔍 Checagem de Débitos")

        while True:
            valor_temp = input("\n💵 Qual é o valor semanal do aluguel? ")
            try:
                valor = float(valor_temp)
                break
            except ValueError:
                print("❌ Digite um número válido.")

        while True:
            total_temp = input("📅 Quantas semanas você ficou com o carro? ")
            try:
                total = int(total_temp)
                break
            except ValueError:
                print("❌ Erro: digite apenas números.")

        while True:
            pagas_temp = input("✅ Quantas semanas foram pagas normalmente? ")
            try:
                pagas = int(pagas_temp)
                if pagas > total:
                    print("❌ Erro: você não pode ter pago mais semanas do que ficou com o carro.")
                else:
                    break
            except ValueError:
                print("❌ Erro: digite apenas números.")

        while True:
            print(f"\nConfirma que você ficou {total} semanas com o carro e pagou {pagas} semanas?")
            confirmacao = input("Digite SIM para continuar ou NÃO para reiniciar: ").strip().upper()

            if confirmacao == "SIM":
                break
            elif confirmacao == "NAO" or confirmacao == "NÃO":
                print("\n🔁 Recomeçando a checagem de débitos...")
                time.sleep(2)
                limpar()
                return checar_debitos()
            else:
                print("⚠️ Resposta inválida. Digite apenas SIM ou NÃO.")
                time.sleep(2)

        atraso = total - pagas
        valor_pago = valor * pagas
        valor_atraso = valor * atraso

        print("\n📌 RESUMO:")
        print(f"📅 Total de semanas com o carro: {total}")
        print(f"✅ Semanas pagas: {pagas}")
        print(f"❌ Semanas em atraso: {atraso}")
        print(f"💵 Valor semanal: R$ {valor:.2f}")

        if atraso > 0:
            multa_percentual = 10 + (atraso - 1) * 5
            multa_valor = valor_atraso * (multa_percentual / 100)
            total_com_multa = valor_atraso + multa_valor

            print(f"\n⚠️ Multa aplicada: {multa_percentual}%")
            print(f"💣 Valor devido (atraso): R$ {valor_atraso:.2f}")
            print(f"➕ Multa sobre atraso: R$ {multa_valor:.2f}")
            print(f"💰 Total a pagar (somente atraso): R$ {total_com_multa:.2f}")
        else:
            print(f"\n✅ Nenhum débito! Total pago: R$ {valor_pago:.2f}")
        input("\nPressione Enter para voltar ao menu...")
        break        
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
        "Semanas": semanas,
        "Valor Pago": valor_pago,
        "Kilometragem": km,
        "Avaliação": avaliacao
    }

    print("\n✅ Relatório criado com sucesso!\n")

    nome_arquivo = f"relatorio_{nome}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de {nome}\n")
        arquivo.write(f"Carro alugado: {carro}\n")
        arquivo.write(f"Semanas alugadas: {semanas}\n")
        arquivo.write(f"Valor pago: R$ {valor_pago}\n")
        arquivo.write(f"Avaliação: {avaliacao}\n")

    print(f"📁 Relatório salvo como '{nome_arquivo}'")
    print("\n📁Salvando relatório aguarde...⏳")
    time.sleep(3)
    limpar()
    while True:
        visualizar = input("Você deseja visualizar seu relatório? (SIM ou NÃO): ").strip().upper()
        if visualizar == "SIM":
            print("\nAbrindo relatório⏳")
            time.sleep(2)
            os.system(f"start {nome_arquivo}")
            break
        elif visualizar == "NÃO" or visualizar == "NAO":
            print("📝 Relatório criado, mas não será aberto agora.")
            break
        else:
            print("⚠️ Resposta inválida. Digite apenas SIM ou NÃO.")
def menu():
    while True:
        limpar()
        print("\n📋 MENU DO SISTEMA DE PAGAMENTO")
        print("1️⃣  Registrar pagamento")
        print("2️⃣  Criar novo relatório")
        print("3️⃣  Checar débitos")
        print("4️⃣  Sair do sistema")

        opcao = input("\nEscolha uma opção (1|2|3|4): ").strip()

        if opcao == "1":
            registrar_pagamento()
        elif opcao == "2":
            criar_relatorio()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            checar_debitos()
        elif opcao == "4":
            limpar()
            print("\nObrigado por utilizar nossa empresa 😊")
            break
        else:
            print("❌ Opção inválida. Tente novamente")
            time.sleep(2)
menu()