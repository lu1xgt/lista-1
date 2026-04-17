salario = float(input("digite o seu salario em reais: "))
porcen = float(input("digite seu aumento em porcentagem: "))

aumento = ((porcen / 100) * salario)
novoSalario = (salario + aumento)

print (f"seu aumento foi de {aumento} e seu novo salario é {novoSalario}")