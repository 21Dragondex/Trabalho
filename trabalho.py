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

