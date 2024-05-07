def imprimir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome} - Idade: {idade} - Cidade: {cidade}")

# Exemplo de uso:
imprimir_informacoes("Alice", 25, "São Paulo")

def calcular_operacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {resultado}")

# Exemplo de uso:
calcular_operacao()

def criar_lista_compras():
    itens = input("Digite os itens da lista de compras (separados por vírgula): ")
    lista = itens.split(", ")

    for i, item in enumerate(lista, start=1):
        print(f"Item {i}: {item}")

# Exemplo de uso:
criar_lista_compras()

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.2f}")

def capturar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        nomes.append(nome)

    print("Nomes digitados:")
    for i, nome in enumerate(nomes, start=1):
        print(f"Nome {i}: {nome}")

# Exemplo de uso:
capturar_nomes()



