valorA = int(input("Digite valor de A: "))
valorB = int(input("Digite valor de B: "))
valorC = int(input("Digite valor de C: "))
soma = valorA + valorB

if soma < valorC:
    print(f"{soma} (soma de {valorA} + {valorB}) é menor que {valorC}.")
else:
    print(f"{valorA} + {valorB} = {soma}\nÉ igual ou maior a {valorC}")
