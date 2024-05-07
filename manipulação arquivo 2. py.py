def imprimir_conteudo_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")

# Exemplo de uso:
imprimir_conteudo_arquivo()