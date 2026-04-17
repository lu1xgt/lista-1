preco = float(input("digite o preço do produo: "))
porcen = float(input("digite o percentual do desconto: "))

desconto = ((porcen / 100) * preco)
novoPreco = (preco - desconto)

print (f"o desconto é de {desconto} e o preço a pagar é de {novoPreco}")