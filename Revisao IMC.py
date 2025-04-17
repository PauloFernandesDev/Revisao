print("************* IMC (Indice de Massa Corporal) *************")
peso = float(input("Digite seu peso: "))
altura = float(input("Difgite sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu imc: {imc :.1f} ")
if imc < 18.6:
    print("Abaixo do peso!")
elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal (parabéns)")
elif imc >= 25.0 and imc <= 29.9:
    print("Levemente acima do peso")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35.0 and imc<= 39.9:
    print("Obesidade grau II")
elif imc >= 40.0:
    print("Obesidade grau III")

