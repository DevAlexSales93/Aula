def calcular_anos_caninos(idade):
    if idade <= 0:
        return 0
    elif idade == 1:
        return 15
    elif idade == 2:
        return 24
    else:
        return 24 + (idade - 2) * 5


idade = int(input("Digite a idade do cachorro: "))
print(f"A idade humana equivalente é: {calcular_anos_caninos(idade)} anos.")