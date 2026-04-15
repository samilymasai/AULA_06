#n1 = float(input('Nota 1:'))
#n2 = float(input('Nota 2:'))
#media = (n1 + n2) / 2
#print(media)

# Estrutura de repetições (for)
#for i in  range(3):
#    print('Olá mundo !')

#qtd = int(input("Que contar até quanto? '"))
#for i in range(qtd):
#        print(i, end="boi ") #imprime na mesma linha

# Soma = 0
#for u in range(3):
#        print(f"\nRodada {u+1}")
#        num1 = int(input("Informe o número: "))
#        num2 = int(input("Informe o segundo número: "))
#        soma = num1 + num2
#        print(f"O total é {soma}")
        
# Variável Acumuladora 
#soma = 0
#for i in range(3):
#    numero = float(input("Digite um número:"))
#    soma = soma + numero

#print(f"O total é {soma}")

# print(f"\nO Valor é {soma}")

soma = 0
for v in range(3):
    venda = float(input('Informe o valor: '))

    if venda > 100:
        #soma = soma + venda 
        soma += venda 
        print(f"Valor R$ {venda} somado")
    else:
        print("Valor não computado")

print(f"\nTotak de R$ {soma}")

