dep = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros: "))
calculo = (taxa * dep) / 100
soma = dep + calculo
i = 1
arredondarCalculo = round(calculo, 2)
arredondarSoma = round(soma, 2)

print(f"Para o mês inicial o valor de taxa é de {taxa} e o valor total é de {dep}")

while (i <= 24):
    print(f"Para o mês {i} o valor de taxa será de {arredondarCalculo} e o valor total será de {arredondarSoma}")
    i += 1
    calculo = (soma * taxa) / 100
    soma += calculo
    arredondarCalculo = round(calculo, 2)
    arredondarSoma = round(soma, 2)
