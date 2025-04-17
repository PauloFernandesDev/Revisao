resp = "s"
while resp == "s" and "S":
    numero = int(input("Digite um numero: "))
    if numero %2 == 0:
            if numero > 0:
                print(f"{numero} é par e positivo")
            else:
                print(f"{numero} é par e negativo")
    else:
        if numero > 0:
            print(f"{numero} é impar e positivo")
        else:
            print(f"{numero} é impar e negativo")
    resp = input("Deseja verificar um novo numero [s]Sim / [n]Não: ")