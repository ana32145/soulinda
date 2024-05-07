def buscar_nome_por_numero():
    numero = int(input("Digite um número: "))
    try:
        with open('arquivo_exemplo.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if 1 <= numero <= len(linhas):
                nome = linhas[numero - 1].strip()
                print(f"Nome correspondente ao número {numero}: {nome}")
            else:
                print(f"Nenhum nome encontrado para o número {numero}.")
    except FileNotFoundError:
        print("Arquivo 'bia.txt' não encontrado.")

# Exemplo de uso:
buscar_nome_por_numero()