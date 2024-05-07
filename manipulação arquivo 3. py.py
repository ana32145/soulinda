def copiar_conteudo_arquivo():
    try:
        with open('bia.txt', 'r') as origem:
            conteudo = origem.read()
        with open('bia.txt', 'w') as destino:
            destino.write(conteudo)
        print("Conteúdo copiado com sucesso para 'bia.txt'.")
    except FileNotFoundError:
        print("Arquivo 'bia.txt' não encontrado.")

# Exemplo de uso:
copiar_conteudo_arquivo()
