def gravar_nome_arquivo():
    nome = input("Digite seu nome: ")
    try:
        with open('nome.txt', 'w') as arquivo:
            arquivo.write(nome)
        print(f"Nome '{nome}' gravado no arquivo 'nome.txt'.")
    except Exception as e:
        print(f"Erro ao gravar o nome: {str(e)}")

# Exemplo de uso:
gravar_nome_arquivo()




