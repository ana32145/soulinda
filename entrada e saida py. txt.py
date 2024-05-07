print("Olá", "mundo", sep="-") 

print("Olá", "Python", end="!\n")

print("18", "04", "2023", sep="/") 

print("Bia", "Ribeiro", "ab-papa@bol.com.br", sep="; ") 
 
print("Loading", end=" ")

print("[OK]")

nome = input("Digite seu nome:")

print("Olá", nome)
 
itens = input("arroz,feijao,couve").split(',')
print("Itens:", itens)

idade = int(input("Digite sua idade: "))
print("Daqui a cinco anos, você terá", idade + 5, "anos.")

altura = float(input("Digite sua altura em metros: "))
print("Sua altura é", altura, "metros.")

print("Digite números para adicionar à lista (digite 'done' para terminar):")
numeros = []
while True:
 entrada = input()
 if entrada.lower() == 'done':
     break
 else:
     numeros.append(int(entrada))
print("Números coletados:", numeros)
