def calcular_media_e_soma(lista):
    # Calcula a soma dos números na lista
    soma = sum(lista)
    # Calcula a média dividindo a soma pelo número de elementos
    media = soma / len(lista)
    return soma, media

# Exemplo de uso:
numeros = [1, 2, 3, 4]
soma_resultado, media_resultado = calcular_media_e_soma(numeros)
print(f"Soma: {soma_resultado}, Média: {media_resultado:.2f}")
def substituir_palavra(lista, palavra_procurada, nova_palavra):
    return [palavra.replace(palavra_procurada, nova_palavra) for palavra in lista]

# Exemplo de uso:
palavras = ["banana", "morango", "limão"]
palavra_procurada = "morango"
nova_palavra = "abacaxi"
lista_alterada = substituir_palavra(palavras, palavra_procurada, nova_palavra)
print(lista_alterada)
def gerar_triangulo_asteriscos(num_linhas):
    for i in range(1, num_linhas + 1):
        print(" " * (num_linhas - i) + "*" * (2 * i - 1))

# Exemplo de uso:
num_linhas_triangulo = 5
gerar_triangulo_asteriscos(num_linhas_triangulo)





