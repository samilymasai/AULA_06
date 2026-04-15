# Estrutura de Repetição while
# Números até 10
i = 1
while i <= 10:
    print(i)
    i += 1
# Exemplo 01
n = 1
soma = 0
while n != 0:
    n = int(input("Digite um número: "))
    soma += n
print(f"O resultado Total é: {soma}")

# Exemplo 02
resposta = "S"
soma = 0
while resposta != "n" :
    n = int(input("Informe o número: "))
    soma += n
    resposta = input("Quer continuar? [S/N]").upper().strip()[0]

print(f"O Total da soma é: {soma}")