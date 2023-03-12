import random

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
email = ['nome1@icloud.com', 'nome2@live.com','nome3@icloud.com', 'nome4@icloud.com', 'nome5@gmail.com']
telefones = ['11999999999', '19999999999','81999999999', '13999999999', '15999999999']
cidades = ['São Paulo', 'Salvador','Santana de Parnaiba', 'Barueri', 'Carapicuiba']
estados = ['SP', 'MG', 'RJ', 'BA', 'RS']




print("\n\nBem-vindo ao gerador de dados de Testes - Para finalizar o programa, digite 'parar'\n\n")
print("-----------------------------------------")

while True:
    try:
        arquivo = open("dados_gerados.txt", "a")
        gerarNome = random.choice(nomes)
        gerarEmail = random.choice(email)
        gerarTelefones = random.choice(telefones)
        gerarCidades = random.choice(cidades)
        gerarEstados = random.choice(estados)
        print("Escolha uma ou mais opções abaixo a serem geradas aleatoriamente!")
        escolha = input(
            "[1] - Nome\n[2] - Email\n[3] - Telefone\n[4] - Cidade\n[5] - Estado\n[parar] - para finalizar o programa\nDigite uma ou mais opções separadas por vírgula: ")
        if escolha == 'parar':
            print("Software finalizado pelo usuário...")
            break

        opcoes = escolha.split(',')
        for opcao in opcoes:
            if opcao == '1':
                print(gerarNome)
                arquivo.write("Nome gerado: " + gerarNome + "\n")
            elif opcao == '2':
                print(gerarEmail)
                arquivo.write("Email gerado: " + gerarEmail + "\n")
            elif opcao == '3':
                print(gerarTelefones)
                arquivo.write("Telefone gerado: " + gerarTelefones + "\n")
            elif opcao == '4':
                print(gerarCidades)
                arquivo.write("Cidade gerada: " + gerarCidades + "\n")
            elif opcao == '5':
                print(gerarEstados)
                arquivo.write("Estado gerado: " + gerarEstados + "\n")
            else:
                print(
                    "Escolheu uma opção inválida (digite apenas o número da opção desejada)")
        arquivo.write("--------------------------------------\n")
        arquivo.close()
    except:
        print("Ocorreu um erro inesperado!")
    
