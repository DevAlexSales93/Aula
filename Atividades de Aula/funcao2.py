def calcular_imc(altura, peso): 
    imc = peso / (altura * altura)

    print(f"\nIMC:{imc:.2f}")

    if imc < 18.5:
        print("Situação: Abaixo do peso")
    elif imc < 25:
        print("Situação: Peso normal")        
    elif imc < 30:        
        print("Situação: Sobrepeso")
    elif imc < 35:
        print("Situação: Obesidade Grau I")        
    elif imc < 40:
        print("Situação: Obesidade Grau II")        
    else:
        print("Situação: Obesidade Grau III")  

altura = float(input("Digite sua altura (em metros): "))        
peso = float(input("Digite seu peso (em kg): "))

calcular_imc(altura, peso)
