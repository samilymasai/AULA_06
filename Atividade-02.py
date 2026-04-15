resposta = "S"
s = 0
while resposta != "N":
    n = int(input('informe o número: '))
    if n > 1000:
        d = n * 0.10
        dn = n - d
        print(f"Valor com desconto é : {dn}")
    else:
        print(f"Desconto não aplicado com {n}.")
    resposta = input("Quer continuar? [S/N]").upper().strip()[0]
print(f"Final do valor foi sem/com o desconto por :{n} :{dn}")