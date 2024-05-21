def numeros_pares(numero):
    lista_pares = []
    for i in range(1, numero + 1):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

# Teste da função
numero_dado = int(input("Digite um número inteiro: "))
lista_de_pares = numeros_pares(numero_dado)
print("Números pares até", numero_dado, "são:", lista_de_pares)

